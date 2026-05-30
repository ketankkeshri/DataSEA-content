```markdown
# Statistical Thinking for Analysts — Cheatsheet

## Section 1: Descriptive Statistics

| Thing                | Syntax                      | Notes                                   |
|---------------------|-----------------------------|-----------------------------------------|
| Mean                | `mean(data)`                | Average of the dataset.                 |
| Median              | `median(data)`              | Middle value when data is sorted.      |
| Mode                | `mode(data)`                | Most frequently occurring value(s).     |
| Standard Deviation   | `std(data)`                 | Measure of data dispersion.             |
| Variance            | `var(data)`                 | Square of standard deviation.           |
| Quantiles           | `quantile(data, q)`        | Value below which a percentage q of data falls. |
| Interquartile Range | `iqr(data)`                 | Difference between the 75th and 25th percentiles. |

## Section 2: Common Distributions

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Normal Distribution
data = np.random.normal(loc=0, scale=1, size=1000)
sns.histplot(data, kde=True)
plt.title('Normal Distribution')
plt.show()
```

```python
# Binomial Distribution
n, p = 10, 0.5
data = np.random.binomial(n, p, 1000)
sns.histplot(data, kde=True)
plt.title('Binomial Distribution')
plt.show()
```

## Section 3: Correlation vs. Causation

| Concept                     | Definition                                         |
|-----------------------------|----------------------------------------------------|
| Correlation                | A statistical measure that indicates the extent to which two variables fluctuate together. |
| Causation                  | Indicates that one event is the result of the occurrence of another event. |
| Correlation Coefficient     | `corrcoef(x, y)` for numerical correlation values. Values close to 1 or -1 indicate strong correlation. |

## Section 4: Sampling Techniques

| Technique           | Description                                      |
|---------------------|--------------------------------------------------|
| Simple Random Sample | Every member of the population has an equal chance of selection. |
| Stratified Sample    | Population divided into subgroups; samples drawn from each. |
| Systematic Sample    | Selecting every nth member from a list.        |
| Cluster Sample       | Dividing the population into clusters and randomly selecting entire clusters. |

## Gotchas

- ⚠️ Correlation does not imply causation! Just because two variables are correlated doesn't mean one causes the other.
- ⚠️ Be cautious of outliers as they can skew statistical measures, particularly mean and standard deviation.

## Mental Model

- **Descriptive Statistics** summarize data.
- **Distributions** describe the frequency of data values.
- **Correlation** measures relationship strength; **Causation** confirms a direct influence.
```