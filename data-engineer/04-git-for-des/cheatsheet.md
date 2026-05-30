```markdown
# Git for Data Engineers — Cheatsheet

## [Section 1: Core syntax]

| Thing                | Syntax                     | Notes                                          |
|----------------------|----------------------------|------------------------------------------------|
| Initialize repo      | `git init`                 | Creates a new Git repository.                  |
| Clone repo           | `git clone <url>`          | Clones a remote repository to your local machine. |
| Check status         | `git status`               | Shows the status of changes as untracked, modified, or staged. |
| Add changes          | `git add <file>`           | Stages changes for the next commit. Use `.` for all changes. |
| Commit changes       | `git commit -m "message"`  | Records the staged changes with a message.    |
| View history         | `git log`                  | Displays the commit history.                   |
| Checkout branch      | `git checkout <branch>`    | Switch to a different branch.                  |
| Create branch        | `git branch <new_branch>`  | Creates a new branch.                          |
| Merge branch         | `git merge <branch>`       | Merges changes from the specified branch into the current branch. |

## [Section 2: Common operations]

```bash
# Create a new branch and switch to it
git checkout -b <new_branch>

# Rebase current branch onto another
git rebase <base_branch>

# Update local repo with remote changes
git pull origin <branch>

# Push changes to remote
git push origin <branch>

# Remove a branch
git branch -d <branch_name>
```

## [Gotchas]

- ⚠️ Always pull changes from the remote before starting a new feature branch to avoid conflicts.
- ⚠️ Avoid rebasing public branches as it rewrites history, which can confuse collaborators.

## [Mental model]

1. **Branching**: Think of branches as parallel universes for your code. Each branch allows you to experiment without affecting the main line of development.
2. **Merging vs. Rebasing**: Merging creates a new commit that combines changes, while rebasing rewrites commit history, making it linear.
3. **Staging Area**: Changes go through a staging area before being committed. Imagine it as a "review zone" before changes are finalized.
```