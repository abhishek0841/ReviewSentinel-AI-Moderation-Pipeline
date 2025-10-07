# pipeline/dashboard.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from anomaly_detector import detect_sentiment_anomalies

st.title("📊 Trust & Safety Review Dashboard")

df = pd.read_csv("data/processed_reviews.csv")
anomaly_df = detect_sentiment_anomalies(df)

st.subheader("📅 Sentiment Over Time with Anomalies")

fig, ax = plt.subplots(figsize=(10, 4))
sns.lineplot(data=anomaly_df, x="ds", y="y", label="Actual", ax=ax)
sns.lineplot(data=anomaly_df, x="ds", y="yhat", label="Forecast", ax=ax)
anomaly_points = anomaly_df[anomaly_df["anomaly"] == True]
plt.scatter(anomaly_points["ds"], anomaly_points["y"], color="red", label="Anomalies")
plt.xticks(rotation=45)
plt.legend()
st.pyplot(fig)

st.subheader("🚨 Violating Reviews")

violations = df[df["violation_flag"] == True]
st.write(violations[["timestamp", "review", "sentiment_score"]].head(20))
