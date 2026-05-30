# Mean Median Mode

Understanding the mean, median, and mode is crucial for any data enthusiast. These basic statistical measures provide insights into data distribution and help you summarize large datasets effectively, making them essential tools for data analysis and decision-making.

## What are Mean, Median, and Mode?

- **Mean:** The average of a dataset, calculated by adding all values and dividing by the count of values. It's great for normally distributed data but can be skewed by outliers.
  
- **Median:** The middle value when a dataset is ordered. If there’s an even number of observations, the median is the average of the two middle numbers. The median is robust against outliers, making it a better measure for skewed distributions.
  
- **Mode:** The value that appears most frequently in a dataset. A dataset can have one mode (unimodal), more than one mode (bimodal or multimodal), or no mode at all.

Here's a simple example in Python:

```python
import numpy as np
from scipy import stats

data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7]

mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data).mode[0]

print(f"Mean: {mean}, Median: {median}, Mode: {mode}")
```

## When to Use Each Measure

Choosing between mean, median, and mode depends on your data and what you want to convey:

- **Use Mean** when:
  - Data is symmetrically distributed without outliers.
  - You want to understand overall trends.

- **Use Median** when:
  - Data is skewed (e.g., income distribution).
  - You need a measure that isn’t affected by extreme values.

- **Use Mode** when:
  - Identifying the most common item in categorical data.
  - Analyzing distributions with multiple peaks.

### Visual Representation

Visualizing these measures can clarify their differences. Consider this distribution of test scores:

- If the scores are: `[50, 55, 60, 65, 70, 80, 95]`
- The mean is `65`, median is `65`, and mode is `None` (since all values are unique).

Now, if you have scores like `[50, 50, 60, 65, 70, 80, 95]`, the mean is still `65`, but the mode becomes `50`. 

## Common pitfalls

- **Confusing Mean with Median:** Be careful when interpreting average data; outliers can skew the mean significantly.
  
- **Ignoring Data Distribution:** Always visualize data first. A mean can give a false representation if the data is heavily skewed.

- **Assuming Mode is Always Useful:** In some datasets, especially continuous ones, the mode might not provide meaningful insights.

## In a nutshell

- **Mean** is the average; great for normal distributions.
- **Median** is the middle value; best for skewed data.
- **Mode** is the most frequent value; useful for categorical data.
- Choose wisely based on the data characteristics and analysis needs.