```markdown
# Excel for Analysts — Cheatsheet

## [Section 1: Formulas]

| Thing            | Syntax                     | Notes                                      |
|------------------|----------------------------|--------------------------------------------|
| Sum              | `=SUM(A1:A10)`             | Adds values from A1 to A10.               |
| Average          | `=AVERAGE(B1:B10)`         | Calculates the average of B1 to B10.      |
| Count            | `=COUNT(C1:C10)`           | Counts numeric entries in C1 to C10.      |
| Max              | `=MAX(D1:D10)`             | Finds the maximum value in D1 to D10.     |
| Min              | `=MIN(E1:E10)`             | Finds the minimum value in E1 to E10.     |
| If               | `=IF(F1>10, "Yes", "No")`  | Returns "Yes" if F1 is greater than 10.  |

## [Section 2: VLOOKUP & XLOOKUP]

```excel
# VLOOKUP example
=VLOOKUP(G1, A1:B10, 2, FALSE)

# XLOOKUP example
=XLOOKUP(G1, A1:A10, B1:B10, "Not Found")
```

## [Section 3: Pivot Tables]

| Action          | Steps                                          |
|-----------------|------------------------------------------------|
| Create Pivot    | Select data → Insert → PivotTable             |
| Add Values      | Drag fields to "Values" area                  |
| Filter Rows     | Drag field to "Rows" area                      |
| Filter Columns  | Drag field to "Columns" area                   |

## [Section 4: Charts]

| Chart Type      | Steps                                          |
|-----------------|------------------------------------------------|
| Insert Chart    | Select data → Insert → Choose Chart Type      |
| Modify Chart    | Click on chart → Chart Design tab              |
| Add Elements     | Use "+" icon next to chart to add titles, legends, etc. |

## [Gotchas]

- ⚠️ Formulas must start with `=`; otherwise, Excel treats them as text.
- ⚠️ VLOOKUP only searches the leftmost column of the range.
- ⚠️ XLOOKUP is not available in Excel versions prior to 2019.

## [Mental model]

1. **Formulas**: Use them for calculations.
2. **Lookup Functions**: Use VLOOKUP/XLOOKUP to fetch data.
3. **Data Visualization**: Use charts to represent data insights visually.
```