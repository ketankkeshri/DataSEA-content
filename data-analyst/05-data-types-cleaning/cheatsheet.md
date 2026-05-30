```markdown
# Data Types & Cleaning — Cheatsheet

## [Common Types]

| Thing            | Syntax                 | Notes                                       |
|------------------|------------------------|---------------------------------------------|
| Integer          | `int`                  | Whole numbers, e.g., `42`.                  |
| Float            | `float`                | Decimal numbers, e.g., `3.14`.              |
| String           | `str`                  | Text, e.g., `"Hello, World!"`.              |
| Boolean          | `bool`                 | True or False, e.g., `True`.                |
| List             | `list`                 | Ordered collection, e.g., `[1, 2, 3]`.      |
| Dictionary       | `dict`                 | Key-value pairs, e.g., `{"key": "value"}`. |

## [Handling Missing Data]

```python
import pandas as pd

# Fill missing values
df.fillna(value=0, inplace=True)

# Drop rows with missing values
df.dropna(inplace=True)
```

## [Removing Duplicates]

```python
import pandas as pd

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Keep the first occurrence of duplicates
df.drop_duplicates(keep='first', inplace=True)
```

## [Normalization Techniques]

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(df[['column_name']])
```

## [Gotchas]

- ⚠️ Watch out for `NaN` vs. `None` in pandas; they behave differently.
- ⚠️ `dropna()` can lead to data loss; always check data shape before and after.

## [Mental model]

- **Data Types**: Think of them as containers for your data. Choose wisely based on the kind of data you have.
- **Missing Data Handling**: Decide whether to fill or drop based on the impact on analysis.
- **Normalization**: Scale features to give them equal weight in models; think of it like leveling the playing field.
```