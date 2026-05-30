```markdown
# MySQL Basics — Cheatsheet

## [Data Types]

| Data Type      | Syntax                | Notes                          |
|----------------|-----------------------|--------------------------------|
| INT            | `INT`                 | Integer, no decimals.          |
| VARCHAR        | `VARCHAR(n)`          | Variable-length string, n chars.|
| TEXT           | `TEXT`                | Large text data.               |
| DATE           | `DATE`                | Format: `YYYY-MM-DD`.          |
| DATETIME       | `DATETIME`            | Format: `YYYY-MM-DD HH:MM:SS`. |
| FLOAT          | `FLOAT`               | Floating point number.         |
| DECIMAL        | `DECIMAL(p,s)`        | Exact numeric, p=precision, s=scalability.|

## [Creating Tables and Keys]

```sql
CREATE TABLE table_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## [Indexes Basics]

| Index Type     | Syntax                         | Notes                          |
|----------------|--------------------------------|--------------------------------|
| Primary Key    | `PRIMARY KEY (column_name)`    | Unique identifier.            |
| Unique Index   | `UNIQUE (column_name)`         | No duplicates allowed.        |
| Regular Index  | `INDEX index_name (column_name)`| Improves search speed.       |

## [Common Operations]

```sql
-- Insert Data
INSERT INTO table_name (name) VALUES ('Example');

-- Select Data
SELECT * FROM table_name WHERE name = 'Example';

-- Update Data
UPDATE table_name SET name = 'Updated Example' WHERE id = 1;

-- Delete Data
DELETE FROM table_name WHERE id = 1;
```

## [Gotchas]

- ⚠️ Remember to define `NOT NULL` if a column must have a value; otherwise, it can be left empty.
- ⚠️ Using `AUTO_INCREMENT` requires the column to be indexed (usually as a primary key).

## [Mental model]

- **Table Structure**: Tables consist of rows and columns, where each row is a record and each column is a field.
- **Keys**: Primary keys uniquely identify a record, while foreign keys establish relationships between tables.
- **Indexes**: Think of indexes like the index of a book - they help you find data faster without scanning each row.
```