import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from collections import Counter

class WordCloudGenerator:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.df = None
    
    def load_data(self):
        self.df = pd.read_csv(self.input_path)
        print(f'✅ Data loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns')
    
    def generate_word_cloud(self):
        stopwords = set(STOPWORDS)
        additional_stopwords = {"like", "just", "know", "think", "good", "really"}  # Add more if needed
        stopwords.update(additional_stopwords)
        
        text = " ".join(self.df['processed_selftext'].dropna())
        word_freq = Counter(text.split())
        filtered_text = " ".join([word for word in text.split() if word_freq[word] > 2 and word not in stopwords])
        
        wordcloud = WordCloud(
            width=1200, height=600,
            background_color="white",
            colormap="coolwarm",
            stopwords=stopwords,
            max_words=200,
            contour_color='steelblue',
            contour_width=2
        ).generate(filtered_text)
        
        plt.figure(figsize=(12, 6))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title("🔊 Most Common Words in Reddit Posts", fontsize=16, fontweight='bold')
        plt.savefig(self.output_path, dpi=300)
        plt.show()
        print(f'✅ Word cloud saved at: {self.output_path}')
    
    def run(self):
        self.load_data()
        self.generate_word_cloud()

if __name__ == "__main__":
    input_path = "data/processed/reddit_nlp_ready.csv"
    output_path = "reports/figures/enhanced_word_cloud.png"
    wc = WordCloudGenerator(input_path, output_path)
    wc.run()
