```markdown
# Snowflake Engineering — Cheatsheet

## [Section 1: Warehouses]

| Thing             | Syntax                                    | Notes                                  |
|-------------------|-------------------------------------------|----------------------------------------|
| Create Warehouse   | `CREATE WAREHOUSE my_warehouse;`        | Create a new warehouse.                |
| Resize Warehouse   | `ALTER WAREHOUSE my_warehouse RESIZE TO 'LARGE';` | Change the size of the warehouse.      |
| Suspend Warehouse  | `ALTER WAREHOUSE my_warehouse SUSPEND;` | Temporarily stop the warehouse.        |
| Resume Warehouse   | `ALTER WAREHOUSE my_warehouse RESUME;`  | Reactivate a suspended warehouse.      |
| Drop Warehouse     | `DROP WAREHOUSE my_warehouse;`          | Permanently delete the warehouse.      |

## [Section 2: Snowpipe]

```sql
CREATE OR REPLACE PIPE my_pipe AS 
COPY INTO my_table
FROM @my_stage
FILE_FORMAT = (TYPE = 'CSV');
```

## [Section 3: Streams & Tasks]

| Thing        | Syntax                                             | Notes                                    |
|--------------|----------------------------------------------------|------------------------------------------|
| Create Stream| `CREATE STREAM my_stream ON TABLE my_table;`      | Monitor changes in a table.             |
| Create Task  | `CREATE TASK my_task WAREHOUSE = my_warehouse AS INSERT INTO my_table SELECT * FROM my_stream;` | Automate actions on stream data.        |
| Start Task   | `ALTER TASK my_task RESUME;`                       | Activate the task for execution.        |
| Stop Task    | `ALTER TASK my_task SUSPEND;`                      | Pause the task.                         |
| Drop Stream   | `DROP STREAM my_stream;`                           | Remove the stream.                      |

## [Section 4: Cost Optimization]

| Thing                   | Syntax                                           | Notes                                    |
|-------------------------|--------------------------------------------------|------------------------------------------|
| Enable Auto Suspend      | `ALTER WAREHOUSE my_warehouse SET AUTO_SUSPEND = 300;` | Suspend after 5 minutes of inactivity.  |
| Set Max Concurrent Queries | `ALTER WAREHOUSE my_warehouse SET MAX_CONCURRENCY_LEVEL = 10;` | Limit concurrent queries to save costs. |
| Query History           | `SELECT * FROM TABLE(information_schema.query_history());` | Analyze past queries to optimize costs. |

## [Gotchas]

- ⚠️ Watch out for auto-suspend settings; forgetting to enable can lead to unexpected costs.
- ⚠️ Streams only capture changes post-creation; data before stream creation won't be tracked.

## [Mental model]

- **Warehouses:** Think of them as the power source for your queries, scaling up/down as needed.
- **Snowpipe:** Automates data loading; it's like an assembly line for your data.
- **Streams/Tasks:** Streams capture changes; tasks act on those changes, automating workflows.
```