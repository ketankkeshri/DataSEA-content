# Stationarity

Understanding stationarity is crucial for effective time series analysis. A stationary time series has statistical properties that do not change over time, which is a key assumption for many forecasting models. If your data isn't stationary, your predictions can be wildly off—so let’s dive in!

## What is Stationarity?

Stationarity means that the statistical properties of a time series, such as the mean, variance, and autocorrelation, are constant over time. There are two primary types of stationarity:

- **Strict Stationarity**: All statistical properties remain constant, regardless of the time period.
- **Weak Stationarity**: Only the mean and variance are constant, and the autocovariance depends only on the time lag, not on the actual time.

Most time series forecasting models, like ARIMA, assume that the series is at least weakly stationary. If your data isn’t stationary, you’ll need to transform it before applying these models.

## How to Check for Stationarity

There are several methods to check if your time series data is stationary:

1. **Visual Inspection**: Plot the time series and look for trends or seasonal patterns.
2. **Summary Statistics**: Split the time series into segments and compare the means and variances.
3. **Statistical Tests**: Use tests like the Augmented Dickey-Fuller (ADF) test to statistically confirm stationarity.

Here's how to implement the ADF test in Python using the `statsmodels` library:

```python
import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Sample time series data
data = {
    'date': pd.date_range(start='2020-01-01', periods=100, freq='D'),
    'value': [i + (i * 0.1) for i in range(100)]  # Non-stationary trend
}
df = pd.DataFrame(data)
df.set_index('date', inplace=True)

# ADF test
result = adfuller(df['value'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])

if result[1] < 0.05:
    print("The series is stationary")
else:
    print("The series is non-stationary")
```

## Making a Time Series Stationary

If your series is non-stationary, you can apply several techniques to make it stationary:

1. **Differencing**: Subtract the previous observation from the current observation. This can help eliminate trends.
   ```python
   df['diff'] = df['value'].diff().dropna()
   ```

2. **Transformation**: Apply transformations like logarithmic or square root to stabilize variance.
   ```python
   df['log_value'] = np.log(df['value'])
   ```

3. **Seasonal Decomposition**: Decompose the series into trend, seasonal, and residual components.
   ```python
   from statsmodels.tsa.seasonal import seasonal_decompose

   decomposition = seasonal_decompose(df['value'], model='additive')
   decomposition.plot()
   ```

## Common pitfalls

- **Ignoring Non-Stationarity**: Trying to fit a model on non-stationary data can lead to misleading results.
- **Over-Differencing**: Differencing too many times can lead to loss of information and introduce noise.
- **Not Checking Assumptions**: Always validate your transformations with stationarity tests after applying them.

## In a nutshell

- Stationarity is crucial for accurate time series forecasting.
- Check for stationarity using visual inspection, summary statistics, and ADF tests.
- Apply techniques like differencing, transformations, and seasonal decompositions to achieve stationarity.
- Ensure you validate your data after transformations to maintain the integrity of your analysis.