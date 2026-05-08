# 🛒 E‑Commerce Product Recommendation System

An end‑to‑end **hybrid recommendation engine** that suggests products based on **content‑based filtering** (TF‑IDF + cosine similarity) and **collaborative filtering** (user‑based). Built with Flask, deployed on Render.

🔗 **Live Demo:** [https://ecommerce-recommendation.onrender.com](https://ecommerce-recommendation.onrender.com)  
📂 **GitHub Repo:** [your-repo-link]

---

## 📌 Features

- **Rating‑based Trending Products** – home page shows trending items using `Rating × log(1+ReviewCount)`.
- **Content‑Based Recommendations** – finds similar products using TF‑IDF on product names + brands.
- **Collaborative Filtering** – suggests products based on what similar users liked (synthetic user ratings).
- **Hybrid Recommendations** – combines both methods for better relevance.
- **Fuzzy Matching** – handles typos and partial product names.
- **User Authentication** – signup / signin (optional, can be disabled).
- **Responsive UI** – built with Bootstrap.
- **Deployed on Render** – always accessible via a live URL.

---

## 🧠 How It Works

1. **Data** – Amazon product catalog (name, brand, image path).  
   Synthetic user ratings (1‑5 stars) and review counts are generated to enable collaborative filtering.

2. **Content‑Based Model**  
   - Each product’s `Tags` field (name + brand) is vectorized using **TF‑IDF**.  
   - Cosine similarity measures text‑based similarity.  
   - Fuzzy matching finds the closest product name to the user’s query.

3. **Collaborative Filtering Model**  
   - A user‑item matrix is built from synthetic ratings.  
   - User‑user similarity is computed with cosine similarity.  
   - Top‑N products not yet rated by the active user are recommended.

4. **Hybrid Model**  
   - Combines scores from both models (weighted average).  
   - Provides more robust suggestions.

5. **Web Interface**  
   - Flask serves HTML templates.  
   - Products are displayed with placeholder images (no broken external links).  

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Backend | Flask (Python) |
| Machine Learning | scikit‑learn (TF‑IDF, cosine similarity) |
| Data Handling | Pandas, NumPy |
| Fuzzy Matching | FuzzyWuzzy |
| Frontend | HTML, CSS, Bootstrap |
| Deployment | Render (Gunicorn) |
| Version Control | Git, GitHub |

---

## 📂 Project Structure

ECommerce-Project/
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
├── models/
│ ├── clean_data.csv # User‑item ratings + product details
│ └── trending_products.csv # Unique product list
├── static/
│ ├── images/
│ │ └── placeholder.png # Placeholder image for all products
│ └── v.mp4 # Background video (optional)
├── templates/
│ ├── index.html # Home page (trending products)
│ └── main.html # Search & recommendations page
└── README.md # This file

---

## 🚀 Getting Started (Local Development)

### Prerequisites

- Python 3.8+
- Git

### 1. Clone the repository

```bash
git clone https://github.com/abhinav-singh0/ecommerce-recommendation-system.git
cd ecommerce-recommendation-system
2. Create and activate a virtual environment
macOS / Linux:

bash
python3 -m venv venv
source venv/bin/activate
Windows:

bash
python -m venv venv
venv\Scripts\activate
3. Install dependencies
bash
pip install -r requirements.txt

4. Run the app
bash
python app.py
Open http://127.0.0.1:5000 in your browser.
---

### 📊 Da
The original product data comes from an Amazon Brand Images & Product Index Kaggle dataset.
Synthetic user ratings and review counts were added to enable collaborative filtering.

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## 🙏 Acknowledgements
Amazon product data from Kaggle.

Flask, scikit‑learn, and the open‑source community.

Inspiration from classic recommendation system literature.

## 📧 Contact
Abhinav Singh – ee25mt010@iitdh.ac.in
Project Link: https://github.com/abhinav-singh0/ecommerce-recommendation-system

