# pipeline/sentiment_analyzer.py
from textblob import TextBlob
import pandas as pd

def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def analyze_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    df['sentiment_score'] = df['cleaned_review'].apply(get_sentiment)
    return df
