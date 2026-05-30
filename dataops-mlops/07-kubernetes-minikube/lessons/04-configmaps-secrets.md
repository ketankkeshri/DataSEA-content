# Configmaps Secrets

Managing configuration and sensitive information in Kubernetes is crucial for maintaining the security and flexibility of your applications. ConfigMaps and Secrets allow you to decouple configuration artifacts from container images, making deployments much more streamlined and secure.

## Understanding ConfigMaps

ConfigMaps are used to store non-sensitive configuration data in key-value pairs. They can be consumed in various ways, such as environment variables or mounted as files in a pod.

### Creating a ConfigMap

Here's a practical example of creating a ConfigMap for a web application that stores database configuration:

```bash
kubectl create configmap db-config \
  --from-literal=DATABASE_URL=postgres://user:password@localhost:5432/mydb \
  --from-literal=DATABASE_PORT=5432
```

This command creates a ConfigMap named `db-config` with two key-value pairs. You can verify its creation with:

```bash
kubectl get configmaps
```

### Using a ConfigMap in a Pod

To use the ConfigMap in a pod, reference it in your pod's YAML file:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-app
spec:
  containers:
    - name: app
      image: my-web-app:latest
      env:
        - name: DATABASE_URL
          valueFrom:
            configMapKeyRef:
              name: db-config
              key: DATABASE_URL
        - name: DATABASE_PORT
          valueFrom:
            configMapKeyRef:
              name: db-config
              key: DATABASE_PORT
```

This setup injects the database configuration as environment variables into the application container.

## Understanding Secrets

Secrets are similar to ConfigMaps but are specifically designed to hold sensitive information, such as passwords, OAuth tokens, and SSH keys. Secrets are base64-encoded and are treated with more security precautions.

### Creating a Secret

Here's how to create a Secret for storing sensitive credentials:

```bash
kubectl create secret generic db-credentials \
  --from-literal=username=admin \
  --from-literal=password=supersecretpassword
```

You can view your secrets with:

```bash
kubectl get secrets
```

### Using a Secret in a Pod

To use a Secret in your pod configuration, you can again reference it in the YAML file:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-app
spec:
  containers:
    - name: secure-app-container
      image: my-secure-app:latest
      env:
        - name: DB_USERNAME
          valueFrom:
            secretKeyRef:
              name: db-credentials
              key: username
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-credentials
              key: password
```

This configuration injects the database username and password directly into the environment variables of your container.

## Common pitfalls

- **Exposing Secrets**: Avoid logging Secrets or ConfigMaps directly. Always handle sensitive data carefully to prevent leaks.
- **ConfigMap Updates**: Changing a ConfigMap does not automatically restart the pods that use it. You may need to delete and recreate the pod for changes to take effect.
- **Overusing Secrets**: Only use Secrets for data that truly needs to be secured. Storing non-sensitive data in Secrets adds unnecessary complexity.

## In a nutshell

- **ConfigMaps** are for non-sensitive configuration data, used in various ways.
- **Secrets** store sensitive information and have additional security measures.
- Always reference ConfigMaps and Secrets in your pod configuration for dynamic environment variables.
- Be cautious about exposing sensitive information and manage updates carefully.