# correlation.py
import pandas as pd
from scipy.stats import pearsonr

# -----------------------------
# Merge News & Stock Data
# -----------------------------
def merge_news_stock(news_df: pd.DataFrame, stock_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merge daily aggregated news sentiment with stock daily returns by date and stock symbol.
    Args:
        news_df (pd.DataFrame): Aggregated daily sentiment ('date', 'stock', 'avg_daily_sentiment')
        stock_df (pd.DataFrame): Stock DataFrame with 'Date', 'Close', 'Daily_Return'
    Returns:
        pd.DataFrame: merged DataFrame
    """
    # Ensure consistent column names
    stock_df = stock_df.rename(columns={'Date': 'date'})
    
    merged_df = pd.merge(news_df, stock_df, on='date', how='inner')
    return merged_df

# -----------------------------
# Compute Pearson Correlation
# -----------------------------
def compute_correlation(merged_df: pd.DataFrame) -> float:
    """
    Compute Pearson correlation between daily sentiment and stock daily returns.
    Args:
        merged_df (pd.DataFrame): DataFrame with 'avg_daily_sentiment' and 'Daily_Return'
    Returns:
        float: correlation coefficient
    """
    corr, _ = pearsonr(merged_df['avg_daily_sentiment'], merged_df['Daily_Return'])
    return corr

# -----------------------------
# Compute Lagged Correlation
# -----------------------------
def compute_lag_correlation(merged_df: pd.DataFrame, lag_days: int = 1) -> float:
    """
    Compute correlation between sentiment and stock returns with a lag.
    Args:
        merged_df (pd.DataFrame): merged DataFrame
        lag_days (int): number of days to shift sentiment
    Returns:
        float: lagged correlation coefficient
    """
    merged_df = merged_df.copy()
    merged_df['lagged_sentiment'] = merged_df['avg_daily_sentiment'].shift(lag_days)
    merged_df = merged_df.dropna(subset=['lagged_sentiment', 'Daily_Return'])
    
    corr, _ = pearsonr(merged_df['lagged_sentiment'], merged_df['Daily_Return'])
    return corr
