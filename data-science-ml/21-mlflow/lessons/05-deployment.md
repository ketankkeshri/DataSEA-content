# Deployment

Deploying machine learning models is a crucial step in the ML lifecycle. It transforms your model from a research artifact into a production-ready application that can deliver value. Understanding how to efficiently deploy models with MLflow can streamline this process and ensure that your models are both reliable and scalable.

## Understanding MLflow Deployment

MLflow provides several deployment options, including local deployment, cloud deployment, and deployment to platforms like Docker and Kubernetes. Each deployment strategy has its use cases, depending on your organization’s infrastructure and requirements.

### Local Deployment

You can deploy models locally for testing and development. This is useful for quick iterations and debugging.

```python
import mlflow
import mlflow.pyfunc

# Load model
model = mlflow.pyfunc.load_model("models:/MyModel/1")

# Create a simple prediction
input_data = {"feature1": [1], "feature2": [2]}
predictions = model.predict(input_data)
print(predictions)
```

### Cloud Deployment

For production, deploying models to cloud services like AWS SageMaker or Azure ML can provide scalability and reliability.

```bash
# Example command to deploy to AWS SageMaker
mlflow sagemaker deploy \
    --model-uri models:/MyModel/1 \
    --region us-west-2 \
    --instance-type ml.m5.large \
    --endpoint-name my-endpoint
```

### Containerized Deployment

Using Docker, you can create a portable container for your model, making it easier to deploy across different environments.

```dockerfile
# Dockerfile example
FROM python:3.8-slim

COPY ./model /model
RUN pip install mlflow

ENTRYPOINT ["mlflow", "models", "serve", "-m", "/model", "--port", "5000"]
```

## Model Serving

Once deployed, model serving is the next step. MLflow allows you to serve your model as a REST API, enabling other applications to interact with it seamlessly.

```bash
mlflow models serve -m models:/MyModel/1 --port 5000
```

You can then send requests to this endpoint to get predictions:

```bash
curl -X POST -H "Content-Type: application/json" \
    --data '{"columns":["feature1", "feature2"], "data":[[1, 2]]}' \
    http://localhost:5000/invocations
```

## Common pitfalls

- **Ignoring Model Versioning:** Always keep track of model versions when deploying. Forgetting this can lead to inconsistencies and unexpected behaviors.
- **Insufficient Monitoring:** Failing to monitor the deployed model can lead to degradation in performance over time. Implement monitoring to catch issues early.
- **Hardcoding Environment Variables:** Avoid hardcoding sensitive information in your deployment scripts. Use environment variables or configuration files instead.

## In a nutshell

- MLflow supports various deployment options: local, cloud, and containerized.
- Use model serving to expose your model as a REST API.
- Pay attention to versioning and monitoring to ensure successful deployments.