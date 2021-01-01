pre-commit-hooks
================

Some useful hooks for Django development

See also: https://github.com/pre-commit/pre-commit

### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/ecugol/pre-commit-hooks
    rev: v0.2.0  # Use the ref you want to point at
    hooks:
    -   id: check-untracked-migrations
        # Optional, if specified, hook will work only on these branchesm
        # otherwise it will work on all branches
        args: ["--branches", "main", "other_branch"]
```

### Hooks available

#### `check-untracked-migrations`

Forbids commit if untracked migrations files are found (e.g. `*/migrations/0001_initial.py`)
