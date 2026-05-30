# Intro

Shell scripting is an essential skill for data engineers, enabling you to automate tasks, manipulate data, and streamline workflows. Whether you're processing large datasets or managing server operations, mastering shell scripts can save you time and reduce errors.

## What is Shell Scripting?

Shell scripting involves writing a series of commands for the shell, the command-line interface of your operating system. It allows you to automate repetitive tasks, manage files, and execute complex command sequences. By using shell scripts, you can:

- Simplify data processing tasks.
- Automate deployment and maintenance of data pipelines.
- Enhance productivity by reducing manual work.

Common shells include Bash, Zsh, and Fish, with Bash being the most widely used. In this lesson, we will focus on Bash scripting.

## Basic Syntax and Structure

Bash scripts are plain text files with a `.sh` extension. They start with a shebang (`#!/bin/bash`), which tells the system that this file should be executed using the Bash shell. Here’s a simple example that prints "Hello, DataSEA!" to the console:

```bash
#!/bin/bash
echo "Hello, DataSEA!"
```

### Creating and Running a Script

1. **Create a new file**:
   ```bash
   touch hello_data_sea.sh
   ```

2. **Open it in a text editor** (like `nano` or `vim`):
   ```bash
   nano hello_data_sea.sh
   ```

3. **Add the shebang and echo command**:
   ```bash
   #!/bin/bash
   echo "Hello, DataSEA!"
   ```

4. **Make the script executable**:
   ```bash
   chmod +x hello_data_sea.sh
   ```

5. **Run the script**:
   ```bash
   ./hello_data_sea.sh
   ```

This should output:
```
Hello, DataSEA!
```

### Variables in Shell Scripts

Variables are fundamental in shell scripting, allowing you to store and manipulate data. Here’s how you can define and use a variable:

```bash
#!/bin/bash
name="DataSEA"
echo "Welcome to $name!"
```

### Conditional Statements

Conditional statements let you perform different actions based on conditions. Here's an example using an `if` statement:

```bash
#!/bin/bash
value=10

if [ $value -gt 5 ]; then
  echo "Value is greater than 5."
else
  echo "Value is 5 or less."
fi
```

## Common pitfalls

- **Not using quotes**: Failing to quote variables can lead to unexpected behavior, especially with spaces.
- **Incorrect permissions**: Forgetting to make your script executable will result in a "Permission denied" error.
- **Syntax errors**: A missing semicolon or mismatched brackets can cause your script to fail silently.

## In a nutshell

- Shell scripting automates tasks and improves efficiency.
- Scripts start with a shebang and can include commands, variables, and conditionals.
- Always check for common pitfalls to avoid frustrating debugging sessions.
- Mastering shell scripting is a key skill for data engineers working with data pipelines and automation.