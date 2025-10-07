# pipeline/dashboard.py
import os
import sys
import subprocess
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(FILE_DIR, os.pardir))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

try:
    from pipeline.anomaly_detector import detect_sentiment_anomalies
except ModuleNotFoundError:
    from anomaly_detector import detect_sentiment_anomalies
    
st.set_page_config(page_title="ReviewSentinel Dashboard", layout="wide")
st.title("📊 AI-Powered Moderation & Sentiment Intelligence System")

# ----- Robust path handling -----
# this file is .../pipeline/dashboard.py  -> repo root = parent of 'pipeline'
REPO_ROOT = os.path.dirname(os.path.dirname(__file__))
processed_csv = os.path.join(REPO_ROOT, "data", "processed_reviews.csv")
raw_csv = os.path.join(REPO_ROOT, "data", "user_reviews.csv")
app_runner = os.path.join(REPO_ROOT, "app.py")

# ----- Ensure processed data exists -----
if not os.path.exists(processed_csv):
    st.warning("Processed dataset not found (`data/processed_reviews.csv`).")
    col1, col2 = st.columns([1, 4])
    with col1:
        generate = st.button("Generate processed data")
    with col2:
        st.caption("This runs `python app.py` to preprocess raw reviews and create `processed_reviews.csv`.")
    if generate:
        with st.spinner("Running pipeline..."):
            result = subprocess.run(
                [sys.executable, app_runner],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True
            )
        st.code(result.stdout or "", language="bash")
        if result.stderr:
            st.error(result.stderr)
        if os.path.exists(processed_csv):
            st.success("✅ Processed dataset created. Click **Rerun**.")
        st.stop()
    else:
        st.stop()

# ----- Load processed data -----
df = pd.read_csv(processed_csv)
st.success(f"Loaded {len(df):,} processed reviews")
st.dataframe(df.head(), use_container_width=True)

# ----- Anomaly detection -----
anomaly_df = detect_sentiment_anomalies(df)

st.subheader("📅 Sentiment Over Time with Anomalies")
fig, ax = plt.subplots(figsize=(10, 4))
sns.lineplot(data=anomaly_df, x="ds", y="y", label="Actual", ax=ax)
sns.lineplot(data=anomaly_df, x="ds", y="yhat", label="Forecast", ax=ax)

anomaly_points = anomaly_df[anomaly_df["anomaly"] == True]
ax.scatter(anomaly_points["ds"], anomaly_points["y"], label="Anomalies")

ax.set_xlabel("")
ax.set_ylabel("Sentiment")
ax.tick_params(axis="x", rotation=45)
ax.legend()
st.pyplot(fig)

st.subheader("🚨 Violating Reviews")
violations = df[df.get("violation_flag", False) == True]
st.dataframe(violations[["timestamp", "review", "sentiment_score"]].head(50), use_container_width=True)
