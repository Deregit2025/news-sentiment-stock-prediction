# modules/stock/eda.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from IPython.display import display


# Set seaborn style for nicer plots
sns.set_theme(style="darkgrid")


def basic_info(df, symbol=None):
    """
    Print basic info: shape, columns, data types, first/last rows
    """
    label = f" ({symbol})" if symbol else ""
    print(f"\n===== BASIC INFO{label} =====")
    print("Shape:", df.shape)
    print("\nData types:")
    print(df.dtypes)
    print("\nDataFrame.info():")
    df.info()
    print("\nFirst 5 rows:")
    display(df.head())
    print("\nLast 5 rows:")
    display(df.tail())


def descriptive_stats(df, include_returns=False):
    """
    Descriptive statistics: mean, std, min, max, skew, kurtosis
    If include_returns=True, also calculate percent change (returns)
    """
    stats = df.describe().transpose()
    stats['skew'] = df.skew(numeric_only=True)
    stats['kurtosis'] = df.kurtosis(numeric_only=True)

    if include_returns:
        returns = df['Price'].pct_change().dropna()
        returns_stats = returns.describe().to_frame(name='returns')
        returns_stats.loc['skew'] = returns.skew()
        returns_stats.loc['kurtosis'] = returns.kurtosis()
        return stats, returns_stats

    return stats


def missing_values(df):
    """
    Return missing value counts and percentages
    """
    missing_count = df.isnull().sum()
    missing_pct = (missing_count / len(df)) * 100
    missing_df = pd.concat([missing_count, missing_pct], axis=1)
    missing_df.columns = ['missing_count', 'missing_pct']
    return missing_df.sort_values(by='missing_count', ascending=False)


def time_range(df):
    """
    Return start date, end date, and approximate frequency
    """
    start = df.index.min()
    end = df.index.max()
    try:
        freq = (df.index[1] - df.index[0])
    except Exception:
        freq = None
    return {'start': start, 'end': end, 'approx_freq': freq}


def correlation_matrix(df, numeric_only=True, annot=True, figsize=(8,6)):
    """
    Plot correlation matrix for numeric columns
    """
    corr = df.corr(numeric_only=numeric_only)
    plt.figure(figsize=figsize)
    sns.heatmap(corr, annot=annot, fmt=".2f", cmap='vlag', center=0)
    plt.title("Correlation Matrix")
    plt.show()
    return corr


def plot_time_series(df, columns=None, figsize=(12,5), title=None):
    """
    Plot selected columns over time
    """
    if columns is None:
        columns = ['Price'] if 'Price' in df.columns else df.select_dtypes(include=np.number).columns.tolist()
    plt.figure(figsize=figsize)
    df[columns].plot()
    plt.title(title or "Time Series")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.show()


def plot_distribution(df, column='Price', bins=50, figsize=(8,4)):
    """
    Plot histogram + KDE of a column
    """
    plt.figure(figsize=figsize)
    sns.histplot(df[column].dropna(), bins=bins, kde=True)
    plt.title(f"Distribution of {column}")
    plt.show()


def plot_returns_distribution(df, column='Price', bins=50, figsize=(8,4)):
    """
    Plot percent-change (returns) distribution
    """
    returns = df[column].pct_change().dropna()
    plt.figure(figsize=figsize)
    sns.histplot(returns, bins=bins, kde=True)
    plt.title(f"Returns Distribution of {column}")
    plt.show()
    return returns


def rolling_stats(df, column='Price', window=20, figsize=(12,6)):
    """
    Plot rolling mean and rolling std (volatility)
    """
    rolling_mean = df[column].rolling(window).mean()
    rolling_std = df[column].rolling(window).std()

    plt.figure(figsize=figsize)
    plt.plot(df.index, df[column], label='Price', alpha=0.6)
    plt.plot(rolling_mean, label=f'Rolling Mean ({window})')
    plt.plot(rolling_std, label=f'Rolling Std ({window})')
    plt.legend()
    plt.title(f"Rolling statistics ({window} days)")
    plt.show()


def detect_outliers_iqr(df, column='Price', multiplier=1.5):
    """
    Detect outliers using IQR method
    Returns boolean mask and DataFrame of outliers
    """
    series = df[column].dropna()
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - multiplier * iqr
    upper = q3 + multiplier * iqr
    mask = (df[column] < lower) | (df[column] > upper)
    return mask, df[mask]


def seasonal_decompose_plot(df, column='Price', model='additive', period=None):
    """
    Decompose time-series into trend, seasonal, residual components
    period: number of observations in a cycle (e.g., 252 for daily trading data ~1 year)
    """
    if period is None:
        period = 252
    clean = df[column].dropna()
    result = seasonal_decompose(clean, model=model, period=period, extrapolate_trend='freq')
    result.plot()
    plt.suptitle(f"Seasonal Decompose of {column} (period={period})", fontsize=14)
    plt.show()
    return result
