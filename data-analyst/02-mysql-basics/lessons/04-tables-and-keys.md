# Tables And Keys

Understanding tables and keys in MySQL is crucial for structuring your database effectively. A solid grasp of these concepts will help you design efficient databases that maintain data integrity and optimize query performance, which is essential for any data-driven role.

## What Are Tables?

Tables are the backbone of any relational database, acting as the containers for your data. Each table consists of rows and columns, where:

- **Rows** represent individual records (or entries).
- **Columns** represent the attributes of those records.

For example, consider a `customers` table:

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

Here, `customer_id` is a unique identifier for each customer. This is where keys come into play.

## Understanding Keys

Keys are critical in ensuring the integrity and efficiency of your database. They help establish relationships between tables and enforce rules. The main types of keys are:

- **Primary Key**: A unique identifier for each row in a table. No two rows can have the same primary key value.
- **Foreign Key**: A field (or collection of fields) in one table that uniquely identifies a row of another table. It creates a link between the two tables.

For instance, let’s create an `orders` table that references the `customers` table:

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

In this example, `customer_id` in the `orders` table is a foreign key that links back to the `customers` table. This relationship ensures that every order is associated with a valid customer.

## Common pitfalls

- **Not setting primary keys**: Forgetting to define a primary key can lead to duplicate records and make it difficult to uniquely identify each row.
- **Cascading deletes**: Be cautious when using foreign keys with cascading options. Deleting a record from a parent table might unintentionally remove related records in child tables.
- **Data type mismatches**: Ensure that the data types of foreign keys match those of the primary keys they reference. A mismatch can lead to errors when inserting or updating records.

## In a nutshell

- Tables store data in rows and columns, with each row representing a record.
- Primary keys uniquely identify records, while foreign keys establish relationships between tables.
- Be mindful of common pitfalls like missing primary keys and cascading deletes to avoid data integrity issues.