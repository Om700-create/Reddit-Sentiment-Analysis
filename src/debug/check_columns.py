import pandas as pd

df = pd.read_csv("data/processed/reddit_nlp_ready.csv")
print("✅ Data loaded successfully!")
print("\n📌 Available Columns:\n", df.columns)
print("\n🔹 First few rows:\n", df.head())
