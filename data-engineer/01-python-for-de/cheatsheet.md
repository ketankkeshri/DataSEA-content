```markdown
# Python for Data Engineering — Cheatsheet

## [Section 1: Data Structures]

| Thing              | Syntax                           | Notes                                     |
|--------------------|----------------------------------|-------------------------------------------|
| List               | `my_list = [1, 2, 3]`           | Ordered, mutable, allows duplicates.     |
| Tuple              | `my_tuple = (1, 2, 3)`          | Ordered, immutable, allows duplicates.   |
| Dictionary         | `my_dict = {'key': 'value'}`    | Key-value pairs, unordered.              |
| Set                | `my_set = {1, 2, 3}`            | Unordered, no duplicates.                 |

## [Section 2: File I/O]

```python
# Reading a file
with open('file.txt', 'r') as file:
    data = file.read()

# Writing to a file
with open('file.txt', 'w') as file:
    file.write('Hello, DataSEA!')
```

## [Section 3: Context Managers]

```python
# Using a context manager
with open('file.txt', 'r') as f:
    content = f.read()  # Automatically closes the file
```

## [Section 4: Error Handling]

```python
# Try/Except block
try:
    risky_code()  # Replace with code that might fail
except Exception as e:
    print(f"An error occurred: {e}")
```

## [Section 5: Virtualenv & Pip]

```bash
# Create a virtual environment
python -m venv myenv

# Activate virtual environment
# On Windows
myenv\Scripts\activate
# On macOS/Linux
source myenv/bin/activate

# Install packages
pip install package_name
```

## [Section 6: Typing]

```python
# Function with type hints
def add(a: int, b: int) -> int:
    return a + b
```

## [Gotchas]

- ⚠️ Remember to deactivate your virtual environment with `deactivate` when done.
- ⚠️ Using `with open(...)` is crucial for proper file handling; it avoids resource leaks.

## [Mental model]

- **Data Structures:** Lists, tuples, dicts, and sets—choose based on mutability and order.
- **File I/O:** Always use `with` for file operations to ensure files are closed.
- **Error Handling:** Use try/except to manage exceptions without crashing your program.
```