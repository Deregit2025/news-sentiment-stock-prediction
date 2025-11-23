import pandas as pd

def get_top_publishers(df, top_n=10):
    """
    Returns the top N most active publishers.

    Args:
        df (pd.DataFrame)
        top_n (int)

    Returns:
        pd.Series: Publisher counts
    """
    publisher_counts = df['publisher'].value_counts().head(top_n)
    return publisher_counts


def extract_email_domains(df):
    """
    Extracts domains from publisher emails and counts top domains.

    Args:
        df (pd.DataFrame)

    Returns:
        pd.Series: Top 10 publisher domains by frequency
    """
    # Create domain column if publisher looks like email
    df['publisher_domain'] = df['publisher'].apply(
        lambda x: x.split('@')[-1] if '@' in x else None
    )
    domain_counts = df['publisher_domain'].value_counts().head(10)
    return domain_counts


def publisher_content_summary(df, text_column='headline', top_n_words=10):
    """
    Summarizes first N words of headlines per publisher to give a quick idea of content differences.

    Args:
        df (pd.DataFrame)
        text_column (str)
        top_n_words (int)

    Returns:
        dict: {publisher: list of first N words from combined headlines}
    """
    summary = {}
    publishers = df['publisher'].unique()
    for pub in publishers:
        combined_text = " ".join(df[df['publisher'] == pub][text_column].dropna())
        summary[pub] = combined_text.split()[:top_n_words]
    return summary
