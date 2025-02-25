import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import os

# Download VADER if not already present
nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self, input_csv="data/processed/reddit_nlp_ready.csv", output_csv="data/processed/reddit_sentiment.csv"):
        self.input_csv = input_csv
        self.output_csv = output_csv
        self.df = None
        self.analyzer = SentimentIntensityAnalyzer()

    def load_data(self):
        """Load the NLP-preprocessed data."""
        if not os.path.exists(self.input_csv):
            raise FileNotFoundError(f"Processed data file '{self.input_csv}' not found.")
        
        self.df = pd.read_csv(self.input_csv)
        print(f"✅ Data loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns")

    def analyze_sentiment(self, text):
        """Analyze sentiment using VADER and return compound score."""
        sentiment = self.analyzer.polarity_scores(text)
        return sentiment['compound']

    def apply_sentiment_analysis(self):
        """Apply sentiment analysis on preprocessed text columns."""
        self.df['sentiment_score'] = self.df['processed_title'].apply(self.analyze_sentiment)
        
        # Categorize sentiment into Positive, Negative, and Neutral
        self.df['sentiment_label'] = self.df['sentiment_score'].apply(lambda score: 
            'Positive' if score > 0.05 else 'Negative' if score < -0.05 else 'Neutral'
        )
        
        print("✅ Sentiment analysis complete")

    def save_results(self):
        """Save the sentiment analysis results."""
        os.makedirs(os.path.dirname(self.output_csv), exist_ok=True)
        self.df.to_csv(self.output_csv, index=False)
        print(f"✅ Sentiment data saved at: {self.output_csv}")

    def run_analysis(self):
        """Execute the full sentiment analysis pipeline."""
        self.load_data()
        self.apply_sentiment_analysis()
        self.save_results()

# Run sentiment analysis
if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    analyzer.run_analysis()
