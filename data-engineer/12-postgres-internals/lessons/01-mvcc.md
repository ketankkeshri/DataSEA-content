# Mvcc

Multi-Version Concurrency Control (MVCC) is a key feature in PostgreSQL that enables high concurrency and consistent reads without locking, a must-know for any data engineer. Understanding MVCC helps you design scalable applications that can handle multiple transactions seamlessly.

## How MVCC Works

MVCC allows multiple transactions to occur simultaneously by keeping several versions of each row in the database. When a transaction modifies a row, PostgreSQL creates a new version of that row instead of overwriting the existing one. This way, readers can access the old version while the writer is busy, ensuring that they see a consistent snapshot of the data.

### Transaction States

In PostgreSQL, each transaction can be in one of several states:

- **Active**: The transaction is currently running.
- **Committed**: The transaction has been successfully completed and its changes are now visible to other transactions.
- **Aborted**: The transaction has been rolled back and its changes are discarded.

### Row Versions

When a row is modified, PostgreSQL creates new versions of that row. Each version has two important timestamps:

- **xmin**: The transaction ID that created the row.
- **xmax**: The transaction ID that deleted the row (if applicable).

This allows PostgreSQL to determine which version of the row is visible to a given transaction based on its own transaction ID.

### Example

Let’s take a look at a simple example using an `orders` table:

```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INT,
    total DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO orders (customer_id, total) VALUES (1, 100.00);
INSERT INTO orders (customer_id, total) VALUES (2, 150.00);
```

Now, if a transaction updates an order:

```sql
BEGIN;

UPDATE orders SET total = 120.00 WHERE id = 1;

-- At this point, the updated row version exists, but the old version is still available to other transactions.
```

Another transaction reading the `orders` table will see the old version of the row until the first transaction is committed:

```sql
BEGIN;

SELECT * FROM orders; -- This will return the old total for order id 1: 100.00

COMMIT;
```

After the first transaction commits, subsequent reads will see the updated total.

## Common pitfalls

- **Transaction IDs wraparound**: If the database is active for a long time, transaction IDs can wrap around, leading to potential visibility issues.
- **Long-running transactions**: These can hold onto old row versions, causing bloat and performance issues over time.
- **Vacuuming**: Not running `VACUUM` regularly can lead to excessive storage usage due to the accumulation of dead tuples.

## In a nutshell

- MVCC allows PostgreSQL to handle multiple transactions simultaneously without locking.
- Each row version has `xmin` and `xmax` timestamps to track visibility.
- Long-running transactions can cause issues if not managed properly.
- Regular maintenance like `VACUUM` is essential to keep performance optimal.