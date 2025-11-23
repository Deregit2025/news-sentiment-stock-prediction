# modules/stock/portfolio.py

import pandas as pd
import numpy as np
from pynance.pf import PortfolioCalculations

# ---------- Prepare stock data for portfolio ----------
def prepare_portfolio_data(df_dict, price_col='Price'):
    """
    Combine multiple stock DataFrames into a single DataFrame of returns.
    
    Parameters:
    - df_dict: dictionary of {symbol: df} where df contains Price column
    - price_col: column used for returns calculation
    
    Returns:
    - returns_df: DataFrame where each column is daily returns of a stock
    """
    price_data = pd.DataFrame()
    
    for symbol, df in df_dict.items():
        # Use 'Adj Close' if available, otherwise 'Price'
        col = 'Adj Close' if 'Adj Close' in df.columns else price_col
        price_data[symbol] = df[col]
    
    # Calculate daily returns
    returns_df = price_data.pct_change().dropna()
    return returns_df


# ---------- Optimize Portfolio ----------
def optimize_portfolio(returns_df, risk_free_rate=0.0):
    """
    Create an optimized portfolio using Pynance.
    
    Parameters:
    - returns_df: DataFrame of daily returns
    - risk_free_rate: risk-free rate for Sharpe ratio optimization
    
    Returns:
    - portfolio: Pynance Portfolio object with optimization results
    """
    portfolio = po.PortfolioCalculations(returns_df)
    portfolio.optimal_portfolio(risk_free_rate=risk_free_rate)
    return portfolio
