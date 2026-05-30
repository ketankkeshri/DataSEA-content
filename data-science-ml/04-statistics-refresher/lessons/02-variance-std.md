# Variance Std

Understanding variance and standard deviation is crucial for any data professional. These two statistical measures help quantify the spread of your data, which is essential in making informed decisions based on data analysis.

## What is Variance?

Variance measures how far each number in a dataset is from the mean (average) and, consequently, from every other number in the dataset. It’s the average of the squared differences from the mean. The formula for calculating variance (σ²) is:

```
σ² = Σ (xi - μ)² / N
```

Where:
- `xi` = each value in the dataset
- `μ` = mean of the dataset
- `N` = number of values in the dataset

### Example Calculation

Let's say we have the following dataset of exam scores: [85, 90, 92, 88, 87].

1. Calculate the mean:
   ```
   μ = (85 + 90 + 92 + 88 + 87) / 5 = 88.4
   ```

2. Calculate the squared differences from the mean:
   ```
   (85 - 88.4)² = 11.56
   (90 - 88.4)² = 2.56
   (92 - 88.4)² = 12.96
   (88 - 88.4)² = 0.16
   (87 - 88.4)² = 1.96
   ```

3. Calculate variance:
   ```
   σ² = (11.56 + 2.56 + 12.96 + 0.16 + 1.96) / 5 = 5.84
   ```

## What is Standard Deviation?

Standard deviation (σ) is simply the square root of the variance. It provides a measure of the average distance from the mean, making it easier to interpret than variance.

```
σ = √σ²
```

Continuing from our previous example, the standard deviation would be:

```
σ = √5.84 ≈ 2.42
```

### Why Use Standard Deviation?

- It’s in the same unit as the data, making it more interpretable.
- It helps identify outliers — values that fall far from the mean.

### Code Example in Python

Here’s how to calculate variance and standard deviation using Python:

```python
import numpy as np

# Sample dataset
scores = np.array([85, 90, 92, 88, 87])

# Calculate mean
mean = np.mean(scores)

# Calculate variance
variance = np.var(scores)

# Calculate standard deviation
std_dev = np.std(scores)

print(f"Mean: {mean:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
```

## Common pitfalls

- **Not using the correct formula**: Make sure you're using the right variance formula (population vs. sample).
- **Ignoring outliers**: Outliers can skew your variance and standard deviation, leading to misleading results.
- **Assuming normal distribution**: Variance and standard deviation don't imply anything about the distribution shape; always visualize your data.

## In a nutshell

- Variance quantifies data spread; higher variance means more spread.
- Standard deviation is the square root of variance, easier to interpret.
- Both are essential for understanding data behavior and making data-driven decisions.