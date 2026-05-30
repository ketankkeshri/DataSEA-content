# Pre Commit Hooks

Pre-commit hooks are a powerful way to automate checks and enforce code quality before you even make a commit. As a data engineer, integrating these hooks into your workflow can save you from introducing bugs and maintain consistency across your codebase.

## What are Pre Commit Hooks?

Pre-commit hooks are scripts that run automatically before a commit is finalized. They allow you to validate your code, run tests, or format your files to adhere to your team's coding standards. This ensures that only high-quality code makes it into your repository.

### Setting Up Pre Commit Hooks

To get started with pre-commit hooks, you can use a tool called `pre-commit`. It allows you to manage and maintain multi-language pre-commit hooks easily. Here’s how to set it up:

1. **Install pre-commit**:
   ```bash
   pip install pre-commit
   ```

2. **Create a `.pre-commit-config.yaml` file** in your repository:
   ```yaml
   repos:
     - repo: https://github.com/pre-commit/pre-commit-hooks
       rev: v3.4.0
       hooks:
         - id: trailing-whitespace
         - id: end-of-file-fixer
         - id: check-yaml
   ```

3. **Install the hooks**:
   Run the following command to install the hooks specified in your config file:
   ```bash
   pre-commit install
   ```

Now, every time you make a commit, the specified hooks will run. 

## Examples of Useful Hooks

Here are some common hooks you might want to include:

- **Trailing Whitespace**: Removes any extra spaces at the end of lines.
- **End of File Fixer**: Ensures there's a newline character at the end of files.
- **Check YAML**: Validates the YAML files for syntax errors.

### Creating a Custom Hook

You can also create your own custom hook. Here’s a simple example that checks for Python syntax errors:

1. **Create a script named `check_syntax.py`**:
   ```python
   #!/usr/bin/env python
   import sys
   import os

   def main():
       for filename in sys.argv[1:]:
           if filename.endswith('.py'):
               with open(filename) as f:
                   try:
                       compile(f.read(), filename, 'exec')
                   except SyntaxError as e:
                       print(f"Syntax error in {filename}: {e}")
                       sys.exit(1)

   if __name__ == "__main__":
       main()
   ```

2. **Modify your `.pre-commit-config.yaml`** to include this custom hook:
   ```yaml
   -   id: check-python-syntax
       name: Check Python Syntax
       entry: python check_syntax.py
       language: python
       types: [python]
   ```

## Common pitfalls

- **Not installing hooks**: Remember to run `pre-commit install` after creating or updating your hook configuration.
- **Ignoring exit codes**: If a hook fails, the commit will be aborted. Ensure your hooks return the correct exit codes to avoid confusion.
- **Overloading with too many hooks**: Too many hooks can slow down your commit process. Keep them meaningful and necessary.

## In a nutshell

- Pre-commit hooks automate code checks before commits.
- Use the `pre-commit` tool to manage hooks easily.
- Common hooks include trailing whitespace removal and YAML validation.
- You can create custom hooks for specific needs.
- Ensure hooks are efficient to maintain a smooth workflow.