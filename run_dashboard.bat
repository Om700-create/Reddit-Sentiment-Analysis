@echo off
cd C:\project\Reddit-Sentiment-Analysis
call reddit\Scripts\activate  # Activate virtual environment (if needed)
streamlit run src/app/dashboard.py
