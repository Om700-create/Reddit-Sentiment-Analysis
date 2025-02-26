# Reddit Sentiment Analysis

## Overview
The **Reddit Sentiment Analysis** project aims to analyze sentiment trends on Reddit using NLP techniques. It involves data extraction, preprocessing, sentiment analysis, and visualization of trends. The project provides insights into how users express opinions across different topics.

## Features
- **Sentiment Classification:** Categorizes posts as Positive, Negative, or Neutral.
- **Word Cloud Visualization:** Highlights the most frequent words in different sentiment categories.
- **Sentiment Score Distribution:** Shows the spread of sentiment scores.
- **Time-Series Sentiment Analysis:** Tracks sentiment changes over time.
- **Confusion Matrix:** Evaluates model performance.

## Visualizations & Observations
### 1️⃣ Confusion Matrix
![Confusion Matrix](./confusion_matrix.png)
- The confusion matrix provides an overview of model performance.
- It shows the number of correct and incorrect predictions across different sentiment categories.
- Higher diagonal values indicate better classification accuracy.

### 2️⃣ Enhanced Word Cloud
![Word Cloud](./enhanced_word_cloud.png)
- The word cloud highlights the most frequent words in Reddit comments.
- Positive words like "love" and "great" appear prominently.
- Negative sentiment words such as "bad" and "hate" are also visible, reflecting the emotional polarity.

### 3️⃣ Sentiment Distribution
![Sentiment Distribution](./sentiment_distribution.png)
- This visualization shows the proportion of Positive, Neutral, and Negative comments.
- A balanced distribution suggests diverse opinions, while skewed data may indicate bias.
- The chart helps in understanding the overall sentiment trend.

### 4️⃣ Sentiment Scores
![Sentiment Scores](./sentiment_scores.png)
- Displays sentiment scores on a scale, revealing intensity variations.
- Scores close to zero indicate neutral sentiments, while extremes denote strong positivity or negativity.
- This helps gauge the strength of user opinions.

### 5️⃣ Time-Series Sentiment Analysis
![Time Series Sentiment](./time_series_sentiment.png)
- Shows how sentiment trends evolve over time.
- Peaks and dips indicate significant events or discussions affecting sentiment.
- This analysis is useful for detecting shifts in user opinions.

## Technologies Used
- **Python**: Data processing and sentiment analysis
- **NLTK & VADER**: Sentiment classification
- **Matplotlib & Seaborn**: Data visualization
- **Pandas & NumPy**: Data manipulation
- **MySQL**: Data storage

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/reddit-sentiment-analysis.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the analysis script:
   ```bash
   python sentiment_analysis.py
   ```

## Future Enhancements
- Improve sentiment model accuracy with fine-tuning.
- Implement real-time sentiment tracking.
- Integrate with additional NLP models (e.g., BERT, GPT).
- Build an interactive dashboard for better visualization.

## Conclusion
This project provides valuable insights into Reddit discussions, helping to understand public sentiment trends effectively. The visualizations and analysis contribute to a deeper understanding of how different topics are perceived online.

🚀 **Feel free to contribute and enhance this project!**


**🚀 Elevate Your NLP Projects to the Next Level!**

