from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process
import os

app = Flask(__name__)


PLACEHOLDER_IMAGE = "/static/images/placeholder.png"

#LOAD DATA 
print("Loading data...")
try:
    full_data = pd.read_csv("models/clean_data.csv")
    products = pd.read_csv("models/trending_products.csv")
    print("Data loaded successfully.")
except Exception as e:
    print(f"Error loading data: {e}")
    full_data = pd.DataFrame()
    products = pd.DataFrame()

#truncate product names
def truncate(text, length=50):
    if not isinstance(text, str):
        text = str(text)
    return text[:length] + "..." if len(text) > length else text

#CONTENT‑BASED PRE‑COMPUTATION
if not products.empty and 'Tags' in products.columns:
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(products['Tags'].fillna(''))
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    print("TF‑IDF matrix computed.")
else:
    tfidf_matrix = None
    cosine_sim = None

def content_based_recommendations(item_name, top_n=10):
    if products.empty or cosine_sim is None:
        return pd.DataFrame()
    all_names = products['Name'].astype(str).values
    match = process.extractOne(item_name, all_names, score_cutoff=70)
    if not match:
        print(f"No match found for '{item_name}'")
        return pd.DataFrame()
    best_match = match[0]
    idx = products[products['Name'] == best_match].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sim_scores[1:top_n+1]]
    recs = products.iloc[top_indices][['ProdID', 'Name', 'Brand', 'ImageURL', 'ReviewCount', 'Rating']].copy()
    recs['similarity'] = [sim_scores[i][1] for i in range(1, top_n+1)]
    recs = recs.sort_values('similarity', ascending=False)
    recs['ImageURL'] = PLACEHOLDER_IMAGE
    return recs

# COLLABORATIVE FILTERING
def collaborative_recommendations(target_user_id, top_n=10):
    if full_data.empty:
        return pd.DataFrame()
    user_item = full_data.pivot_table(index='ID', columns='ProdID', values='UserRating', aggfunc='mean').fillna(0)
    if target_user_id not in user_item.index:
        return pd.DataFrame()
    user_sim = cosine_similarity(user_item)
    user_idx = user_item.index.get_loc(target_user_id)
    sim_scores = list(enumerate(user_sim[user_idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    similar_users = [user_item.index[i] for i, _ in sim_scores[1:11]]  # top 10 similar
    target_rated = set(user_item.loc[target_user_id][user_item.loc[target_user_id] > 0].index)
    rec_scores = {}
    for u in similar_users:
        rated = user_item.loc[u]
        for prod_id in rated[rated > 0].index:
            if prod_id not in target_rated:
                weight = user_sim[user_idx][user_item.index.get_loc(u)]
                rec_scores[prod_id] = rec_scores.get(prod_id, 0) + weight * rated[prod_id]
    if not rec_scores:
        return pd.DataFrame()
    sorted_recs = sorted(rec_scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
    rec_prod_ids = [p for p, _ in sorted_recs]
    recs = products[products['ProdID'].isin(rec_prod_ids)][['ProdID', 'Name', 'Brand', 'ImageURL', 'ReviewCount', 'Rating']].copy()
    recs['collab_score'] = [rec_scores[p] for p in rec_prod_ids]
    recs['ImageURL'] = PLACEHOLDER_IMAGE
    return recs

#HYBRID
def hybrid_recommendations(target_user_id, item_name, top_n=10):
    cb = content_based_recommendations(item_name, top_n)
    cf = collaborative_recommendations(target_user_id, top_n)
    if cb.empty and cf.empty:
        return pd.DataFrame()
    elif cb.empty:
        return cf
    elif cf.empty:
        return cb
    combined = cb.copy()
    for _, row in cf.iterrows():
        if row['Name'] not in combined['Name'].values:
            combined = pd.concat([combined, row.to_frame().T], ignore_index=True)
        if len(combined) >= top_n:
            break
    combined['ImageURL'] = PLACEHOLDER_IMAGE
    return combined.head(top_n)

@app.route("/")
def index():
    if products.empty:
        return "No trending products found."
    trending = products.head(8).copy()
    image_urls = [PLACEHOLDER_IMAGE] * len(trending)
    random_price = random.randint(30, 150)
    return render_template('index.html',
                           trending_products=trending,
                           truncate=truncate,
                           random_product_image_urls=image_urls,
                           random_price=random_price)

@app.route("/main")
def main():
    return render_template('main.html',
                           content_based_rec=pd.DataFrame(),
                           message="Enter a product name to get recommendations")

@app.route("/recommendations", methods=['POST'])
def recommendations():
    prod = request.form.get('prod', '')
    nbr_str = request.form.get('nbr', '10')
    try:
        top_n = int(nbr_str)
    except ValueError:
        top_n = 10
    if not prod.strip():
        return render_template('main.html', message="Please enter a product name.", content_based_rec=pd.DataFrame())
    recs = content_based_recommendations(prod, top_n=top_n)
    if recs.empty:
        message = "No recommendations found. Try a different product name or check spelling."
        return render_template('main.html', message=message, content_based_rec=pd.DataFrame())
    else:
        return render_template('main.html', content_based_rec=recs, truncate=truncate, message="")

if __name__ == '__main__':
    app.run(debug=True)