# Templating

Helm templating allows you to customize Kubernetes applications dynamically, making deployments more flexible and manageable. Understanding how to use templates effectively is crucial for Data Engineers and Data Scientists working with data-driven applications.

## What is Helm Templating?

Helm templates are the backbone of Helm charts, enabling you to define Kubernetes resources in a reusable and customizable way. Instead of hardcoding values, you can use templates to parameterize your configurations. This means you can deploy the same application with different settings across multiple environments (development, testing, production).

Here's a simple example of a template for a Deployment resource:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-app
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ .Release.Name }}-app
  template:
    metadata:
      labels:
        app: {{ .Release.Name }}-app
    spec:
      containers:
        - name: {{ .Release.Name }}-container
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - containerPort: {{ .Values.containerPort }}
```

In this template:
- `{{ .Release.Name }}` pulls the release name from the Helm release context.
- `{{ .Values.* }}` accesses values defined in the `values.yaml` file.

## Using Values in Templates

Values are defined in the `values.yaml` file and can be referenced in your templates. This separation allows you to change configurations without altering the templates themselves. For instance, your `values.yaml` might look like this:

```yaml
replicaCount: 3
image:
  repository: my-app
  tag: latest
containerPort: 8080
```

When you deploy your chart with:

```bash
helm install my-release ./my-chart
```

Helm will replace the placeholders in your template with the values from `values.yaml`, resulting in a fully configured Kubernetes resource.

### Template Functions

Helm supports functions that can be used within templates to manipulate data. Here are a few common functions:

- `quote`: Wraps a string in double quotes.
- `toJson`: Converts a value to a JSON string.
- `default`: Provides a default value if the variable is not set.

Example usage:

```yaml
image: {{ .Values.image.repository | quote }}:{{ .Values.image.tag | default "latest" }}
```

## Common pitfalls

- **Missing values**: If a value is not defined in `values.yaml`, Helm will throw an error. Always ensure your required values are set.
- **Incorrect indentation**: YAML is sensitive to whitespace. Ensure consistent indentation in your templates to avoid deployment failures.
- **Overusing templates**: While templating is powerful, excessive complexity can lead to hard-to-read templates. Keep it simple and maintainable.

## In a nutshell

- Helm templating allows dynamic configuration of Kubernetes resources.
- Use `values.yaml` for separating configuration from templates.
- Leverage built-in functions for data manipulation in templates.
- Watch out for missing values and indentation issues.
- Keep templates simple and readable for better maintainability.