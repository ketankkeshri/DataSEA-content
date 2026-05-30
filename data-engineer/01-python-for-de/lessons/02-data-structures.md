# Data Structures

Data engineers often work with large datasets and need efficient ways to store and manipulate that data. Understanding Python’s built-in data structures like lists, tuples, sets, and dictionaries is crucial for any data-related task, whether you’re cleaning data or building pipelines.

## Python Data Structures Overview

Python provides several built-in data structures that can help you manage and organize your data effectively. Here’s a quick rundown:

- **Lists**: Ordered, mutable collections of items. Great for holding sequences of data.
- **Tuples**: Ordered, immutable collections. Use them when you want to ensure data integrity.
- **Sets**: Unordered collections of unique items. Perfect for eliminating duplicates.
- **Dictionaries**: Key-value pairs. Ideal for mapping relationships between data.

Let’s dive deeper into each of these structures with some runnable examples.

### Lists

Lists are one of the most commonly used data structures in Python. They allow you to store multiple items in a single variable.

```python
# Creating a list of names
names = ["Alice", "Bob", "Charlie"]

# Accessing elements
print(names[0])  # Output: Alice

# Modifying elements
names[1] = "David"
print(names)  # Output: ['Alice', 'David', 'Charlie']
```

### Tuples

Tuples are similar to lists but are immutable. Once created, you cannot change their content.

```python
# Creating a tuple
coordinates = (10.0, 20.0)

# Accessing elements
print(coordinates[0])  # Output: 10.0

# Attempting to modify a tuple will result in an error
# coordinates[1] = 30.0  # Raises TypeError
```

### Sets

Sets are useful when you need to store unique items and don’t care about the order.

```python
# Creating a set
fruits = {"apple", "banana", "cherry", "apple"}  # 'apple' will be ignored

# Checking membership
print("banana" in fruits)  # Output: True

# Adding and removing items
fruits.add("orange")
fruits.remove("banana")
print(fruits)  # Output: {'cherry', 'orange', 'apple'}
```

### Dictionaries

Dictionaries allow you to store data in key-value pairs, making it easy to retrieve information.

```python
# Creating a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

# Accessing values
print(student["name"])  # Output: Alice

# Modifying values
student["age"] = 22
print(student)  # Output: {'name': 'Alice', 'age': 22, 'major': 'Computer Science'}
```

## Common pitfalls

- **Modifying Immutable Structures**: Remember that tuples are immutable. Trying to change their content will raise errors.
- **Using Mutable Keys in Dictionaries**: Avoid using mutable types (like lists) as keys in dictionaries. They can lead to unexpected behavior.
- **Assuming Order in Sets**: Sets are unordered. If you require ordered data, consider using lists or tuples instead.

## In a nutshell

- **Lists** are mutable and ordered.
- **Tuples** are immutable and ordered.
- **Sets** are unordered collections of unique items.
- **Dictionaries** store data in key-value pairs, making data retrieval efficient.
- Choose the right structure based on your data needs to optimize performance and maintainability.