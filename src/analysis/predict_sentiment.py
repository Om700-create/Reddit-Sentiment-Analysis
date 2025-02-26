import pandas as pd
import os
from nltk.sentiment import SentimentIntensityAnalyzer

# Paths
DATA_PATH = "data/processed/reddit_sentiment.csv"
OUTPUT_PATH = "data/processed/reddit_sentiment_with_predictions.csv"

# Load Data
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Processed data not found at {DATA_PATH}. Run sentiment analysis first!")

df = pd.read_csv(DATA_PATH)
print(f"✅ Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# Check if required columns exist
required_columns = ["processed_title", "processed_selftext"]
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    raise ValueError(f"❌ Missing columns {missing_columns} in dataset! Ensure preprocessing was done correctly.")

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    if pd.isna(text) or text.strip() == "":
        return "Neutral"  # Default for empty text
    
    score = sia.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment prediction
df["predicted_sentiment"] = df["processed_title"].astype(str).apply(get_sentiment)

# Save the updated dataset
df.to_csv(OUTPUT_PATH, index=False)
print(f"✅ Predictions saved at: {OUTPUT_PATH}")
