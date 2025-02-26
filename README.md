# Reddit Sentiment Analysis

## Overview
This project analyzes sentiment trends on Reddit, using **NLP techniques** and **machine learning models** to classify user comments into positive, negative, and neutral sentiments. The goal is to extract meaningful insights about online discussions, trends, and user emotions.

## Features
- **Scrapes Reddit data** using PRAW
- **Performs NLP preprocessing** (tokenization, stopword removal, lemmatization)
- **Sentiment classification** using advanced models
- **Data visualization** to showcase trends
- **Evaluation metrics** for model performance

## Installation
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

## Results
### 1️⃣ Confusion Matrix
![Confusion Matrix](https://github.com/Om700-create/Reddit-Sentiment-Analysis/blob/70d5f561726a9e00e7b69ee6564587fb11e7f75f/reports/figures/confusion_matrix.png)
**Observation:** The confusion matrix reveals that the model performs well on positive and negative sentiments but shows some misclassification between neutral and other classes.

### 2️⃣ Enhanced Word Cloud
![Enhanced Word Cloud](https://github.com/Om700-create/Reddit-Sentiment-Analysis/blob/70d5f561726a9e00e7b69ee6564587fb11e7f75f/reports/figures/enhanced_word_cloud.png)
**Observation:** Commonly used words in Reddit comments reflect trends and dominant themes. Negative words indicate frustration, while positive words highlight appreciation and enthusiasm.

### 3️⃣ Sentiment Distribution
![Sentiment Distribution](https://github.com/Om700-create/Reddit-Sentiment-Analysis/blob/70d5f561726a9e00e7b69ee6564587fb11e7f75f/reports/figures/sentiment_distribution.png)
**Observation:** The majority of comments are neutral, but a significant portion expresses either positive or negative sentiments, reflecting balanced discussions.

### 4️⃣ Sentiment Scores
![Sentiment Scores](https://github.com/Om700-create/Reddit-Sentiment-Analysis/blob/70d5f561726a9e00e7b69ee6564587fb11e7f75f/reports/figures/sentiment_scores.png)
**Observation:** The sentiment score distribution suggests that extreme sentiments (very positive or very negative) are less frequent, while most comments have moderate scores.

### 5️⃣ Time-Series Sentiment Analysis
![Time Series Sentiment](https://github.com/Om700-create/Reddit-Sentiment-Analysis/blob/70d5f561726a9e00e7b69ee6564587fb11e7f75f/reports/figures/time_series_sentiment.png)
**Observation:** Sentiment fluctuates over time, showing spikes in negative sentiment during controversial discussions and an increase in positive sentiment during community events.

## How It Works
1. **Data Collection**: Extracts comments from subreddits.
2. **Preprocessing**: Cleans and tokenizes text.
3. **Feature Engineering**: Converts text into numerical representations.
4. **Model Training**: Uses machine learning classifiers.
5. **Evaluation & Visualization**: Displays results through graphs and metrics.

## Future Improvements
- **Improve sentiment model** using transformer-based architectures (BERT, RoBERTa).
- **Expand dataset** for a more robust analysis.
- **Deploy as an interactive tool** using Streamlit or Flask.

## Contributing
Pull requests are welcome! Open an issue for suggestions.

## License
This project is licensed under the MIT License.

---
💡 **Follow for updates & insights on AI-driven analytics!** 🚀


**🚀 Elevate Your NLP Projects to the Next Level!**

