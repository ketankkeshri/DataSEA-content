# Pipes Redirects

Pipes and redirects are essential tools in shell scripting that allow you to manage data flow between commands. For data engineers, mastering these concepts enhances your ability to manipulate and process data efficiently in a Unix/Linux environment.

## Understanding Pipes

Pipes (`|`) enable you to take the output of one command and use it as the input for another. This allows for powerful command chaining without the need for temporary files. 

### Example of Using Pipes

Consider a scenario where you want to count the number of lines in a log file that contain the word "error". You could do this using `grep` and `wc` like so:

```bash
grep "error" /var/log/syslog | wc -l
```

In this example:
- `grep "error" /var/log/syslog` filters lines containing "error".
- The output is then piped (`|`) to `wc -l`, which counts those lines.

This method is efficient and avoids the clutter of intermediate files.

## Redirects: Input and Output

Redirects allow you to control where the command's output goes (standard output) and where it gets its input from (standard input). 

### Output Redirection

You can redirect the output of a command to a file using `>`. For instance, if you want to save the list of users on the system into a file called `users.txt`, you would do:

```bash
cat /etc/passwd > users.txt
```

If you want to append to a file instead of overwriting it, use `>>`:

```bash
echo "New User" >> users.txt
```

### Input Redirection

You can also redirect input from a file using `<`. For example, if you want to read from a file instead of typing out commands, you can use:

```bash
sort < unsorted_numbers.txt
```

This command sorts the contents of `unsorted_numbers.txt` without you needing to type them.

## Common pitfalls

- **Overwriting files unintentionally**: Using `>` will erase the contents of the file if it exists. Always check before running.
- **Not using quotes**: When your search term has spaces, forgetting quotes can lead to errors or unexpected results.
- **Chaining too many commands**: While it's powerful to chain commands, too many pipes can make debugging difficult. Keep it simple.

## In a nutshell

- Pipes (`|`) connect the output of one command to the input of another.
- Use `>` to redirect output to a file, and `>>` to append.
- Input can be redirected using `<` for reading from files.
- Be cautious of overwriting files and remember to use quotes for multi-word strings.
- Keep command chains manageable to simplify debugging.