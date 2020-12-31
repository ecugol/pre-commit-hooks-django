pre-commit-hooks
================

Some useful hooks for Django development

See also: https://github.com/pre-commit/pre-commit

### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/ecugol/pre-commit-hooks
    rev: 0.1.0  # Use the ref you want to point at
    hooks:
    -   id: check-untracked-migrations
```

### Hooks available

#### `check-untracked-migrations`

Forbids commit if untracked migrations files are found (e.g. `*/migrations/0001_initial.py`)
