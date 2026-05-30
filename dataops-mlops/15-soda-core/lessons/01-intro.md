# Intro

Data quality is crucial in any data-driven organization. In this lesson, you’ll learn about Soda Core—a tool that helps ensure your data stays clean and reliable, which is essential for effective data operations and machine learning.

## What is Soda Core?

Soda Core is an open-source framework designed for monitoring and validating data quality. It integrates seamlessly into your data pipeline, allowing you to define quality checks and automate data validation processes. This is vital for Data Engineers and Data Analysts who need to ensure that the data being used for analytics and ML models is accurate, complete, and timely.

### Key Features of Soda Core

- **Data Quality Checks:** Define checks for various data quality metrics such as uniqueness, completeness, and consistency.
- **Automated Monitoring:** Schedule checks to run at intervals or trigger them based on data ingestion events.
- **Integration with Data Tools:** Works with existing data tools and platforms, making it easy to incorporate into your workflow.

## Setting Up Soda Core

To get started with Soda Core, you need to install it and configure your first data quality checks. Here’s how:

1. **Install Soda Core**:
   ```bash
   pip install soda-core
   ```

2. **Create a YAML Configuration**: Define your data sources and checks in a YAML file. Here's an example configuration for a `users` table:
   ```yaml
   data_sources:
     - type: postgres
       name: my_postgres_db
       connection:
         host: localhost
         port: 5432
         user: my_user
         password: my_password
         database: my_database

   checks:
     - name: check_user_email_uniqueness
       sql: |
         SELECT COUNT(DISTINCT email) AS unique_emails,
                COUNT(email) AS total_emails
         FROM users
       assertion: unique_emails = total_emails
   ```

3. **Run the Checks**: Execute the checks using the Soda CLI:
   ```bash
   soda scan path/to/your/config.yaml
   ```

This command will run the defined checks and report results, helping you catch any data quality issues early in the pipeline.

## Common Pitfalls

- **Ignoring Data Quality Checks**: Skipping or underestimating the importance of data quality checks can lead to flawed analyses and unreliable ML models.
- **Overcomplicating Checks**: Keep your checks simple and focused. Complex queries can lead to performance issues or missed checks.
- **Not Updating Checks**: As your data schema changes, ensure that your checks are updated accordingly. Stale checks can give a false sense of security.

## In a nutshell

- Soda Core helps automate data quality management.
- Easy setup with YAML configuration for checks.
- Integrates with existing data workflows.
- Regular monitoring is key to maintaining data integrity.
- Keep checks simple and update them as your data evolves.