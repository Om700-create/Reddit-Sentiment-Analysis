import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class SentimentVisualizer:
    def __init__(self, input_csv="data/processed/reddit_sentiment.csv", output_dir="reports/figures/"):
        self.input_csv = input_csv
        self.output_dir = output_dir
        self.df = None

    def load_data(self):
        """Load sentiment analysis results."""
        if not os.path.exists(self.input_csv):
            raise FileNotFoundError(f"Sentiment data file '{self.input_csv}' not found.")
        
        self.df = pd.read_csv(self.input_csv)
        print(f"✅ Data loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns")

    def plot_sentiment_distribution(self):
        """Plot a bar chart of sentiment label distribution."""
        plt.figure(figsize=(8, 5))
        sns.countplot(x=self.df['sentiment_label'], palette='coolwarm', order=['Positive', 'Neutral', 'Negative'])
        plt.title("Sentiment Distribution of Reddit Posts")
        plt.xlabel("Sentiment")
        plt.ylabel("Count")
        plt.xticks(rotation=0)
        
        # Save and show plot
        os.makedirs(self.output_dir, exist_ok=True)
        plt.savefig(os.path.join(self.output_dir, "sentiment_distribution.png"))
        print(f"✅ Sentiment distribution plot saved at: {self.output_dir}sentiment_distribution.png")
        plt.show()

    def plot_sentiment_scores(self):
        """Plot the sentiment scores distribution."""
        plt.figure(figsize=(8, 5))
        sns.histplot(self.df['sentiment_score'], bins=30, kde=True, color="blue")
        plt.title("Sentiment Score Distribution")
        plt.xlabel("Sentiment Score")
        plt.ylabel("Frequency")

        # Save and show plot
        plt.savefig(os.path.join(self.output_dir, "sentiment_scores.png"))
        print(f"✅ Sentiment score plot saved at: {self.output_dir}sentiment_scores.png")
        plt.show()

    def run_visualization(self):
        """Run all visualizations."""
        self.load_data()
        self.plot_sentiment_distribution()
        self.plot_sentiment_scores()

# Run sentiment visualization
if __name__ == "__main__":
    visualizer = SentimentVisualizer()
    visualizer.run_visualization()
