```markdown
# CI Pipelines Intro — Cheatsheet

## [Section 1: DataOps + MLOps Overview]

| Concept        | Description                             | Key Tools             |
|----------------|-----------------------------------------|-----------------------|
| DataOps        | Practice of integrating data engineering and operations to improve data quality and accessibility. | Apache Airflow, dbt   |
| MLOps          | Collaboration between data scientists and operations to automate ML workflows. | MLflow, Kubeflow      |
| CI/CD          | Continuous Integration / Continuous Deployment; automates code integration and deployment. | GitHub Actions, GitLab CI |

## [Section 2: GitHub Actions Basics]

```yaml
name: CI Pipeline

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest
```

## [Section 3: GitLab CI Basics]

```yaml
stages:
  - build
  - test

build-job:
  stage: build
  script:
    - echo "Building the project..."

test-job:
  stage: test
  script:
    - echo "Running tests..."
    - pytest
```

## [Section 4: Common Patterns]

- **Sequential Jobs**: Define jobs to run one after another.
- **Parallel Jobs**: Use multiple jobs to run tasks simultaneously.
- **Conditional Execution**: Use `if` conditions to run jobs based on the outcome of previous jobs.

## [Gotchas]

- ⚠️ Ensure workflows are triggered correctly; check `on` conditions.
- ⚠️ Be aware of secrets management; use GitHub Secrets or GitLab CI/CD variables.

## [Mental model]

1. **CI/CD Pipeline**: Code → Build → Test → Deploy
2. **Automation**: Reduces manual effort and increases reliability.
3. **Feedback Loop**: Immediate feedback on code changes for faster iterations.
```