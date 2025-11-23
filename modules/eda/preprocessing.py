import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data once
nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text):
    """
    Cleans textual data:
    - Converts to lowercase
    - Removes punctuation and numbers
    - Removes stopwords
    - Lemmatizes words

    Args:
        text (str)

    Returns:
        str: Cleaned text
    """
    text = str(text).lower()  # lowercase
    text = re.sub(r'[^a-z\s]', '', text)  # remove numbers & punctuation
    tokens = text.split()

    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if w not in stop_words]

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(w) for w in tokens]

    return ' '.join(tokens)


def preprocess_news_dataframe(df, text_column='headline', date_column='date'):
    """
    Preprocesses the news dataframe:
    - Cleans text
    - Converts date column to datetime
    - Removes rows with missing headlines or publishers

    Args:
        df (pd.DataFrame)
        text_column (str): Name of the text column
        date_column (str): Name of the date column

    Returns:
        pd.DataFrame: Preprocessed dataframe
    """
    # Drop rows with missing text or publisher
    df = df.dropna(subset=[text_column, 'publisher'])

    # Clean text
    df['cleaned_text'] = df[text_column].apply(clean_text)

    # Convert date column to datetime
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
    df = df.dropna(subset=[date_column])  # drop rows with invalid dates

    return df
