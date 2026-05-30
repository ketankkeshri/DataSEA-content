# Descriptive Stats

Descriptive statistics are essential for understanding data at a glance, providing insights into its central tendency, variability, and overall distribution. For a Data Analyst, mastering descriptive stats is crucial for summarizing datasets effectively and making informed decisions.

## Measures of Central Tendency

When you're analyzing data, the first thing to look at is the central tendency, which tells you where most of your data points lie. There are three primary measures:

- **Mean**: The average value, calculated by summing all values and dividing by the count.
- **Median**: The middle value when data is sorted. If the dataset has an even number of observations, it's the average of the two middle numbers.
- **Mode**: The most frequently occurring value in the dataset.

Here's how to compute these in Python using `pandas`:

```python
import pandas as pd

# Sample data
data = {
    'sales': [200, 220, 250, 270, 200, 300, 220, 250],
}

df = pd.DataFrame(data)

mean_sales = df['sales'].mean()
median_sales = df['sales'].median()
mode_sales = df['sales'].mode()[0]  # Get the first mode

print(f"Mean: {mean_sales}, Median: {median_sales}, Mode: {mode_sales}")
```

## Measures of Dispersion

Understanding how data spreads out is just as important as knowing where it centers. Key measures of dispersion include:

- **Range**: The difference between the maximum and minimum values.
- **Variance**: The average of the squared differences from the mean, indicating how much the values differ from the mean.
- **Standard Deviation**: The square root of the variance, providing a scale of dispersion that matches the original data units.

You can calculate these measures with the following code:

```python
# Continuing from the previous DataFrame
range_sales = df['sales'].max() - df['sales'].min()
variance_sales = df['sales'].var()
std_dev_sales = df['sales'].std()

print(f"Range: {range_sales}, Variance: {variance_sales}, Std Dev: {std_dev_sales}")
```

## Common pitfalls

- **Over-relying on the mean**: The mean can be skewed by outliers. Always check the median and mode for a fuller picture.
- **Ignoring the context**: Descriptive stats alone don’t tell the whole story. Consider the data's context and potential biases.
- **Forgetting to visualize**: Numbers are great, but visualizations (like histograms) can reveal trends that stats alone might miss.

## In a nutshell

- **Central tendency**: Mean, median, and mode summarize data locations.
- **Dispersion**: Range, variance, and standard deviation describe data spread.
- Always consider context and visualize your data for better insights.