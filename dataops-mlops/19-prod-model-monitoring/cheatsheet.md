```markdown
# Production Model Monitoring — Cheatsheet

## [Section 1: DataOps + MLOps Concepts]

| Thing                     | Syntax                              | Notes                                                   |
|---------------------------|-------------------------------------|---------------------------------------------------------|
| Latency Error Budgets     | `latency_budget = target_latency + tolerance` | Define acceptable latency range for model performance.   |
| Data Drift Detection       | `monitor_data_drift(model, new_data)` | Use statistical tests to detect changes in input data distribution. |
| Shadow Deployment         | `deploy_shadow(model, request)`    | Run new model alongside the current model without affecting production. |

## [Section 2: Common Operations]

```python
# Latency Error Budget Calculation
target_latency = 100  # in ms
tolerance = 20        # in ms
latency_budget = target_latency + tolerance
print(f"Latency Budget: {latency_budget} ms")

# Data Drift Monitoring
def monitor_data_drift(model, new_data):
    # Implement statistical tests to compare distributions
    # Example: Kolmogorov-Smirnov test
    from scipy import stats
    # Assuming model's training data is available as 'train_data'
    stat, p_value = stats.ks_2samp(train_data, new_data)
    return p_value < 0.05  # indicates drift if p-value is low

# Shadow Deployment Example
def deploy_shadow(model, request):
    # Simulate request to both models
    current_response = current_model.predict(request)
    shadow_response = new_model.predict(request)
    return current_response, shadow_response
```

## [Gotchas]

- ⚠️ **Latency Budgets**: Ensure tolerance levels are realistic; overestimating can lead to degraded user experience.
- ⚠️ **Data Drift**: Not all drift indicates problems; understand business context before taking action.
- ⚠️ **Shadow Deployments**: Monitor system resources closely; can increase load on infrastructure.

## [Mental model]

- **Latency Budget**:
  - Target latency + tolerance = acceptable performance range.
  
- **Data Drift**:
  - Regular checks → Identify drift → Take action (retrain, investigate).

- **Shadow Deployment**:
  - Current model + new model → Compare outputs without user impact.
```