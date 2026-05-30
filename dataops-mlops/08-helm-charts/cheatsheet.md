```markdown
# Helm Charts — Cheatsheet

## [Section 1: Core syntax]

| Thing             | Syntax                                           | Notes                                          |
|-------------------|--------------------------------------------------|------------------------------------------------|
| Chart Creation     | `helm create <chart-name>`                      | Creates a new chart with default files.       |
| Install Chart      | `helm install <release-name> <chart-name>`     | Deploys the chart to the Kubernetes cluster.  |
| Upgrade Chart      | `helm upgrade <release-name> <chart-name>`     | Upgrades the release to a new version.        |
| Rollback Chart     | `helm rollback <release-name> <revision>`      | Reverts to a previous release version.        |

## [Section 2: Templating]

```yaml
# Example template using Helm
apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}-service
spec:
  ports:
    - port: {{ .Values.service.port }}
  selector:
    app: {{ .Release.Name }}
```

## [Section 3: Values]

| Key                  | Description                                     | Default           |
|----------------------|-------------------------------------------------|-------------------|
| `service.port`       | The port on which the service will run.        | `80`              |
| `image.repository`   | The Docker image repository.                    | `nginx`           |
| `image.tag`          | The Docker image tag.                           | `latest`          |

## [Section 4: Upgrades and Rollbacks]

```bash
# Upgrade example
helm upgrade my-release my-chart --set service.port=8080

# Rollback example
helm rollback my-release 1
```

## [Gotchas]

- ⚠️ Ensure your `values.yaml` is correctly set up to avoid deployment issues.
- ⚠️ Be cautious with release names; reusing them can lead to confusion.

## [Mental model]

- Helm acts as a package manager for Kubernetes.
- Charts are packages of pre-configured Kubernetes resources.
- Templates allow you to define reusable configurations that can be customized with values.
```