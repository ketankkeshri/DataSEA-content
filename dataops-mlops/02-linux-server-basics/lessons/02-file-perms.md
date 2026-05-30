# File Perms

Understanding file permissions in Linux is crucial for anyone working in DataOps or MLOps. Proper file permissions help protect sensitive data and ensure that only authorized users can access or modify files.

## File Permission Basics

In Linux, every file and directory has three types of permissions: **read (r)**, **write (w)**, and **execute (x)**. These permissions can be assigned to three categories of users:

- **Owner**: The user who created the file.
- **Group**: A set of users that share access to the file.
- **Others**: All other users on the system.

You can view file permissions using the `ls -l` command. Here's how it looks:

```bash
$ ls -l myfile.txt
-rw-r--r-- 1 user group 0 Oct 10 10:00 myfile.txt
```

In this example:
- The first character (`-`) indicates it's a regular file (a `d` would indicate a directory).
- The next three characters (`rw-`) show the owner's permissions (read and write).
- The next three (`r--`) show the group's permissions (read only).
- The last three (`r--`) indicate permissions for others (read only).

## Modifying File Permissions

You can change file permissions using the `chmod` command. Here's how to use it:

```bash
$ chmod u+x myfile.txt  # Adds execute permission for the owner
$ chmod g-w myfile.txt  # Removes write permission for the group
$ chmod o+r myfile.txt  # Adds read permission for others
```

You can also use numerical notation to set permissions. The permissions are represented by numbers:
- **Read (4)**
- **Write (2)**
- **Execute (1)**

For example, to set read and write permissions for the owner and read for the group and others, you would use:

```bash
$ chmod 644 myfile.txt
```

This breaks down to:
- Owner: 6 (4 for read + 2 for write)
- Group: 4 (read only)
- Others: 4 (read only)

## Common pitfalls

- **Ignoring permissions**: Always check file permissions when sharing files or directories; you might expose sensitive data.
- **Over-permissioning**: Giving write permissions to the group or others can lead to accidental data loss or corruption.
- **Not using `umask`**: If you don't set a default `umask`, newly created files might have overly permissive settings.

## In a nutshell

- File permissions in Linux manage access to files and directories.
- Use `ls -l` to view permissions and `chmod` to modify them.
- Understand the difference between user, group, and others to maintain security.
- Be cautious of common pitfalls to prevent unauthorized access or data loss.