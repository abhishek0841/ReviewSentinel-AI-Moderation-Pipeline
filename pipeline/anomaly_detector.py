# pipeline/anomaly_detector.py
import pandas as pd
from prophet import Prophet

def prepare_sentiment_timeseries(df: pd.DataFrame) -> pd.DataFrame:
    sentiment_df = df.groupby("timestamp")["sentiment_score"].mean().reset_index()
    sentiment_df.columns = ["ds", "y"]
    sentiment_df["ds"] = pd.to_datetime(sentiment_df["ds"])  # Ensure datetime type
    return sentiment_df

def detect_sentiment_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    ts_df = prepare_sentiment_timeseries(df)

    model = Prophet(daily_seasonality=True)
    model.fit(ts_df)

    future = model.make_future_dataframe(periods=3)
    forecast = model.predict(future)

    result = pd.merge(ts_df, forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]], on="ds", how="left")
    result["anomaly"] = result.apply(
        lambda row: abs(row["y"] - row["yhat"]) > 0.2, axis=1
    )

    return result
