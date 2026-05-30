# Lineage

Data lineage gives you a clear view of the data journey from its origin to its destination. Understanding lineage is crucial for Data Engineers and Data Scientists because it helps ensure data trustworthiness and compliance, making it easier to debug, audit, and optimize data workflows.

## What is Data Lineage?

Data lineage refers to the process of tracking and visualizing the flow of data through various stages in a data pipeline. This includes data creation, transformation, and consumption. A robust lineage system allows you to answer questions like:

- Where did this data come from?
- What transformations were applied?
- How is this data being used?

For example, if you're analyzing customer behavior from an `orders` table, understanding lineage helps you see how raw data from the `customers` table is aggregated, filtered, and transformed into actionable insights.

### Why Does It Matter?

- **Debugging**: Quickly identify where things went wrong in your data pipeline.
- **Compliance**: Meet regulatory requirements by knowing data origins and transformations.
- **Optimization**: Improve data workflows by understanding unnecessary transformations or data copies.

## Implementing Data Lineage

To implement data lineage effectively, you can leverage various tools and techniques. Here's a simple example using Python with a SQLite database to track lineage for our `orders` data.

```python
import sqlite3

# Connect to a SQLite database
conn = sqlite3.connect('data_lineage.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers (id)
);
''')

# Insert sample data
cursor.execute('INSERT INTO customers (name) VALUES ("Alice")')
cursor.execute('INSERT INTO orders (customer_id, amount) VALUES (1, 100.50)')

# Function to track lineage
def log_lineage(action, table_name):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS lineage (
        id INTEGER PRIMARY KEY,
        action TEXT,
        table_name TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')
    cursor.execute('INSERT INTO lineage (action, table_name) VALUES (?, ?)', (action, table_name))
    conn.commit()

# Log the lineage
log_lineage("INSERT", "customers")
log_lineage("INSERT", "orders")

# Fetch and display lineage
cursor.execute('SELECT * FROM lineage')
print(cursor.fetchall())

conn.close()
```

### Explanation

1. **Database Setup**: We create a SQLite database with `customers` and `orders` tables.
2. **Data Insertion**: Sample data is inserted into both tables.
3. **Lineage Logging**: A `log_lineage` function is defined to track actions (like inserts) and log them in a `lineage` table.

## Common pitfalls

- **Inconsistent Logging**: Failing to log all transformations can lead to incomplete lineage tracking.
- **Overly Complex Pipelines**: Keeping lineage simple is key. Complex transformations can obscure the data path.
- **Lack of Documentation**: Without proper documentation, understanding lineage can become cumbersome and confusing.

## In a nutshell

- Data lineage tracks the path of data from source to destination.
- It aids in debugging, compliance, and optimization.
- Implement lineage using logging mechanisms in your data pipelines.
- Watch out for inconsistent logging and overly complex setups.
- Keep documentation updated to simplify lineage understanding.