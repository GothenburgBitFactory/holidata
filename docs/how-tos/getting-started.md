# Getting Started with Holidata

This document provides step-by-step instructions for checking out the holidata repository, setting up a development environment, installing dependencies, running the holidata script, and executing the test suite.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Git
- Python 3.10 or higher
- pip (Python package installer)

## Step 1: Checkout the Repository

Clone the holidata repository from GitHub:

```bash
git clone https://github.com/GothenburgBitFactory/holidata.git
cd holidata
```

## Step 2: Create a Virtual Environment

It's recommended to use a virtual environment to isolate project dependencies:

```bash
# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

When the virtual environment is activated, your terminal prompt will be prefixed with `(venv)`.

When you're done working on the project, you can deactivate the virtual environment by simply calling:

```bash
deactivate
```

## Step 3: Install Dependencies

### Install Runtime Dependencies

Install the core holidata library and its runtime dependencies:

```bash
# Install the package in development mode
pip install -e .
```

This installs the package in "editable" mode, meaning changes to the source code will be reflected without reinstalling.

## Step 4: Run the Holidata Script

Once installed, you can use the `holidata` command-line tool to generate holiday data.

Holiday data is always generated for a specific year and a specific locale.
A locale is a combination of a language and a country, e.g. the call for Germany ([ISO 3166-1 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) `DE`) in language German ([ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) `de`) for the year `2024` looks like this:

```bash
holidata --year=2024 --locale=de-DE
```

Country and language can also be supplied as separate arguments:

```bash
holidata --year=2024 --country=DE --lang=de
```

If the country has a default language defined, or if there is only one locale available, the `--lang` parameter can be omitted:

```bash
holidata --year=2024 --country=DE
```

Use `--help` to see all command line options:
```bash
holidata --help
```

## Step 5: Run the Test Suite

The holidata project uses [pytest](https://pytest.org) for testing with snapshot testing via [syrupy](https://syrupy-project.github.io/syrupy/).

### Install Test Dependencies

Before running the tests, ensure you have the additional dependencies installed:

```bash
pip install -e '.[test]'
```

### Run the Test Suite

To run the test suite, simply call:

```bash
pytest
```

### Update Snapshot Files

When adding new countries or modifying existing ones, you may need to generate new snapshot files:

```bash
pytest --snapshot-update
```

## Next Steps

After setting up your environment, take a look at how to [add a new country](add-country.md) or how to [define a holiday](define-holidays.md).
