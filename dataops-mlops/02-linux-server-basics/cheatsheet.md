```markdown
# Linux Server Basics — Cheatsheet

## [Section 1: SSH Basics]

| Thing           | Syntax                     | Notes                               |
|-----------------|----------------------------|-------------------------------------|
| Connect to SSH  | `ssh user@hostname`        | Replace `user` with your username and `hostname` with the server's IP or domain. |
| Copy files      | `scp localfile user@host:remotefile` | Use `scp` to securely copy files to/from a remote server. |
| SSH Keygen      | `ssh-keygen -t rsa`       | Generate a new SSH key pair. Follow prompts for file location and passphrase. |
| SSH Config      | `~/.ssh/config`            | Create or edit this file to simplify SSH commands for different hosts. |

## [Section 2: File Permissions]

| Thing                   | Syntax                   | Notes                                              |
|-------------------------|--------------------------|----------------------------------------------------|
| View permissions        | `ls -l`                  | Lists files with permissions, owner, and group info. |
| Change permissions      | `chmod 755 filename`     | Change permissions: `rwxr-xr-x`. `755` = owner can read/write/execute, others can read/execute. |
| Change owner            | `chown user:group filename` | Change file owner and group.                       |
| Change group            | `chgrp group filename`   | Change the group ownership of a file.              |

## [Section 3: Package Management]

| Thing                   | Syntax                   | Notes                                              |
|-------------------------|--------------------------|----------------------------------------------------|
| Update package list     | `sudo apt update`        | For Debian/Ubuntu-based systems.                   |
| Upgrade packages        | `sudo apt upgrade`       | Upgrades installed packages to the latest versions. |
| Install a package       | `sudo apt install pkgname` | Replace `pkgname` with the package you want to install. |
| Remove a package        | `sudo apt remove pkgname` | Uninstall a package.                               |

## [Section 4: Log Files]

| Thing                   | Syntax                   | Notes                                              |
|-------------------------|--------------------------|----------------------------------------------------|
| View log file           | `cat /var/log/syslog`    | Display system log.                               |
| Tail log file           | `tail -f /var/log/syslog` | Continuously view new log entries.                  |
| Search log file         | `grep 'error' /var/log/syslog` | Search for specific strings in logs.               |

## [Gotchas]

- ⚠️ Ensure your user has permission to execute commands like `sudo`.
- ⚠️ Always check file permissions before sharing sensitive files.
- ⚠️ Log files can grow large; consider log rotation to manage size.

## [Mental model]

- SSH ➡️ Secure access to remote servers.
- Permissions ➡️ Control who can do what with files.
- Package Management ➡️ Keep your system up-to-date and install necessary software.
- Log Files ➡️ Monitor system activity and troubleshoot issues.
```