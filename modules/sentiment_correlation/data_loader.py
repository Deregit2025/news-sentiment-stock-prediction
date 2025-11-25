import pandas as pd
import os

# Path configurations
NEWS_DATA_PATH = os.path.join("data", "news_data", "news.csv")
STOCK_DATA_FOLDER = os.path.join("data", "stock_data")

def load_news_data():
    """Loads the news dataset."""
    try:
        df_news = pd.read_csv(NEWS_DATA_PATH)
        print(f"[INFO] Loaded news data: {df_news.shape} rows")
        return df_news
    except Exception as e:
        print(f"[ERROR] Failed to load news data: {e}")
        return None

def load_stock_data(symbol):
    """
    Loads stock data for a specific stock symbol.
    Example: load_stock_data('AAPL')
    """
    filename = f"{symbol.lower()}.csv"
    stock_file_path = os.path.join(STOCK_DATA_FOLDER, filename)

    try:
        df_stock = pd.read_csv(stock_file_path)
        print(f"[INFO] Loaded stock data for {symbol}: {df_stock.shape} rows")
        return df_stock
    except Exception as e:
        print(f"[ERROR] Could not load stock data for {symbol}: {e}")
        return None

def list_available_stocks():
    """Returns a list of CSV files in the stock_data folder (symbols available)."""
    try:
        files = os.listdir(STOCK_DATA_FOLDER)
        stock_symbols = [file.split(".")[0].upper() for file in files if file.endswith(".csv")]
        return stock_symbols
    except Exception as e:
        print(f"[ERROR] Unable to list stock files: {e}")
        return []
