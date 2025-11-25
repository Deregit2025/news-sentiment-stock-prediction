import pandas as pd

def merge_news_stock(news_df, stock_df):
    """
    Merge preprocessed news data and stock data based on date and stock symbol.
    Aggregates sentiment per day per stock (mean).
    """
    # 1️⃣ Aggregate daily sentiment per stock
    daily_sentiment = (
        news_df.groupby(['date', 'stock'])['polarity']
        .mean()
        .reset_index()
        .rename(columns={'polarity': 'Daily_Sentiment'})
    )

    # 2️⃣ Ensure stock_df date format matches
    stock_df['Date'] = pd.to_datetime(stock_df['Date'], utc=True)
    
    # 3️⃣ Merge datasets
    merged_df = pd.merge(
        daily_sentiment,
        stock_df[['Date', 'Close', 'Daily_Return']],
        left_on='date',
        right_on='Date',
        how='inner'
    )

    # Drop duplicate column
    merged_df = merged_df.drop(columns=['Date'])
    
    return merged_df


def compute_correlation(merged_df):
    """
    Compute Pearson correlation between sentiment and stock return.
    """
    return merged_df['Daily_Sentiment'].corr(merged_df['Daily_Return'])


def compute_lag_correlation(merged_df, lag_days=1):
    """
    Shift sentiment scores to previous day(s).
    Useful if market reacts next day.
    """
    merged_df['Lagged_Sentiment'] = merged_df['Daily_Sentiment'].shift(lag_days)
    return merged_df['Lagged_Sentiment'].corr(merged_df['Daily_Return'])
