# Magics

Jupyter magics are special commands that enhance your workflow in Jupyter notebooks. Knowing how to use them can save you time and make your analysis more efficient, which is crucial for any Data Engineer, Data Analyst, or Data Scientist.

## What Are Magics?

Magics are built-in commands in Jupyter that allow you to perform operations with a simple syntax. There are two types of magics: line magics and cell magics.

- **Line magics** start with a single `%` and operate on a single line of input.
- **Cell magics** start with `%%` and apply to the entire cell.

### Example of Line Magic

Let’s check out a classic line magic: `%timeit`. This command helps you measure the execution time of a single line of code.

```python
%timeit sum(range(1000))
```

### Example of Cell Magic

For cell magics, consider `%%writefile`, which creates a file with the contents of the cell.

```python
%%writefile hello.py
print("Hello, DataSEA!")
```

This command will create a Python file named `hello.py` in your current directory. You can then run this file using:

```bash
!python hello.py
```

## Useful Magics for Data Science

Here are some magics frequently used by data scientists:

- **`%matplotlib inline`**: This command is used to display matplotlib plots inline within the Jupyter notebook.
- **`%load`**: Loads code from a file into a cell.
- **`%run`**: Runs a Python script and imports its variables into the notebook.
- **`%history`**: Displays the command history for your current session.

### Example of `%matplotlib inline`

To visualize some data inline, you can use the following:

```python
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

## Common pitfalls

- **Using the wrong magic type**: Remember that line magics only work for single lines, while cell magics affect the entire cell. Using them incorrectly can lead to unexpected errors.
- **Forgetting to load libraries**: Some magics depend on libraries being imported first. Always ensure you have your necessary imports before using them.
- **Not checking the current directory**: When using `%writefile`, ensure you know where the file is being saved, or you might end up looking for it in the wrong place.

## In a nutshell

- Magics enhance Jupyter's capabilities with simple commands.
- Line magics (`%`) apply to single lines, while cell magics (`%%`) apply to the whole cell.
- Common magics include `%matplotlib inline` for plotting and `%run` for executing scripts.
- Always check your syntax and library imports when using magics.
- Be aware of your current directory when saving files.