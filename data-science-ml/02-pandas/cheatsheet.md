```markdown
# Pandas Essentials — Cheatsheet

## [Core syntax]

| Thing            | Syntax                          | Notes                          |
|------------------|---------------------------------|--------------------------------|
| Import pandas     | `import pandas as pd`           | Use `pd` as the alias.        |
| Create Series     | `pd.Series(data)`               | `data` can be a list, dict, etc. |
| Create DataFrame  | `pd.DataFrame(data)`            | `data` can be a dict of lists, etc. |
| View DataFrame    | `df.head(n)`                    | Shows first `n` rows (default 5). |
| Get shape         | `df.shape`                      | Returns tuple (rows, columns). |

## [Common operations]

```python
# Create a DataFrame
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NY', 'LA', 'SF']
}
df = pd.DataFrame(data)

# Indexing
print(df['Name'])         # Access column
print(df.iloc[0])        # Access first row

# Groupby
grouped = df.groupby('City').mean()  # Group data by 'City'

# Merge
df2 = pd.DataFrame({'City': ['NY', 'LA'], 'State': ['NY', 'CA']})
merged_df = pd.merge(df, df2, on='City', how='inner')

# Reshaping
reshaped_df = df.melt(id_vars=['Name'], value_vars=['Age', 'City'])  # Unpivot
```

## [Gotchas]

- ⚠️ Remember that DataFrames are mutable. Changes affect the original DataFrame unless copied explicitly.
- ⚠️ Grouping by non-aggregated columns can lead to unexpected results. Always specify aggregation functions.

## [Mental model]

- **DataFrame:** Table-like structure with rows and columns.
- **Series:** One-dimensional array, a single column of a DataFrame.
- **Indexing:** Access data via labels or positions, like SQL queries.
```