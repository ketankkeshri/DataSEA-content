```markdown
# Hypothesis Testing — Cheatsheet

## Core Concepts

| Thing               | Syntax                                         | Notes                                             |
|---------------------|------------------------------------------------|---------------------------------------------------|
| Null Hypothesis (H0)| H0: μ = μ0                                    | Assumes no effect or difference.                    |
| Alternative Hypothesis (H1)| H1: μ ≠ μ0                          | Assumes there is an effect or difference.           |
| Significance Level  | α = 0.05                                      | Common threshold for rejecting H0.                  |
| p-value             | p-value < α                                   | Indicates statistical significance.                  |

## T-Tests

### One-Sample T-Test

```python
import scipy.stats as stats

data = [20, 22, 19, 24, 30]  # Your sample data
mu = 25                      # Population mean
t_stat, p_value = stats.ttest_1samp(data, mu)

print(f"T-statistic: {t_stat}, p-value: {p_value}")
```

### Two-Sample T-Test

```python
import scipy.stats as stats

data1 = [20, 22, 19, 24, 30]  # Sample 1
data2 = [25, 30, 29, 32, 35]  # Sample 2
t_stat, p_value = stats.ttest_ind(data1, data2)

print(f"T-statistic: {t_stat}, p-value: {p_value}")
```

## Chi-Square Test

### Goodness of Fit

```python
import scipy.stats as stats

observed = [50, 30, 20]  # Observed frequencies
expected = [40, 40, 20]  # Expected frequencies
chi2_stat, p_value = stats.chisquare(observed, expected)

print(f"Chi-square statistic: {chi2_stat}, p-value: {p_value}")
```

### Test of Independence

```python
import scipy.stats as stats
import numpy as np

data = np.array([[10, 20], [20, 30]])  # Contingency table
chi2_stat, p_value, _, _ = stats.chi2_contingency(data)

print(f"Chi-square statistic: {chi2_stat}, p-value: {p_value}")
```

## Gotchas

- ⚠️ T-tests assume normality in data. Use Shapiro-Wilk test to check.
- ⚠️ Chi-square tests require expected frequency of at least 5 in each cell.
- ⚠️ P-values are not the probability that H0 is true. They only measure data's compatibility with H0.

## Mental Model

1. **Null vs. Alternative:** Always start by defining H0 and H1.
2. **Calculate Statistics:** Use the appropriate test for your data type.
3. **Decision:** Compare p-value to α; reject or fail to reject H0.
```