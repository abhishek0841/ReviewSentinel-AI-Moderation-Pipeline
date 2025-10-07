# pipeline/data_ingestion.py
import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

def generate_fake_reviews(num_reviews=1000):
    sample_reviews = [
        "This app is amazing!",
        "Worst experience ever. App keeps crashing.",
        "Customer service is terrible. Avoid this.",
        "I love it! Super easy to use.",
        "This is a scam. Took my money and didn’t work.",
        "Works fine, but lags sometimes.",
        "Very buggy. Deleted my files!",
        "App is decent. Could use some improvements.",
        "They stole my data. Don’t download this!",
        "Good UX. Recommended."
    ]

    violations_keywords = ["scam", "stole my data", "terrible", "hate", "fraud", "abuse", "PII", "fake"]

    reviews = []
    start_date = datetime.now() - timedelta(days=30)

    for _ in range(num_reviews):
        review_date = start_date + timedelta(days=random.randint(0, 29))
        text = random.choice(sample_reviews)
        user_id = fake.uuid4()
        rating = random.randint(1, 5)

        reviews.append({
            "user_id": user_id,
            "review": text,
            "rating": rating,
            "timestamp": review_date.strftime("%Y-%m-%d")
        })

    df = pd.DataFrame(reviews)
    return df

def save_reviews_csv(path="data/user_reviews.csv"):
    df = generate_fake_reviews()
    df.to_csv(path, index=False)
    print(f"[✓] Fake reviews saved to {path}")

if __name__ == "__main__":
    save_reviews_csv()
