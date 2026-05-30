# Conflict Resolution

Collaboration in data projects often leads to conflicts in code when multiple team members work on different parts of the same files. Understanding how to resolve these conflicts efficiently is crucial for maintaining workflow and ensuring that your projects stay on track.

## Why Conflicts Happen

Conflicts typically arise during merges when two branches have changes in the same line of code or when one branch modifies a file that another branch has deleted. Here’s a simple example:

- **Branch A** adds a new feature to a Python script.
- **Branch B** makes a bug fix to the same line in that script.

When you try to merge Branch B into Branch A, Git won't know which change to keep, resulting in a conflict.

### Example Scenario

Let’s say you have a Python file called `calculator.py` with the following content:

```python
def add(a, b):
    return a + b
```

- On **Branch A**, you change the `add` function to log the result:

```python
def add(a, b):
    result = a + b
    print(f"Adding {a} and {b} gives {result}")
    return result
```

- On **Branch B**, you change the return statement to add error handling:

```python
def add(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers.")
    return a + b
```

When you try to merge Branch B into Branch A, Git will flag a conflict. 

## How to Resolve Conflicts

Resolving conflicts in Git can be done through the command line or GUI tools. Here’s a quick guide on how to do it via the command line:

1. **Identify the Conflict**: After attempting to merge, Git will mark the conflicting files. You can check this with:

    ```bash
    git status
    ```

2. **Open the Conflicted File**: Open `calculator.py`. You’ll see conflict markers like this:

    ```python
    <<<<<<< HEAD
    result = a + b
    print(f"Adding {a} and {b} gives {result}")
    =======
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers.")
    >>>>>>> branch-b
    ```

3. **Edit the File**: Decide how to merge the changes. For our example, you might choose to combine both changes:

    ```python
    def add(a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Both arguments must be numbers.")
        result = a + b
        print(f"Adding {a} and {b} gives {result}")
        return result
    ```

4. **Mark as Resolved**: After editing, save the file and mark the conflict as resolved:

    ```bash
    git add calculator.py
    ```

5. **Complete the Merge**: Finally, complete the merge:

    ```bash
    git commit -m "Resolved merge conflict in calculator.py"
    ```

## Common pitfalls

- **Ignoring Conflict Markers**: Forgetting to resolve the markers can lead to broken code.
- **Not Testing After Merge**: Always run tests after resolving conflicts to ensure functionality.
- **Overwriting Changes**: Be careful while resolving to not lose important changes from either branch.

## In a nutshell

- Conflicts occur when changes overlap in multiple branches.
- Identify, edit, and resolve conflicts in your code.
- Always test after resolving to ensure everything works.
- Keep your team informed about conflict resolution decisions.
- Use tools (like `git mergetool`) to help visualize and resolve conflicts effectively.