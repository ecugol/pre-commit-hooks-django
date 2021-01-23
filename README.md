pre-commit-hooks-django
================

Some useful hooks for Django development

See also: https://github.com/pre-commit/pre-commit

### Using pre-commit-hooks-django with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/ecugol/pre-commit-hooks-django
    rev: v0.3.0  # Use the ref you want to point at
    hooks:
    -   id: check-untracked-migrations
        # Optional, if specified, hook will work only on these branches
        # otherwise it will work on all branches
        args: ["--branches", "main", "other_branch"]
    -   id: check-unapplied-migrations
    -   id: po-location-format
        # Mandatory, select one of the following options:
        # file: show only the file path as location
        # never: remove all locations
        args: ["--add-location", "file"]
```

### Hooks available

#### `check-untracked-migrations`

Forbids commit if untracked migrations files are found (e.g. `*/migrations/0001_initial.py`)

##### Options:
    --branches

    Optional, if specified, hook will work only on these branches
    otherwise it will work on all branches

#### `check-unapplied-migrations`

*WARNING: USE ONLY WITH DJANGO > v3.1*

Check for unapplied migrations with manage.py migrate --check

#### `po-location-format`

Changes location format for .po files

##### Options:

    --add-location [file, never]

    Mandatory, select one of the following options:

    file: show only the file path as location
    never: remove all locations
