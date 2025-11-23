# modules/stock/plotting.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Modern seaborn theme
sns.set_theme(style="darkgrid")


# ---------- Price + SMA/EMA ----------
def plot_price_with_ma(df, price_col='Price', ma_cols=None, figsize=(12,6), title=None):
    """
    Plot stock price with moving averages (SMA/EMA)
    
    Parameters:
    - df: pandas DataFrame
    - price_col: main price column (default 'Price')
    - ma_cols: list of columns for moving averages
    - figsize: figure size
    - title: plot title
    """
    plt.figure(figsize=figsize)
    plt.plot(df.index, df[price_col], label=price_col, linewidth=2, color='black')
    
    if ma_cols:
        for col in ma_cols:
            plt.plot(df.index, df[col], label=col, linewidth=1.5)
    
    plt.title(title or f"{price_col} with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()


# ---------- RSI ----------
def plot_rsi(df, rsi_col='RSI_14', overbought=70, oversold=30, figsize=(12,4), title=None):
    """
    Plot RSI with overbought and oversold levels
    """
    plt.figure(figsize=figsize)
    plt.plot(df.index, df[rsi_col], label=rsi_col, color='blue', linewidth=1.5)
    plt.axhline(overbought, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(oversold, color='green', linestyle='--', label='Oversold (30)')
    plt.title(title or f"RSI ({rsi_col})")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.show()


# ---------- MACD ----------
def plot_macd(df, macd_col='MACD', signal_col='MACD_signal', hist_col='MACD_hist', figsize=(12,5), title=None):
    """
    Plot MACD line, signal line, and histogram
    """
    plt.figure(figsize=figsize)
    plt.plot(df.index, df[macd_col], label='MACD', color='blue')
    plt.plot(df.index, df[signal_col], label='Signal', color='red')
    plt.bar(df.index, df[hist_col], label='Histogram', color='gray', alpha=0.5)
    plt.title(title or "MACD")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.show()


# ---------- Bollinger Bands ----------
def plot_bollinger_bands(df, price_col='Price', upper_col='BB_Upper', middle_col='BB_Middle', lower_col='BB_Lower',
                         figsize=(12,6), title=None):
    """
    Plot Price with Bollinger Bands
    """
    plt.figure(figsize=figsize)
    plt.plot(df.index, df[price_col], label=price_col, color='black')
    plt.plot(df.index, df[upper_col], label='Upper Band', color='red', linestyle='--')
    plt.plot(df.index, df[middle_col], label='Middle Band', color='blue', linestyle='--')
    plt.plot(df.index, df[lower_col], label='Lower Band', color='green', linestyle='--')
    
    plt.fill_between(df.index, df[lower_col], df[upper_col], color='gray', alpha=0.1)
    
    plt.title(title or f"{price_col} with Bollinger Bands")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

