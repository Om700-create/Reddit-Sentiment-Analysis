import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime

# Set page config (Must be the first Streamlit command)
st.set_page_config(page_title="Reddit Sentiment Dashboard", layout="wide")

# Load Data with Caching
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/reddit_sentiment_with_predictions.csv")
    df["created_utc"] = pd.to_datetime(df["created_utc"], errors='coerce')
    return df.dropna(subset=["created_utc"])  # Remove invalid date rows

df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filter Data")
author_filter = st.sidebar.multiselect("Select Authors", df["author"].unique())
min_score, max_score = st.sidebar.slider("Select Score Range", int(df["score"].min()), int(df["score"].max()), (int(df["score"].min()), int(df["score"].max())))
date_range = st.sidebar.date_input("Select Date Range", [df["created_utc"].min().date(), df["created_utc"].max().date()])

# Apply Filters
filtered_df = df[(df["score"] >= min_score) & (df["score"] <= max_score) & (df["created_utc"].dt.date.between(date_range[0], date_range[1]))]
if author_filter:
    filtered_df = filtered_df[filtered_df["author"].isin(author_filter)]

# Streamlit Tabs for Organization
tab1, tab2, tab3 = st.tabs(["📊 Sentiment Overview", "📈 Time-Series Trends", "☁️ Word Cloud"])

# Tab 1: Sentiment Overview
with tab1:
    st.header("📊 Sentiment Distribution")
    fig, ax = plt.subplots()
    sns.countplot(data=filtered_df, x="predicted_sentiment", palette="coolwarm", order=["Positive", "Neutral", "Negative"], ax=ax)
    st.pyplot(fig)
    
    # Top Authors by Engagement
    st.subheader("🔥 Top Authors by Engagement")
    filtered_df["engagement"] = filtered_df["score"] + filtered_df["num_comments"]
    top_authors = filtered_df.groupby("author")["engagement"].sum().nlargest(10)
    fig, ax = plt.subplots()
    sns.barplot(data=top_authors.reset_index(), x="engagement", y="author", palette="coolwarm", ax=ax)
    st.pyplot(fig)

# Tab 2: Time-Series Trends
with tab2:
    st.header("📈 Sentiment Trends Over Time")
    df_time = filtered_df.groupby([filtered_df["created_utc"].dt.date, "predicted_sentiment"]).size().unstack().fillna(0)
    st.line_chart(df_time)

# Tab 3: Word Cloud
with tab3:
    st.header("☁️ Word Cloud of Most Used Words")
    sentiment_choice = st.selectbox("Select Sentiment", ["Positive", "Neutral", "Negative"])
    text = " ".join(filtered_df[filtered_df["predicted_sentiment"] == sentiment_choice]["processed_selftext"].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

# Deployment Tips
st.sidebar.markdown("## 🚀 Deployment Tips")
st.sidebar.markdown("- Deploy on Streamlit Cloud for free")
st.sidebar.markdown("- Use Heroku, AWS, or Render for better performance")





