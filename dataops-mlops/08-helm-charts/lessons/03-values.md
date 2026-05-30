# Values

Helm charts are powerful tools for managing Kubernetes applications, and values are key to customizing them for different environments. Understanding how to leverage values in your Helm charts can streamline your deployments and avoid configuration drift.

## What are Values in Helm?

In Helm, values are the dynamic configurations you use to customize your charts. They allow you to define parameters in a `values.yaml` file or pass them directly via the command line when installing or upgrading your charts. This flexibility is crucial for deploying the same application in multiple environments (like development, staging, and production) without hardcoding values.

### Defining Values

You typically define your values in a `values.yaml` file within your Helm chart:

```yaml
replicaCount: 3

image:
  repository: myapp
  tag: latest
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

resources:
  limits:
    cpu: "500m"
    memory: "128Mi"
  requests:
    cpu: "250m"
    memory: "64Mi"
```

In this example, you can see how each setting corresponds to a piece of configuration for your app. The `replicaCount`, `image`, `service`, and `resources` fields can be modified as needed when deploying the app.

## Using Values in Templates

To access these values in your templates, you use the Helm template syntax. For instance, in your deployment template, you might have:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: {{ .Values.image.repository }}:{{ .Values.image.tag }}
          ports:
            - containerPort: {{ .Values.service.port }}
```

Here, Helm replaces the placeholders with the corresponding values from `values.yaml`. This maintains a clean separation between your configuration and your code, making it easier to manage changes.

### Overriding Values

You can override values at install time using the `--set` flag:

```bash
helm install myapp ./mychart --set replicaCount=5 --set image.tag=v1.0.1
```

This command sets the `replicaCount` to 5 and changes the image tag to `v1.0.1`, allowing you to make environment-specific adjustments quickly.

## Common pitfalls

- **Hardcoding Values:** Avoid hardcoding values directly in your templates. Always use values from `values.yaml` or the command line to ensure flexibility.
- **Not Using Default Values:** If you don’t define defaults in `values.yaml`, users of your chart may struggle to figure out necessary configurations.
- **Ignoring Type Validation:** Helm doesn’t enforce types on values; ensure you validate the types in your templates to prevent runtime errors.

## In a nutshell

- Values in Helm allow dynamic configuration for deployments.
- Use `values.yaml` for defaults and the `--set` flag to override them.
- Access values in templates using the Helm template syntax.
- Avoid hardcoding and ensure proper validation to prevent issues.