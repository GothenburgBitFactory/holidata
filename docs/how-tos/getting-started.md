# Getting Started with Holidata

This document provides step-by-step instructions for checking out the holidata repository, setting up a development environment, installing dependencies, running the holidata script, and executing the test suite.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- [Git](https://git-scm.com)
- [uv](https://docs.astral.sh/uv/)

Using `uv` is the recommended way to work with holidata.
It manages the Python interpreter, virtual environment, and dependencies automatically based on [`pyproject.toml`](../pyproject.toml) and [`.python-version`](../.python-version).

## Step 1: Checkout the Repository

Clone the holidata repository from GitHub:

```bash
git clone https://github.com/GothenburgBitFactory/holidata.git
cd holidata
```

## Step 2: Sync Dependencies

From the project root, let `uv` set up everything (the pinned Python version, a virtual environment, and all dependencies):

```bash
uv sync
```

This reads `pyproject.toml` and creates a `.venv` in the project directory, installing runtime dependencies plus the `dev` dependency group (test and linting tools).
If you only need the runtime dependencies, you can run `uv sync --no-dev` instead.

## Step 3: Run the Holidata Script

Once synced, use `uv run` to invoke the `holidata` command-line tool to generate holiday data.

Holiday data is always generated for a specific year and a specific locale.
A locale is a combination of a language and a country, e.g. the call for Germany ([ISO 3166-1 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) `DE`) in language German ([ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) `de`) for the year `2026` looks like this:

```bash
uv run holidata --year=2026 --locale=de-DE
```

Country and language can also be supplied as separate arguments:

```bash
uv run holidata --year=2026 --country=DE --lang=de
```

If the country has a default language defined, or if there is only one locale available, the `--lang` parameter can be omitted:

```bash
uv run holidata --year=2026 --country=DE
```

Use `--help` to see all command line options:
```bash
uv run holidata --help
```

## Step 4: Run the Test Suite

The holidata project uses [pytest](https://pytest.org) for testing with snapshot testing via [syrupy](https://syrupy-project.github.io/syrupy/).

### Run the Test Suite

To run the test suite, simply call:

```bash
uv run pytest
```

### Update Snapshot Files

When adding new countries or modifying existing ones, you may need to generate new snapshot files:

```bash
uv run pytest --snapshot-update
```

## Step 5: Code Quality and Linting

The holidata project uses [ruff](https://docs.astral.sh/ruff/) for linting and code formatting, and [mypy](https://mypy-lang.org/) for static type checking. Both are run via `uv run`.

### Run Ruff

To check your code for style and import issues:

```bash
uv run ruff check .
```

To automatically fix issues where possible:

```bash
uv run ruff check --fix .
```

### Run MyPy

To perform static type checking:

```bash
uv run mypy src/
```

### Running All Checks

The project's CI pipeline runs both linting tools. Before submitting a pull request, ensure both checks pass:

```bash
uv run ruff check . && uv run mypy src/
```

## Next Steps

After setting up your environment, take a look at how to [add a new country](add-country.md) or how to [define a holiday](define-holidays.md).
