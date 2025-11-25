# data_loader.py
import pandas as pd
import os

# Base paths
NEWS_PATH = os.path.join("data", "news_data", "news.csv")
STOCK_PATH = os.path.join("data", "stock_data")

# -----------------------------
# Load News Data
# -----------------------------
def load_news_data():
    """
    Load news CSV and normalize date column to datetime with UTC.
    Returns:
        pd.DataFrame: news data with 'date', 'headline', 'stock', etc.
    """
    df = pd.read_csv(NEWS_PATH)
    
    # Ensure date column is datetime with UTC
    df['date'] = pd.to_datetime(df['date'], utc=True)
    
    # Clean stock symbols if necessary
    df['stock'] = df['stock'].str.upper()
    
    return df

# -----------------------------
# Load Stock Data
# -----------------------------
def load_stock_data(symbol: str):
    """
    Load stock CSV by symbol and normalize Date column.
    Args:
        symbol (str): Stock symbol (e.g., 'AAPL')
    Returns:
        pd.DataFrame: Stock data with 'Date', 'Close', etc.
    """
    filename = f"{symbol.lower()}.csv"
    path = os.path.join(STOCK_PATH, filename)
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"Stock file for {symbol} not found at {path}")
    
    df = pd.read_csv(path)
    
    # Normalize Date column
    df['Date'] = pd.to_datetime(df['Date'], utc=True)
    
    return df

# -----------------------------
# List Available Stocks
# -----------------------------
def list_available_stocks():
    """
    Returns list of available stock symbols from stock_data folder.
    """
    files = os.listdir(STOCK_PATH)
    symbols = [f.split(".")[0].upper() for f in files if f.endswith(".csv")]
    return symbols
