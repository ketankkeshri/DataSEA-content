```markdown
# GitHub Actions for dbt/Python — Cheatsheet

## [Section 1: Core syntax]

| Thing                | Syntax                       | Notes                                              |
|---------------------|------------------------------|----------------------------------------------------|
| Define a job        | `job: <job_name>`            | A job is a set of steps that execute in a workflow.  |
| Set up dbt          | `uses: dbt-labs/dbt-action@v1` | Use this action to run dbt commands in CI.       |
| Run tests           | `run: dbt test`              | Execute dbt tests to ensure data quality.          |
| Cache dependencies   | `paths: .dbt/target`         | Cache dbt compiled artifacts to speed up runs.     |
| Secrets management   | `secrets: ${{ secrets.SECRET_NAME }}` | Access secrets stored in GitHub for use in workflows. |

## [Section 2: Common operations]

```yaml
name: dbt CI

on: [push, pull_request]

jobs:
  dbt:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install dbt
        run: pip install dbt

      - name: Run dbt tests
        run: dbt test

      - name: Run dbt CI
        run: dbt ci
```

## [Gotchas]

- ⚠️ Ensure your dbt profile is correctly configured in the repository for CI to access.
- ⚠️ Watch out for dependency conflicts when installing dbt packages in Python.

## [Mental model]

- **Workflow**: A collection of jobs.
- **Job**: A sequence of steps.
- **Step**: An action or command within a job.
- **Action**: Reusable commands that can be shared across workflows.
```