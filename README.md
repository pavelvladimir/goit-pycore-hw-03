# goit-pycore-hw-03

This repository is set up for `uv` and organized so each homework assignment can live in its own module. It also includes a documentation stack based on `pnpm`, Docusaurus, and Sphinx-generated API pages.

## Project Structure

```text
goit-pycore-hw-03/
├── main.py
├── pyproject.toml
├── package.json
├── pnpm-lock.yaml
├── pnpm-workspace.yaml
├── README.md
├── .gitignore
├── uv.lock
├── goit_pycore_hw_03/
│   ├── __init__.py
│   └── task_01.py
├── sphinx/
│   ├── conf.py
│   ├── index.rst
│   └── api.rst
├── tests/
│   └── test_task_01.py
└── website/
    ├── docs/
    ├── src/
    ├── docusaurus.config.js
    ├── package.json
    └── sidebars.js
```

## Task 1

The module [goit_pycore_hw_03/task_01.py](goit_pycore_hw_03/task_01.py) contains the `get_days_from_today(date)` function.

It:

- accepts a date string in `YYYY-MM-DD` format
- returns the number of days between the given date and today
- returns a negative number when the given date is in the future
- raises `ValueError` for an invalid date format

## Run

The entry point in [main.py](main.py) asks for a date and prints the difference in days.

```bash
uv run python main.py
```

Example input:

```text
2021-10-09
```

## Tests

Run the test suite with:

```bash
uv run python -m unittest discover -s tests -q
```

## Documentation

The documentation setup uses:

- `pnpm` for the Docusaurus site in `website/`
- `uv` for Python tooling
- `Sphinx` to generate API reference from Python docstrings

Install dependencies:

```bash
pnpm install
uv sync --group docs
```

Start the docs site locally:

```bash
pnpm docs:start
```

Build the static docs output:

```bash
pnpm docs:build
```
