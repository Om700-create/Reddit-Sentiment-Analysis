import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit page config
st.set_page_config(page_title="Reddit Sentiment Dashboard", layout="wide")

# Load Data
@st.cache_data
def load_data():
    df_sentiment = pd.read_csv("data/processed/reddit_sentiment.csv")
    top_upvoted = pd.read_csv("reports/data/top_upvoted_posts.csv")
    top_engaging = pd.read_csv("reports/data/top_engaging_posts.csv")
    return df_sentiment, top_upvoted, top_engaging

df, top_upvoted, top_engaging = load_data()

# Dashboard Title
st.title("📊 Reddit Sentiment Analysis Dashboard")

# Sidebar Filters
st.sidebar.header("🔍 Filter Options")
selected_subreddit = st.sidebar.selectbox("Select Subreddit", ["All"] + sorted(df["subreddit"].unique()))

# Apply filter
if selected_subreddit != "All":
    df = df[df["subreddit"] == selected_subreddit]

# Top Upvoted Posts
st.subheader("🔥 Top 10 Most Upvoted Posts")
st.dataframe(top_upvoted)

# Top Engaging Posts
st.subheader("🚀 Top 10 Highly Engaging Posts")
st.dataframe(top_engaging)

# Scatter Plot: Upvotes vs. Comments
st.subheader("💬 Upvotes vs. Comments Relationship")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=df, x="score", y="num_comments", hue="sentiment_label", palette="coolwarm", alpha=0.6)
plt.xlabel("Upvotes (Score)")
plt.ylabel("Number of Comments")
plt.title("Upvotes vs. Comments Relationship")
plt.legend(title="Sentiment")
st.pyplot(fig)

# Top Subreddits by Engagement
st.subheader("🏆 Top Subreddits by Engagement")

# Read and display the HTML visualization
with open("reports/figures/top_subreddits_engagement.html", "r", encoding="utf-8") as file:
    html_content = file.read()

st.components.v1.html(html_content, height=600, scrolling=True)

st.plotly_chart(fig)

st.write("✅ Data refreshed! Explore engagement insights 🔍")



