# modules/stock/indicators.py

import pandas as pd
import numpy as np
import talib  # Technical Analysis Library


# ---------- Simple Moving Average (SMA) ----------
def add_sma(df, window=20, column='Price'):
    """
    Add Simple Moving Average (SMA) using TA-Lib.
    """
    df[f'SMA_{window}'] = talib.SMA(df[column].values, timeperiod=window)
    return df


# ---------- Exponential Moving Average (EMA) ----------
def add_ema(df, window=20, column='Price'):
    """
    Add Exponential Moving Average (EMA) using TA-Lib.
    """
    df[f'EMA_{window}'] = talib.EMA(df[column].values, timeperiod=window)
    return df


# ---------- Relative Strength Index (RSI) ----------
def add_rsi(df, window=14, column='Price'):
    """
    Add RSI using TA-Lib.
    """
    df[f'RSI_{window}'] = talib.RSI(df[column].values, timeperiod=window)
    return df


# ---------- Moving Average Convergence Divergence (MACD) ----------
def add_macd(df, fast=12, slow=26, signal=9, column='Price'):
    """
    Add MACD, MACD signal, and MACD histogram using TA-Lib.
    """
    macd, macd_signal, macd_hist = talib.MACD(df[column].values,
                                              fastperiod=fast,
                                              slowperiod=slow,
                                              signalperiod=signal)
    df['MACD'] = macd
    df['MACD_signal'] = macd_signal
    df['MACD_hist'] = macd_hist
    return df


# ---------- Bollinger Bands ----------
def add_bollinger_bands(df, window=20, num_std=2, column='Price'):
    """
    Add Bollinger Bands using TA-Lib.
    Returns upper, middle, lower bands.
    """
    upper, middle, lower = talib.BBANDS(df[column].values,
                                        timeperiod=window,
                                        nbdevup=num_std,
                                        nbdevdn=num_std,
                                        matype=0)  # simple MA

    df['BB_Upper'] = upper
    df['BB_Middle'] = middle
    df['BB_Lower'] = lower
    return df
