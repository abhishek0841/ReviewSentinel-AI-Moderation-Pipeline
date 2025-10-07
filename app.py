# run_pipeline.py
import pandas as pd
from pipeline.text_cleaning import preprocess_reviews
from pipeline.violation_detector import detect_violations
from pipeline.sentiment_analyzer import analyze_sentiment

def main():
    df = pd.read_csv("data/user_reviews.csv")
    print("Loaded raw reviews")

    df = preprocess_reviews(df)
    print("Cleaned text")

    df = detect_violations(df)
    print("Detected violations")

    df = analyze_sentiment(df)
    print("Analyzed sentiment")

    df.to_csv("data/processed_reviews.csv", index=False)
    print("Saved processed reviews to data/processed_reviews.csv")

if __name__ == "__main__":
    main()
