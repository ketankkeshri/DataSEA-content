```markdown
# Probability for DS — Cheatsheet

## [Section 1: Core Concepts]

| Thing                      | Syntax                              | Notes                                      |
|----------------------------|-------------------------------------|--------------------------------------------|
| Probability of an event    | `P(A)`                              | A measure between 0 (impossible) and 1 (certain). |
| Conditional probability     | `P(A | B)`                         | Probability of A given B has occurred.    |
| Bayes' theorem             | `P(A | B) = (P(B | A) * P(A)) / P(B)` | Updates probability based on new evidence. |
| Expected value             | `E(X) = Σ [x * P(x)]`             | Mean of a random variable.                 |
| Variance                   | `Var(X) = E[(X - μ)²]`            | Measure of data spread around the mean.   |
| Standard deviation         | `σ = √Var(X)`                      | Measures how spread out the numbers are.  |

## [Section 2: Common Distributions]

```python
# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Normal Distribution
mean, std_dev = 0, 1
x = np.linspace(-5, 5, 100)
pdf = stats.norm.pdf(x, mean, std_dev)
plt.plot(x, pdf, label='Normal Distribution')

# Binomial Distribution
n, p = 10, 0.5
k = np.arange(0, n+1)
binom_pmf = stats.binom.pmf(k, n, p)
plt.stem(k, binom_pmf, label='Binomial Distribution', basefmt=" ", use_line_collection=True)

# Show plot
plt.legend()
plt.title("Common Distributions")
plt.xlabel("X-axis")
plt.ylabel("Probability")
plt.show()
```

## [Gotchas]

- ⚠️ Confusing conditional probability with joint probability. Remember, `P(A | B) ≠ P(A and B)`.
- ⚠️ Misapplying Bayes' theorem without correctly identifying prior probabilities can lead to errors.

## [Mental model]

- **Probability Basics:** 
  - 0 = Impossible | 1 = Certain
  - Events can be independent or dependent.
  
- **Bayes' Theorem:** 
  - Prior knowledge influences new data.
  - Formula updates belief based on evidence.
  
- **Distributions:**
  - Normal: Bell curve, symmetric around the mean.
  - Binomial: Discrete outcomes, fixed number of trials.
```