
# 🛡️ Trust & Safety Review Monitoring Pipeline

A data engineering project simulating how platforms like Google Play or YouTube could monitor user reviews for:

- 🚨 Policy violations (hate speech, spam, personal info leaks)
- 📉 Sentiment anomalies (sudden drops/spikes in user feedback)
- ⚠️ Potential abuse/fraud (patterned behavior by users)

This project is **end-to-end**: ingestion → transformation → modeling → dashboard.

---

## 📁 Folder Structure

```
trust_safety_review_pipeline/
├── data/
│   ├── user_reviews.csv # Raw synthetic reviews
│   └── processed_reviews.csv # Cleaned + enriched dataset
├── pipeline/
│   ├── data_ingestion.py # Generates synthetic reviews
│   ├── text_cleaning.py # Preprocesses review text
│   ├── violation_detector.py # Flags policy-violating reviews
│   ├── sentiment_analyzer.py # Adds sentiment score using TextBlob
│   ├── anomaly_detector.py # Detects time-series sentiment anomalies (Prophet)
│   └── dashboard.py # Interactive Streamlit UI
├── run_pipeline.py # End-to-end script to generate processed reviews
└── requirements.txt # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone & Activate

```bash
git clone https://github.com/YOUR_USERNAME/trust_safety_review_pipeline.git
cd trust_safety_review_pipeline
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

If you are using GitHub Codespaces, this should install automatically.

---

## 🚀 Usage

### 1. Generate and Process Reviews

```bash
python run_pipeline.py
```

This will:

- Generate fake reviews
- Clean and tokenize them
- Flag policy violations
- Score sentiment
- Save the final result to `data/processed_reviews.csv`

### 2. Run the Dashboard

```bash
streamlit run pipeline/dashboard.py
```

You’ll see:

- 📈 Sentiment trends with Prophet forecast + red anomaly points
- 🚨 Table of policy-violating reviews

---

## 🔍 Example Output

| timestamp   | review                                | sentiment_score | violation_flag |
|--------------|--------------------------------------|-----------------|----------------|
| 2023-08-01  | this app is a scam and garbage        | -0.8           | ✅            |
| 2023-08-02  | really love it, but they stole my data | 0.2            | ✅            |

---

## 📦 Tech Stack
- **Python**: Core language
- **Pandas, NumPy**: Data wrangling
- **TextBlob**: Sentiment analysis
- **Facebook Prophet**: Time-series forecasting
- **Streamlit**: UI for results
- **Faker**: Synthetic data generation
- **Seaborn/Matplotlib**: Visualizations

---

## 💡 Real-World Relevance
This project simulates real challenges in Trust & Safety teams at companies like Google, YouTube, or Play Store, focusing on:

- Review moderation
- Fraud/spam detection
- Policy enforcement
- Platform health analytics
