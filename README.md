

# Reddit Sentiment Analysis: Unlocking Consumer Insights with AI

## 📚 Overview
This project leverages **Natural Language Processing (NLP)** and **machine learning** to analyze sentiment trends on Reddit, a platform where millions of users discuss brands, products, and finance. By classifying Reddit comments into **positive, negative, and neutral sentiments**, businesses can track consumer perception, detect trends, and make data-driven decisions.

💡 **Why It Matters:**  
✅ **Marketers** can use this tool to measure customer reactions to products and campaigns.  
✅ **Financial analysts** can monitor public sentiment on stocks and investments.  
✅ **Consultants** can analyze industry trends and consumer emotions for business strategy.  

---

## ✨ Features & Capabilities  

🔹 **Reddit Data Scraping** – Automatically extracts Reddit comments using PRAW.  
🔹 **Advanced NLP Processing** – Cleans, tokenizes, and lemmatizes text for meaningful analysis.  
🔹 **Sentiment Classification** – Uses ML-based sentiment analysis to categorize text.  
🔹 **Trend & Sentiment Visualization** – Generates interactive graphs for business insights.  
🔹 **Performance Metrics** – Evaluates model accuracy with detailed analytics.  

---

## 📊 Business Use Cases  

### 📢 1️⃣ Brand Monitoring & Consumer Insights  
💡 **Problem:** Businesses struggle to measure how customers feel about their products.  
🚀 **Solution:** This project tracks sentiment trends and highlights major themes in discussions, helping companies understand customer satisfaction.  

🐹 **Example:** A company can monitor discussions in r/Apple to see how users feel about the latest iPhone update.  

---

### 📈 2️⃣ Financial Market Sentiment Tracking  
💡 **Problem:** Investors and traders need public sentiment data to predict stock movements.  
🚀 **Solution:** By analyzing Reddit finance communities (e.g., r/WallStreetBets), this tool can provide **early signals** for market trends.  

🐹 **Example:** If sentiment on a stock turns negative, investors might anticipate a drop before it happens.  

---

### 📊 3️⃣ Political & Social Trend Analysis  
💡 **Problem:** Policymakers and researchers need to track how public opinions change over time.  
🚀 **Solution:** Sentiment fluctuations can indicate shifts in public sentiment about policies or social issues.  

🐹 **Example:** Governments can analyze public response to policies by monitoring discussions in relevant subreddits.  

---

## 🛠️ Installation & Setup  
Clone the repository:  
```sh
git clone https://github.com/Om700-create/Reddit-Sentiment-Analysis.git
cd Reddit-Sentiment-Analysis
```  
Install dependencies:  
```sh
pip install -r requirements.txt
```  
Run sentiment analysis:  
```sh
python main.py
```  

---

## 📈 Key Results & Insights  

### 1️⃣ Sentiment Analysis Confusion Matrix  
📌 **Observation:** The model correctly classifies positive and negative sentiments but has some misclassifications for neutral tones.  

![Confusion Matrix](https://github.com/Om700-create/Reddit-Sentiment-Analysis/blob/main/reports/figures/confusion_matrix.png)  

---

### 2️⃣ Word Cloud of Top Discussion Topics  
📌 **Observation:** Negative sentiment clusters around complaints, while positive sentiment is associated with appreciation and enthusiasm.  

![Enhanced Word Cloud](https://github.com/Om700-create/Reddit-Sentiment-Analysis/blob/main/reports/figures/enhanced_word_cloud.png)  

---

### 3️⃣ Sentiment Trends Over Time  
📌 **Observation:** Negative sentiment spikes align with major controversies, while positive sentiment peaks occur during special events.  

![Time Series Sentiment](https://github.com/Om700-create/Reddit-Sentiment-Analysis/blob/main/reports/figures/time_series_sentiment.png)  

---

## 🔍 How It Works  
1️⃣ **Data Collection** – Scrapes Reddit posts & comments from relevant subreddits.  
2️⃣ **Text Preprocessing** – Cleans data using NLP techniques (lemmatization, tokenization).  
3️⃣ **Feature Engineering** – Converts text into numerical features for sentiment classification.  
4️⃣ **Model Training** – Uses machine learning to classify sentiment into positive, negative, and neutral.  
5️⃣ **Insights & Visualization** – Generates reports and trend graphs for actionable insights.  

---

## 🚀 Future Improvements  
To make this project even more **business-friendly and impactful**, the next steps include:  

🔹 **Upgrade Sentiment Model** – Implement **BERT/RoBERTa** for state-of-the-art sentiment classification.  
🔹 **Build an Interactive Dashboard** – Use **Streamlit or Power BI** for real-time sentiment tracking.  
🔹 **Expand Dataset Coverage** – Analyze **multiple industries & product categories** for deeper insights.  
🔹 **Deploy as an API/Web App** – Make the tool accessible for businesses via **Flask, FastAPI, or a web dashboard.**  

---

## 📢 Contributing  
Pull requests are welcome! Open an issue for discussions and suggestions.  

---

## 📝 License  
This project is licensed under the MIT License.  

💡 **Follow for more AI-driven business analytics insights! 🚀**  

