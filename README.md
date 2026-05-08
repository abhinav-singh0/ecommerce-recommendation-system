# 🛒 E-Commerce Product Recommendation System

An end-to-end **hybrid recommendation engine** that suggests products using both:

- **Content-Based Filtering** (TF-IDF + cosine similarity)
- **Collaborative Filtering** (user-based recommendations)

Built with Flask and deployed on Render.

---

## 🔗 Links

- **Live Demo:** https://e-commerce-product-recommendation-system-mhh0.onrender.com
- **GitHub Repo:** https://github.com/abhinav-singh0/ecommerce-recommendation-system

---

## 📌 Features

 **Rating‑based Trending Products** – home page shows trending items using Rating × log(1+ReviewCount).
- **Content‑Based Recommendations** – finds similar products using TF‑IDF on product names + brands.
- **Collaborative Filtering** – suggests products based on what similar users liked (synthetic user ratings).
- **Hybrid Recommendations** – combines both methods for better relevance.
- **Fuzzy Matching** – handles typos and partial product names.
- **User Authentication** – signup / signin (optional, can be disabled).
- **Responsive UI** – built with Bootstrap.
- **Deployed on Render** – always accessible via a live URL.
---

## 🧠 How It Works

### 1. Dataset

Amazon product catalog containing:
- Product names
- Brand names

Synthetic ratings and review counts are generated to support collaborative filtering.

---

### 2. Content-Based Filtering

- Product names and brands are combined into a `Tags` column
- TF-IDF vectorization is applied
- Cosine similarity identifies similar products
- Fuzzy matching improves search accuracy

---

### 3. Collaborative Filtering

- User-item interaction matrix is created
- User-user cosine similarity is computed
- Products liked by similar users are recommended

---

### 4. Hybrid Recommendation System

Final recommendations are generated using a weighted combination of:
- Content similarity score
- Collaborative filtering score

---

### 5. Web Application

- Flask backend serves recommendations
- HTML templates render UI
- Placeholder images prevent broken image links

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Backend | Flask (Python) |
| Machine Learning | scikit-learn |
| Data Handling | Pandas, NumPy |
| Fuzzy Matching | FuzzyWuzzy |
| Frontend | HTML, CSS, Bootstrap |
| Deployment | Render + Gunicorn |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
ECommerce-Project/
│
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── .gitignore
│
├── models/
│   ├── clean_data.csv
│   └── trending_products.csv
│
├── static/
│   ├── images/
│   │   └── placeholder.png
│   └── v.mp4
│
├── templates/
│   ├── index.html
│   └── main.html
│
└── README.md
```

---

## 🚀 Local Setup

### Prerequisites

- Python 3.11+
- Git

---

### 1. Clone Repository

```bash
git clone https://github.com/abhinav-singh0/ecommerce-recommendation-system.git

cd ecommerce-recommendation-system
```

---

### 2. Create Virtual Environment

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run Application

```bash
python app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

---

## 📊 Dataset

The original product data is based on an Amazon product dataset from Kaggle.

Synthetic:
- ratings
- review counts
- user interactions

were added to enable collaborative filtering.

---

## 🤝 Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss proposed modifications.

---

## 🙏 Acknowledgements

- Amazon product data from Kaggle
- Flask
- scikit-learn
- Open-source ML community

---

## 📧 Contact

**Abhinav Singh**  
IIT Dharwad  
📧 ee25mt010@iitdh.ac.in

Project Link:  
https://github.com/abhinav-singh0/ecommerce-recommendation-system
