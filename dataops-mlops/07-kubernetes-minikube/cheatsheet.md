```markdown
# Kubernetes with Minikube — Cheatsheet

## [Section 1: Pods & Deployments]

| Thing          | Syntax                                  | Notes                                         |
|----------------|-----------------------------------------|-----------------------------------------------|
| Create a pod   | `kubectl run <pod-name> --image=<image>` | Creates a pod from a specified image.        |
| Delete a pod   | `kubectl delete pod <pod-name>`        | Deletes the specified pod.                    |
| Get pods       | `kubectl get pods`                     | Lists all pods in the current namespace.     |
| Create a deployment | `kubectl create deployment <name> --image=<image>` | Creates a deployment for scaling.   |
| Update a deployment | `kubectl set image deployment/<name> <container>=<image>` | Updates the image for a deployment. |

## [Section 2: Services]

| Thing           | Syntax                                 | Notes                                         |
|-----------------|----------------------------------------|-----------------------------------------------|
| Create a service| `kubectl expose deployment <name> --type=<type> --port=<port>` | Exposes a deployment as a service. |
| Get services    | `kubectl get services`                | Lists all services in the current namespace. |
| Delete a service| `kubectl delete service <service-name>` | Deletes the specified service.              |

## [Section 3: ConfigMaps & Secrets]

| Thing           | Syntax                                             | Notes                                         |
|-----------------|---------------------------------------------------|-----------------------------------------------|
| Create a ConfigMap | `kubectl create configmap <name> --from-literal=<key>=<value>` | Stores configuration data. |
| Get ConfigMaps  | `kubectl get configmaps`                           | Lists all ConfigMaps in the current namespace. |
| Create a Secret | `kubectl create secret generic <name> --from-literal=<key>=<value>` | Stores sensitive information. |
| Get Secrets     | `kubectl get secrets`                              | Lists all Secrets in the current namespace.  |

## [Local Cluster Tips]

```bash
# Start Minikube
minikube start

# Stop Minikube
minikube stop

# Get Minikube IP
minikube ip

# Access dashboard
minikube dashboard
```

## [Gotchas]

- ⚠️ Remember to set the correct context if you have multiple clusters: `kubectl config use-context minikube`.
- ⚠️ ConfigMaps and Secrets are namespace-scoped; ensure you’re in the right namespace (`kubectl config view --minify | grep namespace:`).

## [Mental model]

- **Pods:** Basic deployable units, can be managed through Deployments.
- **Deployments:** Manage the lifecycle of pods, enable scaling and updates.
- **Services:** Abstract access to pods, load balancing, and stable endpoints.
```