

```markdown
# Sentiment News EDA

This repository contains a **modular Exploratory Data Analysis (EDA)** project on news headlines and publisher data. The EDA is designed to be reusable, clean, and scalable, using Python and Jupyter Notebook.

---

## 📁 Project Structure

```

sentiment/
│
├── data/
│   ├── news_data/
│   │   └── news.csv          # News dataset
│   └── stock_data/           # (Optional future use)
│
├── modules/
│   └── eda/
│       ├── **init**.py
│       ├── data_loader.py
│       ├── preprocessing.py
│       ├── descriptive_stats.py
│       ├── publisher_analysis.py
│       ├── text_analysis.py
│       ├── time_series_analysis.py
│       └── plot.py
│
└── notebooks/
└── eda.ipynb              # Main notebook for EDA

````

---

## 🛠 Features

### 1. Data Loading
- Loads news CSV data in a safe and modular way using `data_loader.py`.

### 2. Preprocessing
- Cleans text: lowercase, removes punctuation & numbers, removes stopwords, lemmatizes.
- Converts `date` column to datetime.
- Handles missing values.

### 3. Descriptive Statistics
- Calculates headline lengths and basic statistics.
- Counts articles per publisher.
- Adds `headline_length` column for analysis.

### 4. Publisher Analysis
- Identifies top publishers.
- Extracts domains if publisher names are emails.
- Summarizes headline content per publisher.

### 5. Text Analysis (NLP)
- Extracts top keywords using TF-IDF.
- Performs topic modeling using LDA.

### 6. Time Series Analysis
- Computes daily publication counts.
- Detects spikes in publication frequency.
- Analyzes hourly publication distribution.

### 7. Plotting
- Modular plotting functions for headline length, top publishers, daily and hourly distributions, and spikes.

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd sentiment
````

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

**`requirements.txt`** should include:

```
pandas
matplotlib
nltk
scikit-learn
```

4. Download NLTK data (stopwords & wordnet) if not done:

```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
```

---

## 🚀 Usage

Open the notebook:

```bash
jupyter notebook notebooks/eda.ipynb
```

Step through the notebook to:

* Load data
* Preprocess
* Perform descriptive stats
* Analyze publishers
* Perform text analysis
* Run time series analysis
* Generate plots

---

## 📊 Output

* Headline length distribution
* Top publishers and their domains
* Keywords and topics from headlines
* Daily and hourly article frequency
* Publication spikes detection

---

## 💻 Notes

* Modular design allows **easy extension** for additional datasets or analyses.
* All plotting functions are separate in `plot.py`.
* Designed to run with **Python 3.8+** and **Jupyter Notebook**.

---

## 📜 License

This project is open-source and available under the MIT License.

```

