```markdown
# Pre-commit Hooks for Data Repos — Cheatsheet

## [Section 1: Pre-commit Hooks Overview]

| Thing             | Syntax                             | Notes                                                 |
|-------------------|------------------------------------|-------------------------------------------------------|
| Pre-commit config | `.pre-commit-config.yaml`          | YAML file to define hooks for your repo.             |
| Install hooks      | `pre-commit install`               | Set up the hooks defined in your config file.        |
| Run hooks manually | `pre-commit run --all-files`      | Test all hooks against all files in the repo.        |

## [Section 2: Common Hooks]

### SQLFluff

```yaml
-   repo: https://github.com/sqlfluff/sqlfluff
    rev: v0.11.0
    hooks:
    -   id: sqlfluff-lint
```

| Thing       | Syntax                             | Notes                                                   |
|-------------|------------------------------------|---------------------------------------------------------|
| Lint SQL    | `pre-commit run sqlfluff-lint`    | Lints SQL files for style and syntax issues.           |

### Black and Ruff

```yaml
-   repo: https://github.com/psf/black
    rev: 21.11b1
    hooks:
    -   id: black
```

```yaml
-   repo: https://github.com/charliermarsh/ruff
    rev: v0.0.145
    hooks:
    -   id: ruff
```

| Thing         | Syntax                             | Notes                                                   |
|---------------|------------------------------------|---------------------------------------------------------|
| Format Python | `pre-commit run black`             | Formats Python files according to PEP 8 standards.     |
| Lint Python   | `pre-commit run ruff`              | Runs static analysis on Python code for issues.        |

### dbt Checks

```yaml
-   repo: https://github.com/dbt-labs/dbt
    rev: 1.0.0
    hooks:
    -   id: dbt-check
```

| Thing         | Syntax                             | Notes                                                   |
|---------------|------------------------------------|---------------------------------------------------------|
| Check dbt     | `pre-commit run dbt-check`         | Validates dbt models and checks for issues.            |

## [Gotchas]

- ⚠️ Ensure the correct version of each hook is specified in the config.
- ⚠️ Hooks may fail due to local environment issues; check your setup.

## [Mental model]

- Pre-commit hooks run automatically before commits.
- Config file defines which hooks to run.
- Common hooks include SQLFluff, Black, Ruff, and dbt Checks.
```