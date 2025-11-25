# sentiment_analysis.py
import pandas as pd
from textblob import TextBlob

# -----------------------------
# Clean News Headlines
# -----------------------------
def clean_headlines(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the 'headline' column: convert to string and strip whitespace.
    Args:
        df (pd.DataFrame): News DataFrame
    Returns:
        pd.DataFrame: cleaned DataFrame
    """
    df['headline'] = df['headline'].astype(str).str.strip()
    return df

# -----------------------------
# Compute Sentiment
# -----------------------------
def compute_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute polarity using TextBlob and assign sentiment labels.
    Args:
        df (pd.DataFrame): News DataFrame with 'headline' column
    Returns:
        pd.DataFrame: DataFrame with 'polarity' and 'sentiment_label'
    """
    # Polarity: -1 to 1
    df['polarity'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    
    # Assign sentiment labels based on thresholds
    def get_label(p):
        if p > 0.05:
            return 'positive'
        elif p < -0.05:
            return 'negative'
        else:
            return 'neutral'
    
    df['sentiment_label'] = df['polarity'].apply(get_label)
    return df

# -----------------------------
# Aggregate Daily Sentiment
# -----------------------------
def aggregate_daily_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate multiple headlines per day per stock into average daily sentiment.
    Args:
        df (pd.DataFrame): News DataFrame with 'date', 'stock', 'polarity'
    Returns:
        pd.DataFrame: aggregated daily sentiment per stock
    """
    daily_sentiment = (
        df.groupby(['date', 'stock'])
        .agg(avg_daily_sentiment=('polarity', 'mean'))
        .reset_index()
    )
    return daily_sentiment

# -----------------------------
# Compute Stock Daily Returns
# -----------------------------
def compute_daily_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute daily percentage change in stock closing price.
    Args:
        df (pd.DataFrame): Stock DataFrame with 'Date' and 'Close'
    Returns:
        pd.DataFrame: Stock DataFrame with 'Daily_Return'
    """
    df = df.sort_values('Date')
    df['Daily_Return'] = df['Close'].pct_change()
    df = df.dropna(subset=['Daily_Return'])
    return df

# -----------------------------
# Full News Preprocessing
# -----------------------------
def preprocess_news_data(news_df: pd.DataFrame) -> pd.DataFrame:
    """
    Full preprocessing for news: clean headlines, compute sentiment, aggregate daily.
    """
    news_df = clean_headlines(news_df)
    news_df = compute_sentiment(news_df)
    news_daily = aggregate_daily_sentiment(news_df)
    return news_daily

# -----------------------------
# Full Stock Preprocessing
# -----------------------------
def preprocess_stock_data(stock_df: pd.DataFrame) -> pd.DataFrame:
    """
    Full preprocessing for stock: compute daily returns.
    """
    stock_df = compute_daily_returns(stock_df)
    return stock_df
