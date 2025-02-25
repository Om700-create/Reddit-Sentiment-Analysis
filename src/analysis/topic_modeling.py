import pandas as pd
import gensim
from gensim import corpora
import pyLDAvis.gensim_models
import pyLDAvis
import streamlit as st

# Load the dataset
df = pd.read_csv("data/processed/reddit_sentiment.csv")

# Preprocessing: Tokenization & Stopwords Removal
df['tokens'] = df['title'].astype(str).str.lower().str.split()

# Create a dictionary and corpus for LDA
dictionary = corpora.Dictionary(df['tokens'])
corpus = [dictionary.doc2bow(text) for text in df['tokens']]

# Train the LDA Model
lda_model = gensim.models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)

# Visualize topics
vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
pyLDAvis.save_html(vis, "reports/figures/topic_modeling.html")

print("✅ Topic modeling completed! Check 'reports/figures/topic_modeling.html'")
