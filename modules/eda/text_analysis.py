from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from .preprocessing import clean_text

def extract_keywords(df, column='cleaned_text', top_n=10):
    """
    Extracts top N keywords across the corpus using TF-IDF scores.

    Args:
        df (pd.DataFrame)
        column (str): Name of cleaned text column
        top_n (int)

    Returns:
        list of top keywords
    """
    tfidf = TfidfVectorizer(max_df=0.95, min_df=2)
    X = tfidf.fit_transform(df[column])

    # Compute average TF-IDF per word
    tfidf_scores = X.mean(axis=0).tolist()[0]
    feature_names = tfidf.get_feature_names_out()

    # Pair words with scores and sort
    word_scores = list(zip(feature_names, tfidf_scores))
    word_scores = sorted(word_scores, key=lambda x: x[1], reverse=True)

    top_keywords = [word for word, score in word_scores[:top_n]]
    return top_keywords


def nlp_topic_modeling(df, column='cleaned_text', n_topics=5, n_words=10):
    """
    Performs LDA topic modeling on cleaned text.

    Args:
        df (pd.DataFrame)
        column (str): Name of cleaned text column
        n_topics (int): Number of topics
        n_words (int): Number of top words per topic

    Returns:
        list of strings describing topics
    """
    # Vectorize text
    vectorizer = CountVectorizer(max_df=0.95, min_df=2)
    X = vectorizer.fit_transform(df[column])

    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(X)

    topics = []
    for idx, topic in enumerate(lda.components_):
        top_words = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-n_words:]]
        topics.append(f"Topic {idx+1}: {', '.join(top_words)}")

    return topics
