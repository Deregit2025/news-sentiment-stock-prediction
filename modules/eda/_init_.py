# Data Loader
from .data_loader import load_news_data

# Preprocessing
from .preprocessing import preprocess_news_dataframe, clean_text

# Descriptive Statistics
from .descriptive_stats import dataset_overview, analyze_headline_length, count_articles_per_publisher

# Publisher Analysis
from .publisher_analysis import get_top_publishers, extract_email_domains, publisher_content_summary

# Text Analysis (NLP)
from .text_analysis import extract_keywords, nlp_topic_modeling

# Time Series Analysis
from .time_series_analysis import daily_publication_count, detect_publication_spikes, hourly_publication_distribution

# Optional: plotting module
from .plot import *
