# Python Monorepo

todo

## Features

- [x] Black
- [x] Flake8
- [x] Isort
- [ ] Mypy
- [ ] Pytest

## Settings Hierachy

Folder `settings.json` overwrites `.workspace` settings
`.workspace` settings overwrites user `settings.json` (CMD + ,)

## Guidelines

- Everything must work without VS Code by using the command line
- `.venv` folder in every package and project to separate dependencies
- `pyproject.toml` to define package meta data and abstract dependencies
- `pyproject.toml` to define tooling configurationsn (black, flake8, isort, ...)
- Packages needs to be namespaced by a prefix (e.g. `abc_`)
- Package or project must work on its own without monorepo setup