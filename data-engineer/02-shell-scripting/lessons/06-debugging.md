# Debugging

Debugging is a critical skill for data engineers, helping you quickly identify and fix errors in your shell scripts. Whether it's a typo or a logical flaw, knowing how to debug effectively can save you hours of troubleshooting time.

## Common Debugging Techniques

When debugging shell scripts, there are several techniques you can use to pinpoint the issue.

### 1. Use `set -x`

The `set -x` command enables a mode of the shell where all executed commands are printed to the terminal. This is helpful to trace what your script is doing step-by-step.

```bash
#!/bin/bash
set -x

# Example script that might have an error
for file in *.txt; do
    cat $file
done
```

### 2. Echo Statements

Adding `echo` statements throughout your script can provide insights into variable values and the flow of execution.

```bash
#!/bin/bash

file_path="/path/to/file.txt"
echo "Checking file: $file_path"

if [ -f "$file_path" ]; then
    echo "File exists."
else
    echo "File does not exist."
fi
```

### 3. Check Exit Status

Every command in a shell script has an exit status. You can check the exit status using `$?`. A status of `0` means success, while any other value indicates an error.

```bash
#!/bin/bash

cp source.txt destination.txt
if [ $? -ne 0 ]; then
    echo "Copy failed!"
fi
```

## Debugging Tools

There are several tools available that can help you in debugging shell scripts:

- **ShellCheck**: A static analysis tool that helps identify common issues in shell scripts.
- **Bash Debugger**: A debugger for bash scripts that allows you to set breakpoints and step through your code.

### Using ShellCheck

ShellCheck is a great tool to catch potential issues before running the script. You can install it and run:

```bash
shellcheck your_script.sh
```

## Common pitfalls

- **Not Quoting Variables**: Forgetting to quote variables can lead to unexpected behavior, especially with filenames containing spaces.
- **Ignoring Exit Status**: Failing to check the exit status of commands may result in silent failures.
- **Overusing `set -x`**: While `set -x` is helpful, using it excessively can clutter your output and make it hard to follow.

## In a nutshell

- Use `set -x` to trace your script's execution.
- Add `echo` statements to understand variable values and flow.
- Always check exit statuses to catch errors early.
- Consider tools like ShellCheck to improve script quality.
- Avoid common pitfalls to make debugging easier.