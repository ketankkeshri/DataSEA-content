# Streams Tasks

Streams in Snowflake are powerful tools for tracking changes to data in your tables. This lesson dives into how to effectively use streams and tasks to automate data pipelines, ensuring your data is always fresh and ready for analysis.

## Understanding Streams

Streams in Snowflake capture changes to a table, allowing you to track inserts, updates, and deletes. They act like a change data capture (CDC) mechanism, so you can keep your analytics up-to-date without having to reprocess entire datasets.

Here’s how to create a stream on a table:

```sql
CREATE OR REPLACE STREAM orders_stream 
ON TABLE orders 
APPEND_ONLY = FALSE; 
```

In this example, we create a stream called `orders_stream` on the `orders` table. The `APPEND_ONLY` option is set to `FALSE`, meaning it will track all changes (inserts, updates, deletes).

### Querying Stream Data

Once you have a stream created, you can query it to see what changes have occurred since the last time you processed it. Here’s how to get the latest changes:

```sql
SELECT * 
FROM orders_stream;
```

This will return all changes made to the `orders` table since the last time you queried the stream. You can use this data to feed into downstream processing tasks.

## Automating with Tasks

Tasks in Snowflake are scheduled operations that can run SQL statements on a defined schedule. By combining tasks with streams, you can automate the processing of data changes.

Here’s an example of creating a task that processes new orders:

```sql
CREATE OR REPLACE TASK process_new_orders 
WAREHOUSE = my_warehouse 
SCHEDULE = 'USING CRON 0 * * * * UTC' 
AS 
INSERT INTO processed_orders 
SELECT * 
FROM orders_stream 
WHERE METADATA$IS_UPDATE = FALSE; 
```

In this example, the task `process_new_orders` runs every hour, inserting new records from `orders_stream` into the `processed_orders` table. The `METADATA$IS_UPDATE` filter ensures that only new records (not updates) are processed.

### Chaining Streams and Tasks

You can set up multiple streams and tasks to create a robust data pipeline. For instance, if you have a stream for user events, you can create a separate task that aggregates user activity and triggers downstream processes.

```sql
CREATE OR REPLACE TASK aggregate_user_events 
WAREHOUSE = my_warehouse 
SCHEDULE = 'USING CRON 15 * * * * UTC' 
AS 
INSERT INTO user_activity_summary 
SELECT user_id, COUNT(*) AS event_count 
FROM user_events_stream 
GROUP BY user_id; 
```

This task aggregates user events every 15 minutes and stores the results in a summary table, enabling quick access to user activity metrics.

## Common pitfalls

- **Not considering stream retention:** Streams have a limited retention period (default 14 days). If data isn't processed in time, you might miss changes.
- **Overlapping tasks:** If tasks that write to the same table run concurrently, you could encounter issues with conflicting writes or performance bottlenecks.
- **Ignoring error handling:** Always implement error handling in your tasks. Use error tables or notifications to catch and resolve issues promptly.

## In a nutshell

- Streams track changes to tables, enabling real-time data updates.
- Tasks automate SQL operations on a defined schedule, allowing for efficient data processing.
- Combine streams and tasks to create automated data workflows.
- Be mindful of retention periods and potential pitfalls in task designs.