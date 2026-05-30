# Common Distributions

Understanding probability distributions is crucial for data scientists and machine learning practitioners. They help us model uncertainty and make informed decisions based on data. Let's dive into some of the most common distributions you'll encounter in your data journey.

## Key Probability Distributions

### Normal Distribution

The normal distribution, often called the Gaussian distribution, is a bell-shaped curve that describes how the values of a variable are distributed. It’s characterized by its mean (μ) and standard deviation (σ).

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Parameters
mu, sigma = 0, 0.1  # mean and standard deviation

# Generate data
data = np.random.normal(mu, sigma, 1000)

# Plot
sns.histplot(data, bins=30, kde=True)
plt.title('Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
```

### Binomial Distribution

The binomial distribution models the number of successes in a fixed number of independent Bernoulli trials (like flipping a coin). It’s defined by the number of trials (n) and the probability of success (p).

```python
from scipy.stats import binom

n = 10  # number of trials
p = 0.5  # probability of success
x = np.arange(0, n+1)

# Binomial PMF
pmf = binom.pmf(x, n, p)

# Plot
plt.bar(x, pmf)
plt.title('Binomial Distribution PMF')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.xticks(x)
plt.show()
```

### Poisson Distribution

The Poisson distribution is used for modeling the number of events occurring in a fixed interval of time or space. It’s characterized by the average number of events (λ).

```python
from scipy.stats import poisson

lambda_ = 3  # average rate (events per interval)
x = np.arange(0, 10)

# Poisson PMF
pmf = poisson.pmf(x, lambda_)

# Plot
plt.bar(x, pmf)
plt.title('Poisson Distribution PMF')
plt.xlabel('Number of Events')
plt.ylabel('Probability')
plt.xticks(x)
plt.show()
```

## When to Use Which Distribution

- **Normal Distribution**: Use when your data is continuous and bell-shaped.
- **Binomial Distribution**: Use for discrete data representing success/failure over a fixed number of trials.
- **Poisson Distribution**: Use for rare events occurring over a specified interval or area.

## Common pitfalls

- **Ignoring Assumptions**: Each distribution has assumptions (e.g., normality for the normal distribution). Violating them can lead to incorrect conclusions.
- **Overfitting Models**: Using too many parameters with distributions can lead to overfitting, especially with small datasets.
- **Misinterpreting Results**: Always check your distribution fit. Just because data looks bell-shaped doesn’t mean it’s normally distributed.

## In a nutshell

- **Normal Distribution**: Bell-shaped, used for continuous data.
- **Binomial Distribution**: Models number of successes in trials.
- **Poisson Distribution**: Models rare events over intervals.
- Choose the right distribution for your data to avoid misleading results.