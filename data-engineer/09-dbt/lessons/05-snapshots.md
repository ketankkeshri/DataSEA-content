# Snapshots

Snapshots in dbt are powerful tools that allow you to capture the state of your data at a specific point in time. This is especially useful for tracking changes in your data and for auditing purposes. As a data engineer, understanding how to effectively implement snapshots can help you maintain data integrity and manage historical data efficiently.

## What are Snapshots?

Snapshots are a way to create a historical record of your data. When you apply a snapshot in dbt, you essentially create a new table that records changes to a specified set of columns over time. This is particularly important in scenarios where data is regularly updated, and you need to track these changes for analysis or compliance.

### How Snapshots Work

When you set up a snapshot, you define a source table and specify which columns to monitor for changes. Each time the snapshot is run, dbt compares the current state of the source table with the previous snapshot. If any specified columns have changed, a new record is created in the snapshot table, preserving the old value and the timestamp of the change.

```sql
-- Example: Creating a snapshot in dbt

{{ config(
    target_database='your_database',
    target_schema='snapshots',
    unique_key='user_id',
    strategy='timestamp',
    updated_at='updated_at'
) }}

SELECT
    user_id,
    email,
    created_at,
    updated_at,
    CURRENT_TIMESTAMP() AS dbt_valid_from,
    NULL AS dbt_valid_to
FROM
    {{ ref('users') }}
```

In this example, we’re creating a snapshot of the `users` table. We're tracking changes based on the `updated_at` column, and we use `user_id` as our unique key. Each time this snapshot is run, it will capture the current state of the user's email and other relevant fields.

## Setting Up Snapshots

To implement snapshots in dbt, follow these steps:

1. **Define Your Snapshot**: Create a new `.sql` file in the `snapshots` directory of your dbt project.
2. **Use the Config Block**: Specify the configuration settings, including the unique key and strategy (e.g., timestamp or check).
3. **Write the SQL Query**: Select the columns you want to track and ensure you're capturing the necessary metadata for auditing.
4. **Run the Snapshot**: Execute the snapshot using the dbt CLI with `dbt snapshot`.

### Common Use Cases

- **Tracking Slowly Changing Dimensions**: Snapshots are ideal for tracking changes in dimensions like customer profiles or product details.
- **Auditing Changes**: If you need to maintain a historical record of how your data evolves, snapshots provide a clear audit trail.
- **Data Quality Checks**: You can use snapshots to verify that your data transformations are yielding the expected results over time.

## Common pitfalls

- **Not Defining a Unique Key**: Ensure you always define a unique key to avoid duplicate records in your snapshot.
- **Ignoring Performance Implications**: Depending on the size of your source table, snapshots can become large and impact performance. Regularly review your snapshot strategy.
- **Not Archiving Old Snapshots**: If you don’t manage old snapshots, they can consume unnecessary storage and slow down your queries.

## In a nutshell

- Snapshots capture the state of your data over time.
- Define unique keys and select columns carefully for effective tracking.
- Use snapshots for auditing, slowly changing dimensions, and data quality checks.
- Regularly review and manage snapshots to maintain performance and storage efficiency.