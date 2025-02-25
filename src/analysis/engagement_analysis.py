import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Create directories if they don't exist
os.makedirs("reports/data", exist_ok=True)
os.makedirs("reports/figures", exist_ok=True)

# Load the processed Reddit sentiment data
df = pd.read_csv("data/processed/reddit_sentiment.csv")

# Ensure numerical columns are of the correct type
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce")

# 🔥 Top 10 Most Upvoted Posts
top_upvoted_posts = df.nlargest(10, "score")[["title", "subreddit", "score", "num_comments", "sentiment_label"]]

# 📈 Relationship Between Upvotes & Comments
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="score", y="num_comments", hue="sentiment_label", palette="coolwarm", alpha=0.6)
plt.xlabel("Upvotes (Score)")
plt.ylabel("Number of Comments")
plt.title("💬 Upvotes vs. Comments Relationship")
plt.legend(title="Sentiment")
plt.savefig("reports/figures/upvotes_vs_comments.png", bbox_inches="tight")
plt.close()

# 🏆 Top Subreddits by Engagement (Score & Comments)
top_subreddits = df.groupby("subreddit")[["score", "num_comments"]].mean().reset_index()
top_subreddits = top_subreddits.sort_values(by="score", ascending=False).head(15)

fig = px.bar(
    top_subreddits,
    x="subreddit",
    y="score",
    title="🏆 Top 15 Subreddits by Engagement",
    color="score",
    color_continuous_scale="viridis"
)
fig.write_html("reports/figures/top_subreddits_engagement.html")

# 🔢 Compute Engagement Score (Upvote-to-Comment Ratio)
df["engagement_score"] = df["score"] / (df["num_comments"] + 1)  # Avoid division by zero

# 🚀 Top 10 Highly Engaging Posts
top_engaging_posts = df.nlargest(10, "engagement_score")[["title", "subreddit", "score", "num_comments", "engagement_score"]]

# ✅ Save results
top_upvoted_posts.to_csv("reports/data/top_upvoted_posts.csv", index=False)
top_engaging_posts.to_csv("reports/data/top_engaging_posts.csv", index=False)

print("✅ Engagement analysis completed! Check 'reports/figures/' for visualizations.")

