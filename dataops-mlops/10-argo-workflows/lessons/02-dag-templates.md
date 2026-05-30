# Dag Templates

Dag templates in Argo Workflows streamline the process of creating reusable workflows, making it easier to manage complex data pipelines. Whether you're orchestrating machine learning models or automating data processing, templates help you maintain consistency and reduce redundancy across your workflows.

## Understanding Dag Templates

Dag (Directed Acyclic Graph) templates allow you to define and reuse workflow structures in Argo. Instead of rewriting the same workflow for different scenarios, you can create a base template that captures common functionality and parameters.

### Creating a Basic Dag Template

Here's a simple example of a Dag template that processes data:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: data-processing-
spec:
  entrypoint: data-pipeline
  templates:
    - name: data-pipeline
      dag:
        tasks:
          - name: extract
            template: extract-template
          - name: transform
            template: transform-template
            dependencies: 
              - extract
          - name: load
            template: load-template
            dependencies: 
              - transform

    - name: extract-template
      container:
        image: my-extract-image
        command: ["python", "extract.py"]

    - name: transform-template
      container:
        image: my-transform-image
        command: ["python", "transform.py"]

    - name: load-template
      container:
        image: my-load-image
        command: ["python", "load.py"]
```

This example defines a simple ETL pipeline where tasks are executed in a specific order. Each task references a separate template for extraction, transformation, and loading data.

## Using Parameters in Dag Templates

Parameters allow you to customize the behavior of your templates. You can pass different values to your tasks without changing the workflow structure. Here's how you can modify the previous example to include parameters:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: data-processing-
spec:
  entrypoint: data-pipeline
  templates:
    - name: data-pipeline
      dag:
        tasks:
          - name: extract
            template: extract-template
            arguments:
              parameters:
                - name: data_source
                  value: "s3://my-bucket/data.csv"
          - name: transform
            template: transform-template
            dependencies: 
              - extract
            arguments:
              parameters:
                - name: transformation_type
                  value: "standardize"
          - name: load
            template: load-template
            dependencies: 
              - transform

    - name: extract-template
      inputs:
        parameters:
          - name: data_source
      container:
        image: my-extract-image
        command: ["python", "extract.py", "{{inputs.parameters.data_source}}"]

    - name: transform-template
      inputs:
        parameters:
          - name: transformation_type
      container:
        image: my-transform-image
        command: ["python", "transform.py", "{{inputs.parameters.transformation_type}}"]

    - name: load-template
      container:
        image: my-load-image
        command: ["python", "load.py"]
```

In this modified template, the `extract` and `transform` tasks accept parameters, allowing you to specify different data sources or transformation types without altering the underlying workflow structure.

## Common pitfalls

- **Ignoring Dependencies:** Make sure to define task dependencies correctly. Omitting them can lead to race conditions and failed workflows.
- **Hardcoding Values:** Avoid hardcoding values in templates. Instead, leverage parameters to enhance reusability and flexibility.
- **Overcomplicating Templates:** Keep your templates simple and focused. Complex templates can become hard to manage and debug.

## In a nutshell

- Dag templates enable reusable workflow structures in Argo Workflows.
- Parameters allow for customization without altering the workflow design.
- Proper dependency management is crucial for successful execution.
- Avoid hardcoding and complexity to maintain clarity in your workflows.
- Leverage modular design for more efficient data processing pipelines.