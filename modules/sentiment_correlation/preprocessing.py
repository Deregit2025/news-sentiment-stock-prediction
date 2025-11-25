import pandas as pd
from textblob import TextBlob

# =====================
# NEWS DATA PREPROCESSING
# =====================

def preprocess_news_data(news_df):
    """
    Cleans and prepares news data:
    - Converts 'date' to datetime format
    - Strips and lowercases headlines
    - Handles missing values
    - Computes sentiment polarity
    """
    # 1️⃣ Handle missing values
    news_df = news_df.dropna(subset=['headline', 'date'])  # drop rows where headline/date is missing
    
    # 2️⃣ Convert 'date' to datetime and normalize timezone
    news_df['date'] = pd.to_datetime(news_df['date'], utc=True, errors='coerce')
    news_df = news_df.dropna(subset=['date'])  # remove failed conversions
    
    # 3️⃣ Clean headline
    news_df['headline'] = news_df['headline'].astype(str).str.strip().str.lower()
    
    # 4️⃣ Compute sentiment polarity
    news_df['polarity'] = news_df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    
    return news_df


# =====================
# STOCK DATA PREPROCESSING
# =====================

def preprocess_stock_data(stock_df):
    """
    Preprocess stock data:
    - Convert 'Date' column to datetime
    - Sort by date
    - Calculate Daily Return (% change of Close price)
    """
    stock_df['Date'] = pd.to_datetime(stock_df['Date'], utc=True, errors='coerce')
    stock_df = stock_df.dropna(subset=['Date'])
    
    stock_df = stock_df.sort_values(by='Date')  # ensure chronological order
    
    # 5️⃣ Compute % change / daily return
    stock_df['Daily_Return'] = stock_df['Close'].pct_change() * 100  # percentage change
    
    return stock_df
