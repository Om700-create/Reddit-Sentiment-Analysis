import pandas as pd
import os

class TimeSeriesSentiment:
    def __init__(self, input_csv="data/processed/reddit_sentiment.csv", output_csv="data/processed/reddit_time_series.csv"):
        self.input_csv = input_csv
        self.output_csv = output_csv
        self.df = None

    def load_data(self):
        """Load sentiment data."""
        if not os.path.exists(self.input_csv):
            raise FileNotFoundError(f"Sentiment data file '{self.input_csv}' not found.")

        self.df = pd.read_csv(self.input_csv)
        print(f"✅ Data loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns")

    def process_time_series(self):
        """Convert timestamp to date and aggregate sentiment scores."""
        try:
            # Try converting if it's a Unix timestamp
            self.df['date'] = pd.to_datetime(self.df['created_utc'], unit='s').dt.date
        except Exception:
            # If it fails, assume it's already in a readable datetime format
            self.df['date'] = pd.to_datetime(self.df['created_utc']).dt.date

        daily_sentiment = self.df.groupby('date')['sentiment_score'].mean().reset_index()

        os.makedirs(os.path.dirname(self.output_csv), exist_ok=True)
        daily_sentiment.to_csv(self.output_csv, index=False)

        print(f"✅ Time-series sentiment data saved at: {self.output_csv}")

    def run(self):
        """Execute time-series processing."""
        self.load_data()
        self.process_time_series()

# Run time-series sentiment analysis
if __name__ == "__main__":
    time_series = TimeSeriesSentiment()
    time_series.run()

