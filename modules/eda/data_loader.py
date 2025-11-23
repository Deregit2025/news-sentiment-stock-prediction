import pandas as pd
import os

def load_news_data(file_path="../data/news_data/news.csv"):
    """
    Loads the news CSV file and returns a pandas DataFrame.

    Args:
        file_path (str): Relative or absolute path to the news CSV file.

    Returns:
        pd.DataFrame
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found: {file_path}")

    df = pd.read_csv(file_path)

    # Basic info
    print(f"📂 Loaded '{file_path}' successfully.")
    print(f"🔹 Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    return df
