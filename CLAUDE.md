# foreman-proof-python

A tiny Python package used to prove Foreman on a non-Node project.

## Rules

- Tests first: every behaviour gets a pytest test in `tests/` before its implementation.
- Standard library only at runtime; pytest is the only dev dependency.
- Small, pure, type-hinted functions with a one-line docstring.
- `uv run pytest` must pass before every commit.
