# Common Types

Understanding data types is crucial in data analytics because they dictate how data is stored, processed, and interpreted. Knowing the common types helps you make informed decisions about data cleaning and analysis.

## Common Data Types

Data can come in various formats, and knowing how to identify and use these types is fundamental. Here are some of the most common types you'll encounter:

### 1. Numeric Types
Numeric data represents quantitative values. There are two primary subtypes:

- **Integer**: Whole numbers, e.g., `1`, `42`, `-5`.
- **Float**: Decimal numbers, e.g., `3.14`, `0.001`, `-2.5`.

```python
# Example of numeric types in Python
integer_value = 42
float_value = 3.14
print(f"Integer: {integer_value}, Float: {float_value}")
```

### 2. String Types
String data types hold text values, which can represent anything from names to descriptions. Strings are often enclosed in quotes.

```python
# Example of string types in Python
name = "Alice"
description = "Data analyst with 5 years of experience."
print(f"Name: {name}, Description: {description}")
```

### 3. Boolean Type
Boolean types represent truth values. They can be either `True` or `False`, making them useful for logical operations.

```python
# Example of boolean types in Python
is_data_clean = True
print(f"Is data clean? {is_data_clean}")
```

### 4. Date and Time Types
Date and time types are used to represent dates and timestamps, critical for time series analysis.

```python
from datetime import datetime

# Example of date and time types in Python
current_time = datetime.now()
print(f"Current time: {current_time}")
```

## Choosing the Right Data Type

Selecting the correct data type is essential for efficient data processing and storage. Here are some guidelines:

- **Use numeric types** for any calculations or aggregations.
- **Use strings** for textual information, especially when it contains non-numeric characters.
- **Use booleans** for binary conditions, like flags.
- **Use date/time types** for any data related to time, as they provide useful methods for manipulation and comparison.

💡 **Tip:** In many databases, using the correct type can also improve query performance.

## Common pitfalls

- **Using the wrong type**: For example, storing numeric values as strings can lead to errors during calculations.
- **Data overflow**: Using integers that are too large for the designated storage type (e.g., exceeding the limit of an `INT`).
- **Timezone issues**: When dealing with date and time, not accounting for time zones can lead to incorrect data interpretation.

## In a nutshell

- Data types include numeric, string, boolean, and date/time.
- Choosing the right type is crucial for data integrity and performance.
- Common pitfalls include wrong type usage and data overflow.
- Always consider the context of your data when selecting types.