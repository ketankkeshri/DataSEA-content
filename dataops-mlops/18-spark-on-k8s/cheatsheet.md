```markdown
# Spark on Kubernetes — Cheatsheet

## [Section 1: Core Concepts]

| Thing                      | Syntax                             | Notes                                                              |
|---------------------------|------------------------------------|--------------------------------------------------------------------|
| Spark Operator             | `spark-operator`                   | Manages Spark applications on K8s.                                |
| Application Spec           | `apiVersion: sparkoperator.k8s.io/v1beta2` | Defines a Spark application in a YAML file.                       |
| Dynamic Allocation         | `spark.dynamicAllocation.enabled` | Turns on dynamic allocation of executors.                         |
| GPU Scheduling             | `spark.kubernetes.executor.request.gpus` | Requests GPU resources for executors.                             |

## [Section 2: Common Operations]

```yaml
apiVersion: sparkoperator.k8s.io/v1beta2
kind: SparkApplication
metadata:
  name: spark-app
spec:
  type: Scala
  mode: cluster
  image: "your-docker-image"
  imagePullPolicy: Always
  mainClass: "org.example.YourMainClass"
  mainApplicationFile: "local:///opt/spark/app.jar"
  sparkConf:
    "spark.executor.instances": "5"
    "spark.dynamicAllocation.enabled": "true"
    "spark.kubernetes.executor.request.gpus": "1"
  restartPolicy:
    type: OnFailure
    onFailureRetries: 3
    onFailureRetryInterval: "10s"
```

## [Gotchas]

- ⚠️ Ensure Kubernetes has enough resources allocated for Spark workloads, especially when using dynamic allocation.
- ⚠️ GPU scheduling may require specific driver installation on the nodes; verify compatibility first.

## [Mental model]

- **Kubernetes** manages the cluster.
- **Spark Operator** handles Spark application lifecycle.
- **Dynamic Allocation** adjusts resources based on load.
```