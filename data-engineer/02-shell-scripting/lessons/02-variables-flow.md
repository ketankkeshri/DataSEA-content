# Variables Flow

Understanding how to use variables in shell scripting is crucial for any Data Engineer. Variables allow you to store data, manipulate it, and make your scripts dynamic and powerful.

## What are Variables?

In shell scripting, a variable is a named storage location for data. You can think of it as a container that holds information you want to use later. For example, you might store the path to a directory or the result of a command in a variable. 

### Declaring Variables

To declare a variable, simply choose a name and assign a value without spaces around the `=` sign. Here’s how you do it:

```bash
my_variable="Hello, DataSEA!"
```

You can access the variable by prefixing it with a dollar sign:

```bash
echo $my_variable
```

### Best Practices for Naming Variables

- Use lowercase letters and underscores (e.g., `my_variable`).
- Avoid spaces and special characters.
- Make names descriptive to improve readability.

### Example: Using Variables in a Script

Let’s look at a simple script that uses variables to manage file backups:

```bash
#!/bin/bash

# Declare variables
source_directory="/path/to/source"
backup_directory="/path/to/backup"
timestamp=$(date +"%Y%m%d_%H%M%S")

# Create a backup
cp -r "$source_directory" "$backup_directory/backup_$timestamp"
echo "Backup created at $backup_directory/backup_$timestamp"
```

In this example:
- We declare `source_directory` and `backup_directory` to store paths.
- We use the `date` command to create a timestamp for the backup filename.
- The `cp` command copies the files, utilizing the variables.

## Variable Types

### Environment Variables

Environment variables are system-wide variables that affect processes and shell sessions. You can create them using the `export` command:

```bash
export MY_ENV_VAR="This is an environment variable"
```

You can access it the same way:

```bash
echo $MY_ENV_VAR
```

### Local Variables

Local variables are defined and used within the current shell session or script. They are not accessible outside of that context unless explicitly exported.

### Read-Only Variables

You can create read-only variables, which cannot be modified after their initial assignment. This is useful for constants:

```bash
readonly MY_CONSTANT="Constant Value"
```

## Common pitfalls

- **Not quoting variables:** Omitting quotes may lead to unexpected behavior, especially with spaces. Always use quotes: `"$my_variable"`.
- **Overwriting variables:** Be cautious of using common names; avoid overwriting important environment variables.
- **Scope confusion:** Remember that local variables do not persist outside the script or session unless exported.

## In a nutshell

- Variables are essential for storing and manipulating data in shell scripts.
- Use descriptive names and follow best practices for variable naming.
- Understand the difference between environment, local, and read-only variables.
- Always quote variables to prevent issues with spaces and special characters.