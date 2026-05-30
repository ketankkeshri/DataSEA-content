```markdown
# A/B Testing Frameworks — Cheatsheet

## [Section 1: Design Principles]

| Thing                   | Syntax                                   | Notes                                       |
|-------------------------|------------------------------------------|---------------------------------------------|
| Hypothesis               | `H0: ...` (Null) <br> `H1: ...` (Alternative) | Clearly define what you're testing.        |
| Test Types              | `A/B` <br> `A/A` <br> `Multi-variate`   | Choose based on complexity of tests.      |
| Randomization           | `random.sample()`                        | Ensure random selection of participants.   |

## [Section 2: Sample Size Calculation]

```python
import statsmodels.api as sm

# Calculate sample size for A/B test
def calculate_sample_size(alpha, power, p1, p2):
    return sm.stats.proportions_ztest([p1, p2], [n1, n2])

# Example usage
alpha = 0.05  # significance level
power = 0.8   # desired power
p1 = 0.1     # conversion rate for group A
p2 = 0.2     # conversion rate for group B
sample_size = calculate_sample_size(alpha, power, p1, p2)
```

## [Sequential Testing]

| Concept                | Description                               |
|------------------------|-------------------------------------------|
| Definition             | Test sequences without increasing alpha.  |
| Method                 | Use `Sequential Analysis` techniques.    |
| Tools                  | Libraries like `bayesian` or `pyMC3`.   |

## [Gotchas]

- ⚠️ Ensure your sample sizes are large enough to be statistically significant.
- ⚠️ Avoid peeking at results before the test completes; it biases outcomes.

## [Mental model]

1. **Test Design:**
   - Define clear hypotheses.
   - Choose the right test type.
   - Randomize participants.

2. **Sample Size:**
   - Use statistical methods for accurate estimates.
   - Account for expected conversion rates.

3. **Execution:**
   - Follow sequential testing rules.
   - Analyze results with a focus on significance and power.
```