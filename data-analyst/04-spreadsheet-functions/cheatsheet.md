```markdown
# Spreadsheet Functions Deep Dive — Cheatsheet

## Section 1: Text Functions

| Thing                  | Syntax                          | Notes                                         |
|-----------------------|---------------------------------|-----------------------------------------------|
| Concatenate strings    | `=CONCATENATE(A1, B1)`         | Combines multiple strings into one.          |
| Uppercase              | `=UPPER(A1)`                   | Converts text to uppercase.                   |
| Lowercase              | `=LOWER(A1)`                   | Converts text to lowercase.                   |
| Trim spaces            | `=TRIM(A1)`                    | Removes extra spaces from text.              |
| Find substring         | `=FIND("text", A1)`           | Returns the starting position of a substring.|
| Replace text           | `=SUBSTITUTE(A1, "old", "new")`| Replaces occurrences of text in a string.    |

## Section 2: Date Functions

| Thing                  | Syntax                          | Notes                                         |
|-----------------------|---------------------------------|-----------------------------------------------|
| Current date           | `=TODAY()`                      | Returns the current date.                    |
| Current date & time    | `=NOW()`                        | Returns the current date and time.           |
| Year from date         | `=YEAR(A1)`                    | Extracts the year from a date.               |
| Month from date        | `=MONTH(A1)`                   | Extracts the month from a date.              |
| Day from date          | `=DAY(A1)`                     | Extracts the day from a date.                |
| Add days to date       | `=A1 + N`                      | Adds N days to the date in A1.               |

## Section 3: Lookup Functions

| Thing                  | Syntax                          | Notes                                         |
|-----------------------|---------------------------------|-----------------------------------------------|
| VLOOKUP                | `=VLOOKUP(lookup_value, table_array, col_index, [range_lookup])` | Searches for a value in the first column. |
| HLOOKUP                | `=HLOOKUP(lookup_value, table_array, row_index, [range_lookup])` | Searches for a value in the first row.     |
| INDEX                  | `=INDEX(array, row_num, [column_num])` | Returns the value of a cell in a table based on row/column number. |
| MATCH                  | `=MATCH(lookup_value, lookup_array, [match_type])` | Returns the position of a value in a range. |

## Section 4: Array Formulas

| Thing                  | Syntax                          | Notes                                         |
|-----------------------|---------------------------------|-----------------------------------------------|
| Simple array formula    | `={1,2,3;4,5,6}`              | Creates a 2D array with rows and columns.    |
| Sum of an array        | `=SUM(A1:A10 * B1:B10)`       | Multiplies corresponding items and sums them.|
| Unique values          | `=UNIQUE(A1:A10)`             | Returns a list of unique values from a range.|
| Filter array           | `=FILTER(A1:A10, B1:B10 > 10)`| Returns an array filtered by a condition.    |

## Gotchas

- ⚠️ VLOOKUP only searches the first column of the specified range — keep that in mind when structuring data.
- ⚠️ Array formulas need to be entered with `Ctrl + Shift + Enter` in older versions of Excel to work correctly.

## Mental model

- **Text Functions:** Manipulate strings for formatting and content.
- **Date Functions:** Handle dates and perform calculations based on them.
- **Lookup Functions:** Efficiently find and retrieve data from tables.
- **Array Formulas:** Work with multiple values and perform operations on arrays.
```