```markdown
# NumPy Foundations — Cheatsheet

## Section 1: Core Syntax

| Thing                  | Syntax                      | Notes                                      |
|-----------------------|-----------------------------|--------------------------------------------|
| Import NumPy          | `import numpy as np`       | Standard alias for NumPy.                  |
| Create array          | `np.array([1, 2, 3])`      | Creates a 1D array.                        |
| Create 2D array       | `np.array([[1, 2], [3, 4]])` | Creates a 2D array (matrix).              |
| Check shape           | `array.shape`               | Returns the dimensions of the array.      |
| Get array type        | `array.dtype`               | Returns the data type of the array elements. |

## Section 2: Common Operations

```python
import numpy as np

# Creating arrays
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])

# Indexing and Slicing
print(a[0])        # Output: 1
print(b[1, 0])     # Output: 3
print(a[1:])       # Output: [2, 3]

# Broadcasting
c = np.array([1, 2, 3])
d = c + 10         # Output: [11, 12, 13]

# Vectorization
e = np.array([1, 2, 3])
f = e * 2          # Output: [2, 4, 6]
```

## Gotchas

- ⚠️ **Indexing starts at 0**: Remember that the first element is accessed with index 0.
- ⚠️ **Shape mismatch**: Operations between arrays must have compatible shapes; otherwise, you'll face errors.

## Mental Model

- **Arrays**: Think of NumPy arrays as lists with superpowers. They support:
  - Multi-dimensional structures (1D, 2D, etc.)
  - Vectorized operations for faster computations
  - Broadcasting to automatically expand arrays for compatible operations
```