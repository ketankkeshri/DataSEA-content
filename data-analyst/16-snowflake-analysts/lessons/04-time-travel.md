# Time Travel

Snowflake's time travel feature allows data analysts to query historical data as it was at a specific point in time. This capability is crucial for auditing, compliance, or simply comparing historical trends against current data.

## Understanding Time Travel

Snowflake's time travel enables you to access historical data for up to 90 days. This is highly useful when you need to:

- Recover lost data due to accidental deletions or updates.
- Analyze trends over time to make informed business decisions.
- Validate data changes by comparing snapshots.

To utilize time travel, you can use the `AT` clause in your queries or specify a timestamp. Here's an example to illustrate:

```sql
SELECT *
FROM orders
AT (TIMESTAMP => '2023-10-01 12:00:00')
WHERE customer_id = 123;
```

In this query, we access the `orders` table as it existed on October 1, 2023, at 12:00 PM. This allows you to see how the order data looked at that exact moment in time.

## Using Time Travel Effectively

### Specifying a Time Period

You can also specify a time period using the `BEFORE` or `AFTER` keywords. This is particularly useful for analyzing changes over a range of time. Here’s how to do it:

```sql
SELECT *
FROM orders
BEFORE (TIMESTAMP => '2023-10-01 00:00:00')
WHERE customer_id = 123;
```

This query retrieves all records from the `orders` table for customer 123 before midnight on October 1, 2023. 

### Retention Periods

Keep in mind that the default time travel retention period is 1 day. You can increase this to 90 days by altering the table definition:

```sql
ALTER TABLE orders 
SET DATA_RETENTION_TIME_IN_DAYS = 30;
```

This change allows you to retain historical data for a longer period, which can be beneficial for analysis and audits.

## Common pitfalls

- **Not Checking Retention Settings:** Always verify your table's data retention settings; forgetting to adjust them can lead to lost historical data.
- **Overusing Time Travel:** Relying too heavily on time travel for data recovery can lead to performance issues. Use it judiciously.
- **Timestamp Format Errors:** Ensure your timestamps are in the correct format. An incorrect format will lead to errors in your queries.

## In a nutshell

- Snowflake's time travel lets you query historical data for up to 90 days.
- Use the `AT`, `BEFORE`, and `AFTER` keywords to specify data snapshots.
- Adjust data retention settings to prevent loss of historical data.
- Avoid common pitfalls like incorrect timestamp formats and over-reliance on time travel.