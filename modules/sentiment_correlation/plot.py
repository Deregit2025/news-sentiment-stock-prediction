import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_vs_returns(merged_df, stock_symbol=None):
    """
    Plot daily sentiment and stock returns over time.
    If stock_symbol is given, filter by that.
    """
    if stock_symbol:
        merged_df = merged_df[merged_df['stock'] == stock_symbol]

    plt.figure(figsize=(10, 5))
    plt.plot(merged_df['date'], merged_df['Daily_Sentiment'], label='Daily Sentiment')
    plt.plot(merged_df['date'], merged_df['Daily_Return'], label='Daily Return')
    plt.legend()
    plt.title(f"Sentiment vs Daily Returns ({stock_symbol if stock_symbol else 'All Stocks'})")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()


def plot_scatter_correlation(merged_df, stock_symbol=None):
    """
    Create a scatter plot of sentiment vs returns with regression.
    """
    if stock_symbol:
        merged_df = merged_df[merged_df['stock'] == stock_symbol]

    plt.figure(figsize=(6, 4))
    sns.regplot(x='Daily_Sentiment', y='Daily_Return', data=merged_df, scatter_kws={'alpha': 0.5})
    plt.title(f"Sentiment vs Stock Return ({stock_symbol if stock_symbol else 'All Stocks'})")
    plt.xlabel("Daily Sentiment")
    plt.ylabel("Daily Return")
    plt.show()


def plot_correlation_heatmap(merged_df):
    """
    Correlation heatmap of sentiment and returns.
    Useful if more variables included.
    """
    correlation_matrix = merged_df[['Daily_Sentiment', 'Daily_Return']].corr()

    plt.figure(figsize=(4, 3))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()
