import os
import praw
import pandas as pd
import nltk
from textblob import TextBlob
from dotenv import load_dotenv

# Load API credentials
load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def fetch_reddit_posts(subreddits=["technology", "datascience", "machinelearning"], limit=100):
    """Fetch latest Reddit posts from specified subreddits."""
    posts = []
    for subreddit in subreddits:
        for post in reddit.subreddit(subreddit).hot(limit=limit):
            posts.append({
                "id": post.id,
                "title": post.title,
                "subreddit": subreddit,
                "score": post.score,
                "num_comments": post.num_comments,
                "created_utc": post.created_utc
            })
    return pd.DataFrame(posts)

def analyze_sentiment(text):
    """Perform sentiment analysis on text."""
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def process_data(df):
    """Clean and process the Reddit data."""
    df["sentiment_score"] = df["title"].apply(analyze_sentiment)
    df["sentiment_label"] = df["sentiment_score"].apply(lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Neutral")
    df["date"] = pd.to_datetime(df["created_utc"], unit='s')
    return df

def save_data(df):
    """Save processed data to CSV."""
    df.to_csv("data/processed/reddit_sentiment.csv", index=False)
    time_series = df.groupby("date")["sentiment_score"].mean().reset_index()
    time_series.to_csv("data/processed/reddit_time_series.csv", index=False)
    print("✅ Data successfully saved!")

# Run pipeline
df = fetch_reddit_posts()
df = process_data(df)
save_data(df)
print("🚀 Reddit data pipeline completed!")
