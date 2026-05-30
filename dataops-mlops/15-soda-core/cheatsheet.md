```markdown
# Soda Core for Data Quality — Cheatsheet

## [Section 1: DataOps + MLOps Core Commands]

| Thing            | Syntax                       | Notes                                    |
|------------------|------------------------------|------------------------------------------|
| Scan YAML config | `soda scan --yaml <file>`    | Scans data based on the specified YAML. |
| Run CLI checks    | `soda check <check_name>`    | Executes a specific data quality check. |
| List checks       | `soda list checks`           | Displays all available checks in the project. |
| CI integration     | `soda ci <command>`          | Integrates with CI tools; specify the command. |

## [Section 2: Common Operations]

```bash
# Scan a YAML file for data quality checks
soda scan --yaml data_quality_checks.yaml

# Run a specific data quality check
soda check my_data_quality_check

# Integrate with CI/CD pipelines
soda ci run
```

## [Gotchas]

- ⚠️ Ensure your YAML file follows the correct structure; otherwise, errors will occur during scanning.
- ⚠️ Running checks without specifying the environment can lead to unexpected results; always confirm your environment settings.

## [Mental model]

- **Data Quality Checks:** Define and automate checks in YAML.
- **Scanning Process:** Scans defined checks against data sources.
- **CI Integration:** Automates checks in pipeline for continuous quality assurance.
```