# Find Grep Awk

Mastering the command line is essential for any data engineer, and tools like `grep` and `awk` are crucial for processing text data. This lesson dives into how to effectively utilize these powerful tools for data extraction and manipulation.

## Understanding Grep

`grep` is a command-line utility for searching plain-text data for lines that match a regular expression. It's your go-to tool for filtering out relevant information from log files, configuration files, or any text data.

### Basic Usage of Grep

Here’s how you can use `grep` in a simple command:

```bash
grep "ERROR" application.log
```

This command searches for the term “ERROR” in the `application.log` file and displays all matching lines. 

### Common Grep Options

- `-i`: Case insensitive search.
- `-v`: Invert match (show lines that do NOT match).
- `-r`: Recursive search through directories.
- `-n`: Show line numbers of matches.

#### Example:

```bash
grep -i "warning" /var/log/syslog
```

This command finds all instances of “warning” (regardless of case) in the system log.

## Getting to Know Awk

`awk` is a powerful programming language designed for text processing. It’s particularly good at handling structured data files, like CSVs or tab-delimited files, and can perform complex pattern matching and data manipulation.

### Basic Usage of Awk

Here’s a simple example to print the second column of a space-separated file:

```bash
awk '{print $2}' data.txt
```

This command reads `data.txt` and prints the second column from each line.

### Common Awk Features

- **Field Separator**: Use `-F` to specify a custom delimiter.
- **Patterns**: You can filter lines based on conditions.
- **Built-in Variables**: `$0` for the whole line, `$1`, `$2`, etc., for individual fields.

#### Example with Conditions:

```bash
awk -F, '$3 > 100 {print $1, $3}' sales.csv
```

This command uses a comma as a delimiter and prints the first and third columns for rows where the third column value is greater than 100.

## Combining Grep and Awk

You can use `grep` and `awk` together for more powerful text processing. For example, you might want to find error messages in logs and extract specific details:

```bash
grep "ERROR" application.log | awk '{print $5, $6}'
```

This command first filters the log for lines containing "ERROR" and then extracts the fifth and sixth fields from those lines.

## Common pitfalls

- Using `grep` without proper regex can lead to unexpected matches.
- Forgetting to quote patterns in `awk` can cause syntax errors.
- Mixing up field numbers in `awk`—remembering that `$1` is the first column!

## In a nutshell

- Use `grep` to quickly search and filter text data.
- Leverage `awk` for more complex data extraction and manipulation.
- Combine both tools for efficient text processing workflows.
- Always check your delimiters and patterns to avoid surprises.