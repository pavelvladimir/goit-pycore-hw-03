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
│   ├── task_01.py
│   └── task_02.py
├── sphinx/
│   ├── conf.py
│   ├── index.rst
│   └── api.rst
├── tests/
│   ├── test_task_01.py
│   └── test_task_02.py
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

## Task 2

The module [goit_pycore_hw_03/task_02.py](goit_pycore_hw_03/task_02.py) contains the `get_numbers_ticket(min, max, quantity)` function.

It:

- validates the allowed lottery range constraints
- returns a sorted list of unique random numbers
- returns an empty list for invalid input values

## Run

The entry point in [main.py](main.py) lets you choose a task and then asks for the required input values.

```bash
uv run python main.py
```

Example flow for Task 1:

```text
1
2021-10-09
```

Example flow for Task 2:

```text
2
1
49
6
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
