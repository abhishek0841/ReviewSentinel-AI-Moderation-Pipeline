# pipeline/text_cleaning.py
import pandas as pd
import re
import string

def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation and special characters
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess_reviews(df: pd.DataFrame) -> pd.DataFrame:
    df['cleaned_review'] = df['review'].apply(clean_text)
    return df
