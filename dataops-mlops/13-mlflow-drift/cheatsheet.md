```markdown
# MLflow + Drift Tracking — Cheatsheet

## [Section 1: MLflow Basics]

| Thing                     | Syntax                              | Notes                                         |
|---------------------------|-------------------------------------|-----------------------------------------------|
| Start MLflow server       | `mlflow ui`                         | Runs the MLflow UI on `localhost:5000`.      |
| Log parameters             | `mlflow.log_param("key", value)`  | Logs a parameter under the current run.      |
| Log metrics                | `mlflow.log_metric("key", value)` | Logs a metric under the current run.         |
| Log model                  | `mlflow.sklearn.log_model(model, "model_name")` | Logs a scikit-learn model. |

## [Section 2: Drift Tracking]

### Data Drift vs. Concept Drift

| Drift Type       | Definition                                              | Detection Method                                      |
|------------------|--------------------------------------------------------|------------------------------------------------------|
| Data Drift       | Change in input data distribution.                     | Statistical tests (e.g., Kolmogorov-Smirnov test).  |
| Concept Drift    | Change in the relationship between input data and target variable. | Performance monitoring and comparison.               |

### Evidently Integration

```python
import evidently
from evidently.report import Report

# Create a report
report = Report(metrics=[
    "data_drift",
    "target_drift"
])

# Generate the report
report.run(reference_data=reference_df, current_data=current_df)
report.save_html("drift_report.html")
```

### Alerting Setup

```python
import mlflow
from mlflow.tracking import MlflowClient

client = MlflowClient()

# Example of setting an alert
def set_alert(run_id, condition):
    alert_message = f"Alert: Drift detected for run {run_id}"
    if condition:  # Replace with actual drift condition
        send_alert(alert_message)

set_alert("your_run_id", drift_detected)
```

## [Gotchas]

- ⚠️ Ensure your data schema is consistent to avoid false positives in drift detection.
- ⚠️ Monitor model performance continuously; drift may not always be evident immediately.

## [Mental model]

- **Data Drift:**
  - Changes in feature distributions.
  - Detected via statistical tests.
  - Can affect model predictions.

- **Concept Drift:**
  - Changes in target variable relationships.
  - Detected through performance drops.
  - Requires retraining or model updates.

- **Evidently:**
  - Tool for monitoring drift.
  - Generates detailed reports.
  - Integrates easily with MLflow.
```