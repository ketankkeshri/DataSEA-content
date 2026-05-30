```markdown
# Shell Scripting — Cheatsheet

## [Section 1: Variables & Flow Control]

| Thing               | Syntax                     | Notes                               |
|---------------------|----------------------------|-------------------------------------|
| Assign variable      | `VAR_NAME=value`           | No spaces around `=`.               |
| Access variable      | `$VAR_NAME`                | Use `$` to reference the variable.  |
| Conditional (if)     | `if [ condition ]; then ... fi` | Use `[` for test conditions.       |
| Loop (for)           | `for item in list; do ... done` | Iterate over items in a list.     |
| Loop (while)         | `while [ condition ]; do ... done` | Continues while the condition is true. |

## [Section 2: Pipes & Redirects]

```bash
# Redirect output to a file
command > output.txt

# Append output to a file
command >> output.txt

# Pipe output from one command to another
command1 | command2
```

## [Section 3: Searching & Text Processing]

| Tool    | Command                      | Notes                               |
|---------|------------------------------|-------------------------------------|
| find    | `find /path -name "*.txt"`  | Search for files by name.          |
| grep    | `grep "pattern" file.txt`    | Search for a pattern in a file.    |
| awk     | `awk '{print $1}' file.txt`  | Print the first column of a file.  |

## [Section 4: Scheduling Tasks]

| Tool    | Command                      | Notes                               |
|---------|------------------------------|-------------------------------------|
| cron    | `crontab -e`                 | Edit cron jobs.                    |
| Schedule| `* * * * * /path/to/script.sh` | Format for cron jobs (min, hour, day, month, week). |

## [Section 5: Debugging]

```bash
# Enable debugging
set -x

# Disable debugging
set +x
```

## [Gotchas]

- ⚠️ Be careful with variable names; they are case-sensitive.
- ⚠️ Use quotes around variables to prevent word splitting: `"$VAR_NAME"`.
- ⚠️ Always check the exit status of commands with `$?` for error handling.

## [Mental model]

- **Variables** store data (use `$` to access).
- **Pipes** connect commands (output of one is input to another).
- **Redirects** send output to files instead of the console.
```