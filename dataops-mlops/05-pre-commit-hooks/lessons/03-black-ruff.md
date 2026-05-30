# Black Ruff

Pre-commit hooks can save your life as a Data Engineer or Data Scientist by automating quality checks before code gets pushed to the repository. Let’s dive into how you can set up pre-commit hooks to catch issues early and maintain clean data repositories.

## What are Pre-commit Hooks?

Pre-commit hooks are scripts that run automatically before a commit is finalized in Git. They allow you to enforce rules, run tests, and prevent problematic code from entering your repository.

### Why Use Pre-commit Hooks?

- **Catch Errors Early:** They help identify syntax errors, formatting issues, and other problems before code is shared.
- **Maintain Standards:** Ensure your team adheres to coding standards and practices.
- **Automate Checks:** Save time by automating tasks like linting and testing.

## Setting Up Pre-commit Hooks

To set up your pre-commit hooks, you'll use the `pre-commit` framework. Here’s how:

### Step 1: Install pre-commit

First, you need to install the `pre-commit` package. You can do this using pip:

```bash
pip install pre-commit
```

### Step 2: Create a Configuration File

Next, create a `.pre-commit-config.yaml` file in the root of your repository. Here’s a sample configuration:

```yaml
repos:
  - repo: https://github.com/sqlfluff/sqlfluff
    rev: v0.9.2
    hooks:
      - id: sqlfluff-lint
        args: [--dialect, postgres]
  - repo: https://github.com/psf/black
    rev: 21.12b0
    hooks:
      - id: black
```

### Step 3: Install the Hooks

After configuring, run the following command to install the hooks specified in the configuration file:

```bash
pre-commit install
```

This command sets up your Git hooks, and they will run automatically on each commit.

### Step 4: Test Your Setup

Create a Python file with some poorly formatted code:

```python
def test_function(  ):
 print("Hello, World!")


```

Try to commit this file. If everything is set up correctly, `black` will automatically reformat the code, and `sqlfluff` will check your SQL files for issues.

## Common pitfalls

- **Not Installing Hooks:** Forgetting to run `pre-commit install` means your hooks won’t run.
- **Misconfigured YAML:** A small typo in `.pre-commit-config.yaml` can prevent hooks from executing.
- **Ignoring Warnings:** Sometimes developers override hooks or ignore warnings, leading to a messy codebase.

## In a nutshell

- Pre-commit hooks run scripts before commits to enforce code quality.
- They help catch errors, maintain coding standards, and automate checks.
- Setting up pre-commit is as simple as installing the package and configuring `.pre-commit-config.yaml`.
- Common pitfalls include not installing hooks, misconfigured files, and ignoring hook warnings.