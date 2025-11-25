# plot.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("whitegrid")

# -----------------------------
# Plot Sentiment vs Returns Over Time
# -----------------------------
def plot_sentiment_vs_returns(df: pd.DataFrame, stock_symbol: str):
    """
    Plot average daily sentiment and stock returns over time.
    Args:
        df (pd.DataFrame): Merged DataFrame with 'date', 'avg_daily_sentiment', 'Daily_Return'
        stock_symbol (str): Stock symbol for title
    """
    plt.figure(figsize=(12,5))
    plt.plot(df['date'], df['avg_daily_sentiment'], label='Avg Daily Sentiment', marker='o')
    plt.plot(df['date'], df['Daily_Return'], label='Daily Return', marker='x')
    plt.title(f"{stock_symbol} - Sentiment vs Daily Returns Over Time")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# -----------------------------
# Scatter Plot: Sentiment vs Returns
# -----------------------------
def plot_scatter_correlation(df: pd.DataFrame, stock_symbol: str):
    """
    Scatter plot between avg daily sentiment and daily returns.
    Args:
        df (pd.DataFrame): Merged DataFrame
        stock_symbol (str): Stock symbol for title
    """
    plt.figure(figsize=(8,6))
    sns.scatterplot(x='avg_daily_sentiment', y='Daily_Return', data=df)
    sns.regplot(x='avg_daily_sentiment', y='Daily_Return', data=df, scatter=False, color='red')
    plt.title(f"{stock_symbol} - Sentiment vs Daily Returns")
    plt.xlabel("Avg Daily Sentiment")
    plt.ylabel("Daily Return")
    plt.tight_layout()
    plt.show()

# -----------------------------
# Correlation Heatmap
# -----------------------------
def plot_correlation_heatmap(df: pd.DataFrame):
    """
    Plot correlation heatmap for all numeric columns in DataFrame.
    Args:
        df (pd.DataFrame): DataFrame containing numeric columns (avg_daily_sentiment, Daily_Return)
    """
    plt.figure(figsize=(6,5))
    corr_matrix = df[['avg_daily_sentiment', 'Daily_Return']].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='viridis', fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()
