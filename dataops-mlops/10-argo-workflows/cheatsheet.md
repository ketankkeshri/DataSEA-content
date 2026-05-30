```markdown
# Argo Workflows — Cheatsheet

## [Section 1: Core syntax]

| Thing                 | Syntax                                                                 | Notes                                      |
|-----------------------|------------------------------------------------------------------------|--------------------------------------------|
| Workflow Definition    | `apiVersion: argoproj.io/v1alpha1`                                   | Kubernetes resource for workflows          |
| Workflow Kind          | `kind: Workflow`                                                      | Specifies the type of resource             |
| Entry Point            | `entrypoint: <workflow-name>`                                         | The main workflow to execute                |
| DAG Template           | `templates:`                                                          | Defines the structure of the workflow      |
| Step                   | `- name: <step-name>`                                                | A single task in the workflow              |
| Parameter              | `arguments:`                                                         | Pass parameters to templates                |

## [Section 2: Common operations]

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: example-workflow-
spec:
  entrypoint: main
  templates:
    - name: main
      dag:
        tasks:
          - name: task1
            template: script
          - name: task2
            template: script
            dependencies: [task1]
    - name: script
      script:
        image: python:3.9
        command: [python]
        source: |
          print("Hello, World!")
```

## [Parameters and Artifacts]

| Parameter      | Syntax                                      | Notes                         |
|----------------|---------------------------------------------|-------------------------------|
| Define          | `inputs:`                                  | Parameters and artifacts      |
| Artifact Input  | `artifacts:`                               | Specify input artifacts       |
| Parameter Value  | `- name: <param-name> value: <value>`    | Setting parameter values      |

## [Retries]

| Setting           | Syntax                               | Notes                               |
|-------------------|--------------------------------------|-------------------------------------|
| Retry Strategy    | `retries: <number>`                  | Number of retries for a task       |
| Retry Delay       | `retryStrategy: {limit: <number>}`  | Configure retry behavior            |

## [Gotchas]

- ⚠️ Ensure all task dependencies are defined; otherwise, tasks may run out of order.
- ⚠️ Parameters and artifacts must match the defined workflow structure to avoid runtime errors.

## [Mental model]

- **DAG Structure**: Each task must explicitly define dependencies.
- **Parameters**: Use to pass data between tasks.
- **Retries**: Handle transient failures gracefully by defining retry policies.
```