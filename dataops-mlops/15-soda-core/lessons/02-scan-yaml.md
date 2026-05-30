# Scan Yaml

Data quality is a cornerstone of successful data operations. In this lesson, we'll dive into the `scan.yaml` file used by Soda Core to define and manage data quality checks, ensuring your data pipelines are robust and reliable.

## Understanding the `scan.yaml` Structure

The `scan.yaml` file is where you define the metrics and checks for your datasets. This file is essential for monitoring quality and understanding the state of your data.

Here's a basic example of what a `scan.yaml` file might look like:

```yaml
data_sources:
  my_database:
    type: postgres
    connection:
      host: localhost
      port: 5432
      user: my_user
      password: my_password
      database: my_db

checks:
  - name: "Check for nulls in user_id"
    sql: |
      SELECT COUNT(*) AS null_count
      FROM users
      WHERE user_id IS NULL

  - name: "Check user registration date is in the past"
    sql: |
      SELECT COUNT(*) AS future_registrations
      FROM users
      WHERE registration_date > NOW()
```

### Key Components of the `scan.yaml`

1. **Data Sources**: This section defines the databases or data stores you are monitoring. Each source has a type and connection details.
2. **Checks**: Each check consists of a name and an SQL query that returns a count of records that violate a condition. You can set up multiple checks for different data quality metrics.

## Implementing and Running Your Scans

Once your `scan.yaml` file is ready, you can run the scans through the Soda CLI. Here's how to execute your defined checks:

```bash
soda scan scan.yaml
```

This command will connect to your defined data source, run the checks specified in your YAML file, and return the results. You can easily integrate this command into your CI/CD pipeline to automate data quality checks.

### Configuring Alerts and Notifications

To keep your team informed, consider setting up alerts based on the results of your scans. Soda Core enables you to configure alerts when quality checks fail. This can be done by adding an `alerts` section in your YAML file:

```yaml
alerts:
  - name: "Notify on nulls in user_id"
    conditions:
      - check: "Check for nulls in user_id"
        threshold: 0
```

This configuration ensures that if the `null_count` exceeds the threshold, an alert is triggered, allowing your team to respond quickly.

## Common pitfalls

- **Incorrect Connection Details**: Double-check your database connection settings. A wrong password or host can lead to failed scans.
- **SQL Errors**: Ensure your SQL queries are valid and test them independently. Syntax errors can prevent checks from running.
- **Overlooking Edge Cases**: Consider edge cases in your data, such as time zones in date fields, which could lead to false negatives in checks.

## In a nutshell

- `scan.yaml` defines your data quality checks and sources.
- Use the Soda CLI to run scans based on this configuration.
- Configure alerts for critical checks to maintain data quality.
- Validate SQL queries to avoid runtime errors.
- Stay aware of edge cases in your datasets that can affect quality checks.