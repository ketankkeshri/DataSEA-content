# Pivot Unpivot

Mastering pivoting and unpivoting data in SQL can dramatically simplify how you analyze and present your datasets. These powerful transformations allow you to reshape your data, making it easier to generate reports and insights.

## Understanding Pivot

Pivoting transforms rows into columns, allowing you to turn unique values from one column into multiple columns in the output. This is particularly useful for summarizing data, like transforming sales data into a more digestible format.

### Example: Pivoting Sales Data

Consider a simple `sales` table that tracks monthly sales by product:

```sql
CREATE TABLE sales (
    product VARCHAR(50),
    month VARCHAR(20),
    amount INT
);

INSERT INTO sales (product, month, amount) VALUES
('Shoes', 'January', 100),
('Shoes', 'February', 150),
('Shirts', 'January', 200),
('Shirts', 'February', 250);
```

To pivot this data and show the total sales for each product by month:

```sql
SELECT 
    product,
    COALESCE(SUM(CASE WHEN month = 'January' THEN amount END), 0) AS january_sales,
    COALESCE(SUM(CASE WHEN month = 'February' THEN amount END), 0) AS february_sales
FROM sales
GROUP BY product;
```

This query results in:

| Product | January Sales | February Sales |
|---------|---------------|----------------|
| Shoes   | 100           | 150            |
| Shirts  | 200           | 250            |

## Understanding Unpivot

Unpivoting is the reverse operation; it transforms columns back into rows. This is essential when you need to normalize data or when you want to perform operations that require a column-oriented view.

### Example: Unpivoting Sales Data

Suppose you have the following pivoted sales data:

```sql
CREATE TABLE sales_summary (
    product VARCHAR(50),
    january_sales INT,
    february_sales INT
);

INSERT INTO sales_summary (product, january_sales, february_sales) VALUES
('Shoes', 100, 150),
('Shirts', 200, 250);
```

To unpivot this data back into a more traditional format:

```sql
SELECT 
    product,
    month,
    amount
FROM sales_summary
UNPIVOT (
    amount FOR month IN (january_sales AS 'January', february_sales AS 'February')
) AS unpvt;
```

This results in:

| Product | Month   | Amount |
|---------|---------|--------|
| Shoes   | January | 100    |
| Shoes   | February| 150    |
| Shirts  | January | 200    |
| Shirts  | February| 250    |

## Common pitfalls

- **Data Type Mismatches:** Ensure that the column types you’re pivoting or unpivoting are compatible to avoid errors.
- **Null Handling:** Be mindful of null values; they can affect your aggregations and final output if not handled properly.
- **Excessive Pivoting:** Overusing pivot can lead to complex queries that are hard to read and maintain. Keep it straightforward.

## In a nutshell

- Pivoting reshapes rows into columns for easier analysis.
- Unpivoting transforms columns back into rows to normalize data.
- Use `COALESCE` to handle nulls when pivoting.
- Ensure data types match during pivot/unpivot operations.
- Avoid convoluted queries by keeping transformations clear and concise.