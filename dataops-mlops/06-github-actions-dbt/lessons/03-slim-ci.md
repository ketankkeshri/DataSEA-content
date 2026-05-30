# Slim CI

Continuous Integration (CI) doesn't have to be bulky. In this lesson, we’ll explore how to slim down your CI/CD pipeline using GitHub Actions with dbt and Python. A lean CI process means faster feedback loops, less compute time, and ultimately, a smoother workflow for data engineers and analysts.

## Understanding Slim CI

Slim CI focuses on optimizing your CI pipeline by executing only the necessary jobs based on the changes made in your repository. Instead of running a full suite of tests and builds for every push, you can create conditional workflows that only trigger specific actions when relevant files change. This is especially useful in dbt projects where not every change necessitates a full rebuild.

### Conditional Workflows

To implement Slim CI, start by defining your jobs in the GitHub Actions workflow file. Here’s a basic example that demonstrates how to set up conditional jobs:

```yaml
name: Slim CI

on:
  push:
    paths:
      - 'models/**'
      - 'dbt_project.yml'

jobs:
  test:
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
          pip install dbt
          pip install -r requirements.txt

      - name: Run dbt tests
        run: dbt test --models my_model
```

In this example, the workflow is triggered only when changes are made to files within the `models` directory or the `dbt_project.yml` file. This way, you avoid unnecessary runs for changes in other parts of the repository.

## Performance Optimization

Besides using conditional workflows, there are other strategies to slim your CI. Here are a few:

### Caching Dependencies

Caching can greatly reduce the time spent on installing dependencies. You can utilize GitHub Actions' caching capabilities as follows:

```yaml
      - name: Cache dbt dependencies
        uses: actions/cache@v2
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-
```

This snippet caches the Python packages installed via pip, so subsequent runs can skip the installation step if nothing has changed in your requirements.

### Parallel Jobs

If you have multiple independent jobs, consider running them in parallel. This reduces the total time taken for the CI process. Here’s a quick example:

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      # Linting steps here...

  test:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      # Testing steps here...
```

The `lint` job runs first and the `test` job runs concurrently, improving efficiency.

## Common pitfalls

- **Overusing paths:** Be careful with your `paths` configuration. If it’s too broad, you may end up triggering builds unnecessarily.
- **Ignoring caching:** Not leveraging caching can lead to longer build times. Make sure to implement it where appropriate.
- **Neglecting job dependencies:** Forgetting to set job dependencies can lead to failures when jobs that rely on previous jobs run out of order.

## In a nutshell

- Slim CI optimizes your CI process by reducing unnecessary runs.
- Use conditional workflows to trigger actions based on specific file changes.
- Implement caching to speed up dependency installation.
- Run independent jobs in parallel to cut down on total execution time.
- Always test and iterate on your CI configuration to keep it efficient.