# Basics

Understanding Git is crucial for data engineers as it helps in version control, collaboration, and maintaining the integrity of data pipelines and projects. This lesson covers the fundamentals of Git, so you can effectively manage your code and collaborate with your team.

## What is Git?

Git is a distributed version control system that allows multiple developers to work on a project simultaneously without stepping on each other's toes. It's widely used in software development and data engineering to track changes, revert to previous stages, and create branches for new features or experiments.

### Key Concepts

- **Repository (Repo)**: This is where your project lives. It contains all your project files and the history of changes made to those files.
- **Commit**: A snapshot of your project at a certain point in time. Each commit has a unique identifier (hash) and a message describing what changed.
- **Branch**: A parallel version of your project. You can create a branch to experiment with new features without affecting the main project.
- **Merge**: The process of integrating changes from one branch into another.

## Getting Started with Git

Before diving into Git commands, you'll want to set up Git on your machine. Here’s how:

1. **Install Git**:
   - On Windows, download Git from [git-scm.com](https://git-scm.com/).
   - On macOS, you can use Homebrew: `brew install git`.
   - On Linux, use your package manager, e.g., `sudo apt install git` for Ubuntu.

2. **Initialize a Git Repository**:
   To start using Git, you need to initialize a repository in your project folder:

   ```bash
   mkdir my_data_project
   cd my_data_project
   git init
   ```

3. **Making Your First Commit**:
   Create a new file and make your first commit:

   ```bash
   echo "print('Hello, Data Engineering!')" > hello.py
   git add hello.py
   git commit -m "Initial commit: add hello.py"
   ```

4. **Viewing Commit History**:
   To see the history of your commits, use:

   ```bash
   git log
   ```

This command shows a list of all your commits, along with their hashes and messages.

## Collaborating with Others

Git shines in team environments. Here’s how you can collaborate:

1. **Cloning a Repository**:
   If you want to work on an existing project, you can clone it:

   ```bash
   git clone https://github.com/username/repo.git
   ```

2. **Pushing Changes**:
   Once you've made changes, you can push them back to the remote repository:

   ```bash
   git add .
   git commit -m "Your message here"
   git push origin main
   ```

3. **Pulling Updates**:
   To stay updated with changes made by others, pull the latest changes:

   ```bash
   git pull origin main
   ```

## Common pitfalls

- **Forgetting to Commit**: Regularly commit your changes. If you make too many changes without committing, you risk losing work.
- **Merge Conflicts**: When multiple changes are made to the same line of a file, Git will throw a merge conflict. Always resolve these before pushing.
- **Not Using Branches**: Avoid working directly on the main branch. Always create a new branch for features or experiments to maintain a clean project history.

## In a nutshell

- Git is essential for version control in data engineering.
- Initialize your repo with `git init` and start committing changes.
- Use branches for experimentation and collaboration.
- Regular commits and updates are key to avoiding headaches in team projects.