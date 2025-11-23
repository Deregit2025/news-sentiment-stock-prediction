import pandas as pd

def dataset_overview(df):
    """
    Returns basic overview of the dataset: info and null values.

    Args:
        df (pd.DataFrame)

    Returns:
        dict: Contains 'info' and 'null_summary'
    """
    overview = {
        "info": df.info(),
        "null_summary": df.isnull().sum()
    }
    return overview


def analyze_headline_length(df):
    """
    Calculates headline length for each article and returns descriptive statistics.

    Args:
        df (pd.DataFrame)

    Returns:
        tuple: (DataFrame with 'headline_length' column, descriptive stats)
    """
    df['headline_length'] = df['headline'].apply(lambda x: len(str(x)))
    stats = df['headline_length'].describe()
    return df, stats


def count_articles_per_publisher(df, top_n=10):
    """
    Returns the count of articles per publisher (top N publishers by default).

    Args:
        df (pd.DataFrame)
        top_n (int): Number of top publishers to return

    Returns:
        pd.Series: Publisher counts
    """
    publisher_counts = df['publisher'].value_counts().head(top_n)
    return publisher_counts
