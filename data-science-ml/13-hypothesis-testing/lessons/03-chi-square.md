# Chi Square

Chi-square tests are essential for understanding relationships between categorical variables. Whether you're looking at survey results or analyzing customer behavior, mastering chi-square can help you make data-driven decisions.

## What is the Chi-Square Test?

The chi-square test assesses whether there's a significant association between two categorical variables. It compares the observed frequencies in each category to the frequencies we would expect if there were no association between the variables.

### Chi-Square Test Formula

The formula for the chi-square statistic (χ²) is:

```math
χ² = Σ ( (O - E)² / E )
```

Where:
- **O** = Observed frequency
- **E** = Expected frequency

### Example Use Case

Imagine you're analyzing customer preferences for a new product feature based on age groups. You have data on 100 customers across three age groups (18-25, 26-35, 36-45) and their feedback on the feature being "liked" or "not liked."

Here's how your data might look:

| Age Group | Liked | Not Liked |
|-----------|-------|-----------|
| 18-25     | 20    | 10        |
| 26-35     | 30    | 20        |
| 36-45     | 10    | 10        |

To perform the chi-square test, first calculate the expected frequencies based on the overall proportions.

## Performing the Chi-Square Test in Python

Let's run a chi-square test using Python's `scipy` library. First, install the library if you haven't already:

```bash
pip install scipy
```

Now, here's how you can perform the test:

```python
import numpy as np
from scipy.stats import chi2_contingency

# Observed data
observed = np.array([[20, 10], [30, 20], [10, 10]])

# Perform the chi-square test
chi2, p, dof, expected = chi2_contingency(observed)

print(f"Chi-square Statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of Freedom: {dof}")
print(f"Expected Frequencies:\n{expected}")
```

### Interpreting the Results

- **Chi-square Statistic:** Indicates how much the observed frequencies deviate from expected frequencies.
- **P-value:** Helps determine the significance. A common threshold is 0.05:
  - If **p < 0.05**, reject the null hypothesis (there's an association).
  - If **p ≥ 0.05**, don't reject the null hypothesis (no association).

## Common pitfalls

- Using chi-square tests with small sample sizes can lead to misleading results. Ensure each expected frequency is at least 5.
- Categorical variables should be mutually exclusive and collectively exhaustive. Mixing categories can distort results.
- Forgetting to check for independence can lead to incorrect conclusions. Always validate your assumptions.

## In a nutshell

- The chi-square test evaluates associations between categorical variables.
- Use the formula: χ² = Σ ( (O - E)² / E ).
- Python's `scipy.stats` library makes it easy to perform the test.
- Check assumptions: sample size and category exclusivity.
- Interpret p-values carefully to make data-driven decisions.