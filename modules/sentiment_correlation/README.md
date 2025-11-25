
# Sentiment and Correlation Analysis Project

## Project Overview
This project performs **sentiment analysis on financial news headlines** and evaluates the **correlation between news sentiment and stock price movements**. The analysis helps Nova Financial Solutions enhance its predictive analytics capabilities for financial forecasting.

---

## Folder Structure

```

sentiment/
├── data/
│   ├── news_data/news.csv
│   └── stock_data/
│       ├── aapl.csv
│       ├── amzn.csv
│       ├── goog.csv
│       ├── meta.csv
│       ├── msft.csv
│       └── nvda.csv
├── modules/
│   └── sentiment_correlation/
│       ├── **init**.py
│       ├── data_handler.py        # Load news and stock data
│       ├── sentiment_analysis.py # Perform sentiment scoring
│       ├── correlation.py        # Merge datasets & compute correlations
│       └── plots.py              # Visualization functions
└── notebooks/
└── senti_corr.ipynb          # Modular notebook for running analysis

````

---

## Modules Description

### 1. `data_handler.py`
- Loads news data (`news.csv`) and stock price CSVs.
- Returns cleaned `DataFrame`s ready for processing.
- Functions:  
  - `load_news_data()`  
  - `load_stock_data(symbol)`  
  - `list_available_stocks()`

### 2. `sentiment_analysis.py`
- Preprocesses news headlines.
- Computes **TextBlob sentiment scores** (polarity and label: positive, neutral, negative).  
- Functions:  
  - `preprocess_news_data(news_df)`  
  - `preprocess_stock_data(stock_df)`  

### 3. `correlation.py`
- Merges news sentiment with stock daily returns.  
- Computes correlation between sentiment and stock price movements.
- Supports optional **lag correlation**.
- Functions:  
  - `merge_news_stock(news_df, stock_df)`  
  - `compute_correlation(merged_df)`  
  - `compute_lag_correlation(merged_df, lag_days=1)`

### 4. `plots.py`
- Visualizes sentiment trends and stock returns.  
- Functions:  
  - `plot_sentiment_vs_returns()`  
  - `plot_scatter_correlation()`  
  - `plot_correlation_heatmap()`

---

## Notebook: `senti_corr.ipynb`
- Fully modular; uses the above modules.  
- Steps:
  1. Load news and stock data
  2. Preprocess and clean datasets
  3. Merge datasets by stock symbol and date
  4. Compute daily stock returns
  5. Compute correlation between sentiment and returns
  6. Visualize trends and scatter plots
  7. Optional: Loop through all available stocks

---

## How to Run
1. Clone the repository or copy the folder structure.  
2. Ensure you have required packages installed:

```bash
pip install pandas matplotlib seaborn textblob nltk
````

3. Open `notebooks/senti_corr.ipynb` in VSCode or Jupyter Notebook.
4. Run all cells sequentially.

---

## Notes

* Ensure the notebook is opened from the **project root (`sentiment/`)** so that custom modules are properly detected.
* The first cell in the notebook adds the project root to `sys.path` to avoid `ModuleNotFoundError`.
* Sentiment polarity thresholds:

  * Positive: `polarity > 0.05`
  * Negative: `polarity < -0.05`
  * Neutral: between `-0.05` and `0.05`

```


