# How to Add a New Country to Holidata

This document explains how to add a new country to the Holidata library.
We'll use the country code `XY` as an example throughout this guide.

## Overview

> Before adding a new country to holidata, ensure you have set up your development environment following these [initial setup](getting-started.md) steps.

Adding a new country to holidata involves creating a new Python package that defines the country's holidays according to the holidata framework.
Each country is represented by a class that inherits from the `Country` base class and implements the necessary attributes.

## Step 1: Create the Country Package

Create a new directory in the `src/holidata/holidays/` directory named after the country's [ISO 3166-1 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) in uppercase (e.g., `XY`):

```
src/holidata/holidays/XY/
```

Inside this directory, create an `__init__.py` file:

```
src/holidata/holidays/XY/__init__.py
```

## Step 2: Define the Country Class

In your new `__init__.py` file, create a class `XY` that inherits from `Country`:

```python
from holidata.holiday import Country

__all__ = [
    "XY",
]


class XY(Country):
    id = "XY"
    languages = ["xy"]

    def __init__(self):
        super().__init__()

        # Holiday definitions will go here
```

Each country class must at least define these attributes:

- `id`: The [ISO 3166-1 alpha-2 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) (e.g., `"XY"`)
- `languages`: A list of [ISO 639-1 alpha-2 language codes](https://en.wikipedia.org/wiki/ISO_639-1) supported by this country (e.g., `["xy"]`)

The combination of country and language defines a 'locale'.
There can be several locales for a country, but each has to define at least one.

## Step 3: Register the Country

Add your country to the main `holidays` module by editing `src/holidata/holidays/__init__.py` and adding:

```python
from .XY import *
```

Make sure to add it in alphabetical order.

## Next Steps

After creating your basic country structure, you can either start with [defining holidays](define-holidays.md),
or [add regions](add-regions.md), especially if your country has (many) regional holidays.
