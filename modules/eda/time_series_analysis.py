import pandas as pd

def daily_publication_count(df, date_column='date'):
    """
    Returns daily publication counts.

    Args:
        df (pd.DataFrame)
        date_column (str): Name of the datetime column

    Returns:
        pd.Series: Daily counts indexed by date
    """
    df[date_column] = pd.to_datetime(df[date_column])
    daily_counts = df.groupby(df[date_column].dt.date).size()
    return daily_counts


def detect_publication_spikes(daily_counts, threshold_factor=2):
    """
    Detect spikes in publication frequency.

    Args:
        daily_counts (pd.Series)
        threshold_factor (float): Multiplier for standard deviation above mean

    Returns:
        pd.Series: Dates with spikes
        float: Threshold used
    """
    mean = daily_counts.mean()
    std = daily_counts.std()
    threshold = mean + threshold_factor * std
    spikes = daily_counts[daily_counts > threshold]
    return spikes, threshold


def hourly_publication_distribution(df, date_column='date'):
    """
    Returns article counts by hour of the day.

    Args:
        df (pd.DataFrame)
        date_column (str)

    Returns:
        pd.Series: Counts indexed by hour (0-23)
    """
    df[date_column] = pd.to_datetime(df[date_column])
    hourly_counts = df.groupby(df[date_column].dt.hour).size()
    return hourly_counts
