import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class TimeSeriesVisualization:
    def __init__(self, input_csv="data/processed/reddit_time_series.csv", output_folder="reports/figures/"):
        self.input_csv = input_csv
        self.output_folder = output_folder
        self.df = None

    def load_data(self):
        """Load time-series sentiment data."""
        if not os.path.exists(self.input_csv):
            raise FileNotFoundError(f"Time-series data file '{self.input_csv}' not found.")

        self.df = pd.read_csv(self.input_csv)
        self.df['date'] = pd.to_datetime(self.df['date'])
        print(f"✅ Data loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns")

    def plot_sentiment_trend(self):
        """Plot sentiment score trend with moving average."""
        plt.figure(figsize=(12, 6))
        sns.set_style("whitegrid")

        # Plot actual sentiment score trend
        plt.plot(self.df['date'], self.df['sentiment_score'], marker='o', linestyle='-', label='Daily Sentiment Score', color='blue')

        # Calculate and plot 7-day moving average
        self.df['sentiment_moving_avg'] = self.df['sentiment_score'].rolling(window=7, min_periods=1).mean()
        plt.plot(self.df['date'], self.df['sentiment_moving_avg'], linestyle='--', label='7-Day Moving Average', color='red')

        plt.xlabel("Date")
        plt.ylabel("Average Sentiment Score")
        plt.title("📅 Sentiment Trend Over Time")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot
        os.makedirs(self.output_folder, exist_ok=True)
        plot_path = os.path.join(self.output_folder, "time_series_sentiment.png")
        plt.savefig(plot_path)
        print(f"✅ Sentiment trend plot saved at: {plot_path}")
        plt.show()

    def run(self):
        """Execute visualization."""
        self.load_data()
        self.plot_sentiment_trend()

# Run time-series visualization
if __name__ == "__main__":
    viz = TimeSeriesVisualization()
    viz.run()
