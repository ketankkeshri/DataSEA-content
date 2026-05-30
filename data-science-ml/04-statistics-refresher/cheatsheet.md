```markdown
# Statistics Refresher — Cheatsheet

## [Section 1: Measures of Central Tendency]

| Thing       | Syntax                     | Notes                             |
|-------------|----------------------------|-----------------------------------|
| Mean        | `mean(data)`               | Average of all values.            |
| Median      | `median(data)`             | Middle value when sorted.         |
| Mode        | `mode(data)`               | Most frequently occurring value.  |

## [Section 2: Variance and Standard Deviation]

| Thing               | Syntax                     | Notes                             |
|---------------------|----------------------------|-----------------------------------|
| Variance            | `variance(data)`           | Measure of data spread.           |
| Standard Deviation  | `std(data)`                | Square root of variance.          |

## [Section 3: Distributions]

| Distribution Type   | Syntax                     | Notes                             |
|---------------------|----------------------------|-----------------------------------|
| Normal              | `scipy.stats.norm`         | Continuous; bell-shaped curve.    |
| Binomial            | `scipy.stats.binom`        | Discrete; fixed number of trials. |
| Poisson             | `scipy.stats.poisson`      | Discrete; counts events in a time frame. |

## [Section 4: Central Limit Theorem (CLT)]

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate random samples
samples = [np.random.normal(loc=0, scale=1, size=30) for _ in range(1000)]
means = [np.mean(sample) for sample in samples]

# Plotting the distribution of sample means
plt.hist(means, bins=30, alpha=0.7)
plt.title('Distribution of Sample Means (CLT)')
plt.show()
```

## [Gotchas]

- ⚠️ Mean is sensitive to outliers; consider median for skewed data.
- ⚠️ Standard deviation assumes normality; use variance for non-normal distributions.

## [Mental model]

1. **Mean, Median, Mode**: Measures of central tendency. Mean is affected by outliers, median is not.
2. **Variance vs. Std Dev**: Variance gives a squared measure of spread; std dev is in the same units as data.
3. **CLT**: Regardless of population distribution, the distribution of sample means approaches normality as sample size increases.
```