```markdown
# MLflow Tracking — Cheatsheet

## [Section 1: Key Concepts]

| Concept       | Description                                               |
|---------------|-----------------------------------------------------------|
| Tracking URI  | Use `mlflow.set_tracking_uri("your_uri")` to set up     |
| Experiment    | Use `mlflow.create_experiment("experiment_name")`      |
| Logging       | Log parameters, metrics, and models with `mlflow.log_*`  |
| Model Registry| Manage models with `mlflow.register_model()`              |
| Deployment    | Deploy models using `mlflow.pyfunc.serve()`               |

## [Section 2: Common Operations]

```python
import mlflow

# Set tracking URI
mlflow.set_tracking_uri("http://localhost:5000")

# Create or set an experiment
mlflow.set_experiment("my_experiment")

# Start a run
with mlflow.start_run() as run:
    mlflow.log_param("param1", 5)
    mlflow.log_metric("metric1", 0.89)
    
    # Log trained model
    mlflow.sklearn.log_model(model, "model_name")

# Register a model
mlflow.register_model("runs:/{}/model_name".format(run.info.run_id), "ModelName")

# Serve the model
mlflow.pyfunc.serve(model_uri="models:/ModelName/1", host="0.0.0.0", port=5001)
```

## [Gotchas]

- ⚠️ Ensure your MLflow server is running when logging data or serving models.
- ⚠️ Model versioning is key—use `models:/ModelName/latest` for the latest version.

## [Mental model]

1. **Experiment Tracking**: Central hub for all runs and metrics.
2. **Model Registry**: Store and manage different model versions.
3. **Deployment**: Easily serve or deploy models once registered.
```