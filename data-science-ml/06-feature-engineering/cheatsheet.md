```markdown
# Feature Engineering Basics — Cheatsheet

## [Section 1: Scaling Techniques]

| Thing                   | Syntax                             | Notes                                         |
|-------------------------|------------------------------------|-----------------------------------------------|
| Min-Max Scaling         | `X_scaled = (X - X.min()) / (X.max() - X.min())` | Transforms features to a range [0, 1].       |
| Standardization         | `X_standardized = (X - X.mean()) / X.std()` | Centers data around mean with unit variance. |
| Robust Scaling          | `X_robust_scaled = (X - X.median()) / X.quantile(0.75) - X.quantile(0.25)` | Robust to outliers.                          |

## [Section 2: Encoding Categorical Variables]

| Thing                   | Syntax                             | Notes                                         |
|-------------------------|------------------------------------|-----------------------------------------------|
| One-Hot Encoding        | `pd.get_dummies(df, columns=['cat_col'])` | Converts categories to binary columns.       |
| Label Encoding          | `from sklearn.preprocessing import LabelEncoder; le = LabelEncoder(); df['cat_col'] = le.fit_transform(df['cat_col'])` | Assigns integers to categories.              |
| Target Encoding         | `target_mean = df.groupby('cat_col')['target'].mean(); df['cat_col_encoded'] = df['cat_col'].map(target_mean)` | Encodes based on target mean.                |

## [Datetime Features]

| Thing                   | Syntax                             | Notes                                         |
|-------------------------|------------------------------------|-----------------------------------------------|
| Extracting Year         | `df['year'] = df['date_column'].dt.year` | Useful for seasonal analysis.                |
| Extracting Month        | `df['month'] = df['date_column'].dt.month` | Identify monthly trends.                     |
| Days Since              | `df['days_since'] = (pd.to_datetime('today') - df['date_column']).dt.days` | Time-based features for modeling.            |

## [Text Features]

| Thing                   | Syntax                             | Notes                                         |
|-------------------------|------------------------------------|-----------------------------------------------|
| Bag of Words            | `from sklearn.feature_extraction.text import CountVectorizer; vectorizer = CountVectorizer(); X = vectorizer.fit_transform(df['text_column'])` | Converts text to a matrix of token counts.  |
| TF-IDF                  | `from sklearn.feature_extraction.text import TfidfVectorizer; tfidf = TfidfVectorizer(); X = tfidf.fit_transform(df['text_column'])` | Weighs terms based on frequency in corpus.  |
| N-grams                 | `from sklearn.feature_extraction.text import CountVectorizer; vectorizer = CountVectorizer(ngram_range=(1, 2)); X = vectorizer.fit_transform(df['text_column'])` | Captures sequences of words.                 |

## [Gotchas]

- ⚠️ Always inspect your data after scaling to ensure no loss of information.
- ⚠️ One-hot encoding increases dimensionality; be cautious with high-cardinality variables.
- ⚠️ Datetime features can introduce multicollinearity; use with care.

## [Mental model]

- **Scaling**: Adjusts feature distributions for better model performance.
- **Encoding**: Transforms categorical data into numerical formats for algorithms.
- **Datetime & Text Features**: Extracts meaningful patterns from temporal and textual data.
```