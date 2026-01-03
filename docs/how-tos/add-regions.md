# How to Add Regions to a Country in Holidata

This document explains how to add regions to countries in the Holidata library.

## Overview

Holidata supports defining holidays for the _principal subdivision_ of a country.
This helps keep regional holidays maintainable by grouping them in separate Python modules.

Use regions especially for holidays defined by regional legislature.

## Step 1: Create Region Modules

Create separate Python modules for each region in the country's package folder:

```
src/holidata/holidays/XY/
├── __init__.py          # Main country definition
├── ABC.py               # First region
├── DEF.py               # Second region
└── ...                  # Additional regions
```

Usually the [ISO 3166-2 codes](https://en.wikipedia.org/wiki/ISO_3166-2) for the principal subdivisions in uppercase are used as region ids and module names.
In this example we use `ABC` and `DEF`.

## Step 2: Define the Region Class

In each region module, create a class, e.g. `ABC`, that inherits from `Region`:

```python
from holidata.holiday import Region


class ABC(Region):
    def __init__(self, country):
        super().__init__("ABC", country)

        # Region holiday definitions will go here
```

## Step 3: Register Regions in Country Class

In your main country `__init__.py`, import and register the regions:

```python
from holidata.holiday import Country
# Import region modules
from holidata.holidays.XY.ABC import ABC
from holidata.holidays.XY.DEF import DEF

__all__ = [
    "XY",
]


class XY(Country):
    id = "XY"
    languages = ["xy"]

    def __init__(self):
        super().__init__()

        # Add regions to the country
        self.regions = [
            ABC(self),
            DEF(self),
        ]
        
        # Country holiday definitions will go here
```

## Next Steps

After having defined regions, now take a look at how to [define holidays](define-holidays.md) in the country and region classes.
