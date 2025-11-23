# modules/stock/utils.py

import os
import pandas as pd

# ---------- Select Price Column ----------
def get_price_column(df):
    """
    Return 'Adj Close' if available, otherwise 'Price' or 'Close'.
    Ensures consistency across modules.
    """
    for col in ['Adj Close', 'Price', 'Close']:
        if col in df.columns:
            return col
    raise ValueError("No suitable price column found in DataFrame.")


# ---------- List CSV files in stock_data folder ----------
def list_stock_files(data_path):
    """
    List all CSV files in the given stock_data folder.
    
    Parameters:
    - data_path: path to stock_data folder
    
    Returns:
    - list of stock symbols (file names without .csv)
    """
    files = [f for f in os.listdir(data_path) if f.endswith('.csv')]
    symbols = [os.path.splitext(f)[0] for f in files]
    return symbols


# ---------- Safe column selection ----------
def select_columns(df, columns=None):
    """
    Safely select columns from DataFrame.
    
    Parameters:
    - df: DataFrame
    - columns: list of columns to select (default None = all numeric)
    
    Returns:
    - subset DataFrame
    """
    if columns is None:
        # Default: all numeric columns
        return df.select_dtypes(include='number')
    missing_cols = [c for c in columns if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Columns not found: {missing_cols}")
    return df[columns]
