```markdown
# Git Workflows — Cheatsheet

## Section 1: Key Concepts

| Thing               | Syntax                             | Notes                                                      |
|---------------------|------------------------------------|------------------------------------------------------------|
| Trunk Branch        | `main` or `master`                 | Central branch for integration.                             |
| Feature Branch      | `feature/branch-name`              | Created from trunk to develop new features.                |
| Git Flow            | `git flow init`                    | Initializes Git Flow in your repository.                   |
| Pull Request        | `git push origin feature/branch`   | Request to merge changes into trunk after code review.     |
| Rebase              | `git rebase main`                  | Integrates changes from trunk into your branch linearly.   |
| Merge               | `git merge feature/branch`          | Combines changes from one branch into another.             |
| Conflict Resolution  | Manual editing, then `git add`    | Resolve conflicts and stage changes before committing.     |

## Section 2: Common Operations

```bash
# Create a new feature branch
git checkout -b feature/my-new-feature

# Push feature branch to remote
git push -u origin feature/my-new-feature

# Create a pull request (using GitHub CLI)
gh pr create --base main --head feature/my-new-feature --title "My New Feature" --body "Description of the feature."

# Rebase your feature branch onto main
git fetch origin
git rebase origin/main

# Merge feature branch into main
git checkout main
git merge feature/my-new-feature

# Resolve conflicts
# Edit files to fix conflicts, then:
git add <resolved-file>
git commit
```

## Gotchas

- ⚠️ Always pull the latest changes from the main branch before rebasing.
- ⚠️ Rebasing rewrites history; avoid rebasing public branches.
- ⚠️ Use descriptive commit messages to clarify PR changes.

## Mental model

1. **Branching Strategy**: Keep the trunk clean; use feature branches for development.
2. **Merge vs. Rebase**: Choose merge for preserving history, rebase for a linear history.
3. **Conflict Handling**: Always resolve conflicts before merging or pushing to avoid integration issues.
```