
# modules/stock/data_loader.py

import pandas as pd
import os

# Root-relative path to stock_data folder
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'stock_data')

def load_stock(symbol):
    """
    Load a stock CSV from stock_data folder.
    
    Parameters:
    - symbol: str, stock ticker (without .csv)
    
    Returns:
    - df: pandas DataFrame with Date as index and 'Price' column (Adj Close if available, else Close)
    """

    # Full file path
    file_path = os.path.join(DATA_PATH, f"{symbol}.csv")

    # Load CSV
    df = pd.read_csv(file_path, parse_dates=['Date'])

    # Use 'Adj Close' if present, else 'Close'
    if 'Adj Close' in df.columns:
        df['Price'] = df['Adj Close']
    else:
        df['Price'] = df['Close']

    # Set Date as index
    df.set_index('Date', inplace=True)

    # Sort chronologically
    df.sort_index(inplace=True)

    return df
