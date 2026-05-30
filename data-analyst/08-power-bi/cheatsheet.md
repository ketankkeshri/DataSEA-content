```markdown
# Power BI Essentials — Cheatsheet

## [Core syntax]

| Thing                 | Syntax                                 | Notes                                         |
|-----------------------|----------------------------------------|-----------------------------------------------|
| Create Measure        | `Measure = SUM(Table[Column])`        | Measures are calculated fields.               |
| Calculate Column      | `NewColumn = Table[Column1] + 10`    | New columns can be added to tables.          |
| Filter Function       | `FILTER(Table, Table[Column] > 10)`   | Used to filter data in DAX expressions.      |
| Calculate Average     | `Average = AVERAGE(Table[Column])`    | Returns the average of a specified column.   |
| Create Relationship    | `Table1[Key] = Table2[Key]`          | Define relationships between tables.          |

## [Common operations]

```dax
// Create a calculated column for profit
Profit = Table[Revenue] - Table[Cost]

// Create a measure for total sales
TotalSales = SUM(Sales[Amount])

// Filter data for a specific year
Sales2023 = CALCULATE(SUM(Sales[Amount]), Sales[Year] = 2023)

// Use RELATED to get data from a related table
CustomerName = RELATED(Customers[Name])
```

## [Gotchas]

- ⚠️ Measures are evaluated in the context of the report filters. Always check filter context!
- ⚠️ Circular relationships can occur if two tables reference each other. Avoid this to prevent errors.
- ⚠️ DAX is case-sensitive. Ensure consistent casing for column and table names.

## [Mental model]

- Relationships are like bridges connecting tables; measures are calculations performed on data.
- Filtering is key: think of it as zooming in on your dataset to only see what matters.
- Use visuals to communicate insights: charts and graphs help tell the story of your data.
```