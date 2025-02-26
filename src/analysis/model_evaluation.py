import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the dataset with predictions
file_path = "data/processed/reddit_sentiment_with_predictions.csv"
df = pd.read_csv(file_path)

print(f"✅ Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"📌 Columns in dataset: {df.columns}")

# Check if required columns exist
required_columns = ["sentiment_label", "predicted_sentiment"]
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    print(f"❌ Error: Missing columns {missing_columns} in dataset!")
    print("🔍 Please generate predictions before running evaluation.")
    exit()

# Define sentiment mapping
sentiment_mapping = {"Negative": 0, "Neutral": 1, "Positive": 2}

df["sentiment_numeric"] = df["sentiment_label"].map(sentiment_mapping)
df["predicted_numeric"] = df["predicted_sentiment"].map(sentiment_mapping)

# Check for NaN values after mapping
if df[["sentiment_numeric", "predicted_numeric"]].isnull().sum().sum() > 0:
    print("❌ Error: Sentiment mapping failed due to unexpected labels!")
    print("🔍 Check if sentiment_label and predicted_sentiment have only expected values.")
    exit()

# Generate classification report
report = classification_report(df["sentiment_numeric"], df["predicted_numeric"], target_names=sentiment_mapping.keys())
print("\n📊 Classification Report:\n")
print(report)

# Generate confusion matrix
conf_matrix = confusion_matrix(df["sentiment_numeric"], df["predicted_numeric"])
plt.figure(figsize=(6, 5))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=sentiment_mapping.keys(), yticklabels=sentiment_mapping.keys())
plt.xlabel("Predicted Sentiment")
plt.ylabel("Actual Sentiment")
plt.title("Confusion Matrix")

# Save confusion matrix
output_dir = "reports/figures"
os.makedirs(output_dir, exist_ok=True)
conf_matrix_path = os.path.join(output_dir, "confusion_matrix.png")
plt.savefig(conf_matrix_path, bbox_inches="tight")
print(f"✅ Confusion matrix saved at: {conf_matrix_path}")

plt.show()
