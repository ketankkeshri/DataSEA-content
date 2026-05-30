```markdown
# Linux Fundamentals — Cheatsheet

## [Section 1: File System Basics]

| Thing           | Syntax                      | Notes                          |
|-----------------|-----------------------------|--------------------------------|
| List files      | `ls`                        | Shows files in current dir.    |
| Change dir      | `cd <directory>`            | Navigate to specified directory.|
| Current dir     | `pwd`                       | Prints the current working dir. |
| Create dir      | `mkdir <directory>`         | Creates a new directory.       |
| Remove file     | `rm <file>`                 | Deletes a file.               |
| Remove dir      | `rmdir <directory>`         | Deletes an empty directory.    |

## [Section 2: Permissions]

| Thing                       | Syntax                           | Notes                                  |
|-----------------------------|----------------------------------|----------------------------------------|
| View permissions            | `ls -l`                          | Lists files with permissions details.  |
| Change permissions          | `chmod <mode> <file>`           | Change file permissions (e.g., `chmod 755 file.txt`). |
| Change ownership            | `chown <user>:<group> <file>`   | Change file owner/group (e.g., `chown user:group file.txt`). |

## [Section 3: Processes]

| Thing                       | Syntax                           | Notes                                  |
|-----------------------------|----------------------------------|----------------------------------------|
| List processes              | `ps aux`                        | Shows all running processes.           |
| Kill process                | `kill <PID>`                    | Terminates process with specified PID. |
| Background process          | `<command> &`                   | Runs command in the background.       |
| Bring process to foreground | `fg %<job_id>`                  | Brings background process to foreground. |

## [Section 4: Networking]

| Thing                       | Syntax                           | Notes                                  |
|-----------------------------|----------------------------------|----------------------------------------|
| Check IP address            | `ip addr`                        | Displays IP address and details.      |
| Test connectivity           | `ping <hostname>`               | Pings a hostname to check reachability. |
| Download file               | `curl -O <URL>`                 | Downloads a file from a URL.         |

## [Section 5: systemd]

| Thing                       | Syntax                           | Notes                                  |
|-----------------------------|----------------------------------|----------------------------------------|
| Start service               | `sudo systemctl start <service>`| Starts a service.                      |
| Stop service                | `sudo systemctl stop <service>` | Stops a service.                       |
| Check service status        | `sudo systemctl status <service>`| Displays the status of a service.     |

## [Gotchas]

- ⚠️ Be careful with `rm` — files are permanently deleted without confirmation.
- ⚠️ Use `sudo` cautiously; it gives elevated privileges that can affect system stability.

## [Mental model]

- **File permissions**: `rwx` (Read, Write, Execute) mapped to user, group, others.
- **Processes**: Parent-Child relationship, where processes can spawn subprocesses.
- **Networking**: Always check IP and connectivity before troubleshooting services.
```