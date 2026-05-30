# File Io

Understanding file input and output (I/O) is crucial for data engineers. Whether you're processing large datasets or managing configuration files, knowing how to efficiently read from and write to files in Python will boost your productivity and help you avoid common pitfalls. 

## Reading Files in Python

Python provides several built-in functions to handle file I/O. The most common way to read a file is using the `open()` function, which allows you to specify the mode (read, write, etc.) in which the file should be opened. 

Here's a classic example of reading a text file:

```python
# Reading a file
file_path = 'data.txt'

with open(file_path, 'r') as file:
    data = file.read()

print(data)
```

This example uses a context manager (`with` statement) to ensure the file is properly closed after its suite finishes, which helps avoid file leaks.

### File Modes

When opening a file, you can use different modes:

- `'r'`: Read (default)
- `'w'`: Write (overwrites if the file exists)
- `'a'`: Append (adds to the end of the file)
- `'b'`: Binary mode (e.g., for images)

Choosing the right mode is essential to avoid unintentional data loss.

## Writing Files in Python

Writing data to files in Python is just as straightforward. You can also use the `open()` function with the write mode. Here's how to create a new file or overwrite an existing one:

```python
# Writing to a file
output_file_path = 'output.txt'

data_to_write = "Hello, Data Engineering!\nWelcome to File I/O in Python."

with open(output_file_path, 'w') as file:
    file.write(data_to_write)
```

In this example, if `output.txt` already exists, it will be overwritten with the new content. If it doesn’t exist, Python will create it for you.

### Using CSV and JSON Formats

For structured data, you often use formats like CSV and JSON. Here’s how to handle these formats:

**CSV Example:**

```python
import csv

data = [
    ['name', 'age'],
    ['Alice', 30],
    ['Bob', 25]
]

with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

**JSON Example:**

```python
import json

data = {
    "name": "Alice",
    "age": 30
}

with open('data.json', 'w') as file:
    json.dump(data, file)
```

Using these formats makes it easier to interchange data between systems, which is a common requirement in data engineering.

## Common pitfalls

- **File Not Found Error**: Always check if the file exists or handle exceptions properly to avoid crashes.
- **Improper File Closure**: Forgetting to close files can lead to memory leaks. Always use a context manager.
- **Data Overwrite**: Using the wrong mode (`'w'` instead of `'a'`) can overwrite existing data. Double-check your file modes.

## In a nutshell

- Use `open()` to manage file I/O in Python.
- Always prefer context managers to ensure files are closed properly.
- Handle structured data with CSV and JSON for better interoperability.
- Be aware of file modes to prevent data loss.
- Check for common pitfalls to write robust file-handling code.