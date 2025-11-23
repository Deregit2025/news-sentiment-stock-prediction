import matplotlib.pyplot as plt

# -----------------------------
# Headline Length Distribution
# -----------------------------
def plot_headline_length_distribution(df):
    plt.figure(figsize=(10, 5))
    df['headline_length'].hist(bins=30, color='skyblue', edgecolor='black')
    plt.title("Headline Length Distribution")
    plt.xlabel("Length of Headline")
    plt.ylabel("Frequency")
    plt.show()


# -----------------------------
# Top Publishers
# -----------------------------
def plot_top_publishers(publisher_counts):
    plt.figure(figsize=(10, 5))
    publisher_counts.plot(kind='bar', color='lightgreen', edgecolor='black')
    plt.title("Top Publishers by Article Count")
    plt.xlabel("Publisher")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


# -----------------------------
# Daily Publication Counts
# -----------------------------
def plot_daily_publication(daily_counts):
    plt.figure(figsize=(12, 5))
    daily_counts.plot(color='orange')
    plt.title("Daily Article Publication Counts")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# -----------------------------
# Publication Spikes
# -----------------------------
def plot_spikes(daily_counts, spikes):
    plt.figure(figsize=(12, 5))
    plt.plot(daily_counts.index, daily_counts.values, label='Daily Counts', color='blue')
    if not spikes.empty:
        plt.scatter(spikes.index, spikes.values, color='red', label='Spikes', s=100, marker='o')
    plt.title("Publication Frequency with Spikes Highlighted")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


# -----------------------------
# Hourly Publication Distribution
# -----------------------------
def plot_hourly_publication(hourly_counts):
    plt.figure(figsize=(10, 5))
    hourly_counts.plot(kind='bar', color='purple', edgecolor='black')
    plt.title("Article Publication by Hour of Day")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
