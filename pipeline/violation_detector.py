# pipeline/violation_detector.py
import pandas as pd

VIOLATION_KEYWORDS = [
    "scam", "stole my data", "terrible", "hate", "fraud", "abuse", "pii", "fake"
]

def detect_violations(df: pd.DataFrame) -> pd.DataFrame:
    def check_violation(text):
        for keyword in VIOLATION_KEYWORDS:
            if keyword in text:
                return True
        return False

    df['violation_flag'] = df['cleaned_review'].apply(check_violation)
    return df
