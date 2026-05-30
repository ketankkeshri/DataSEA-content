```markdown
# Time Series Forecasting — Cheatsheet

## [Core Concepts]

| Concept         | Description                                          |
|-----------------|------------------------------------------------------|
| Stationarity    | A time series is stationary if its statistical properties do not change over time.   |
| ARIMA           | AutoRegressive Integrated Moving Average, used for forecasting stationary time series. |
| Prophet         | A tool by Facebook for forecasting time series data that may have seasonal effects.   |
| Deep Learning TS| Leveraging neural networks to model time series data. |

## [Key Terms]

| Term            | Definition                                          |
|-----------------|-----------------------------------------------------|
| Trend           | Long-term movement in the data over time.          |
| Seasonality     | Regular pattern of fluctuations in the data.       |
| Autocorrelation  | Correlation of a signal with a delayed copy of itself. |

## [Common Operations]

```python
# Stationarity Check
from statsmodels.tsa.stattools import adfuller

result = adfuller(time_series_data)
print('ADF Statistic:', result[0])
print('p-value:', result[1])

# ARIMA Model
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(time_series_data, order=(p, d, q))
model_fit = model.fit()
forecast = model_fit.forecast(steps=10)

# Prophet Model
from fbprophet import Prophet
import pandas as pd

df = pd.DataFrame({'ds': date_list, 'y': value_list})
model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=10)
forecast = model.predict(future)

# Deep Learning Time Series Example (Keras)
from keras.models import Sequential
from keras.layers import LSTM, Dense

model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(n_timesteps, n_features)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=200, verbose=0)
```

## [Gotchas]

- ⚠️ Ensure your time series data is stationary before applying ARIMA; use differencing if needed.
- ⚠️ Prophet requires a specific DataFrame format: columns must be named 'ds' for dates and 'y' for values.
- ⚠️ LSTM models require careful tuning of hyperparameters and data preprocessing.

## [Mental Model]

- **ARIMA**: Combines autoregression (AR), differencing (I), and moving average (MA) for forecasts.
- **Prophet**: Uses additive or multiplicative models to capture seasonality and holidays effectively.
- **Deep Learning**: Models temporal dependencies in sequences, great for complex patterns.

```