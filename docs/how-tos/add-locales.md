# How to Add Additional Languages to a Country in Holidata

This document explains how to add multiple languages to your country implementation.

## Overview

Some countries have multiple official languages, for some users it is helpful to have a translation of the holidays in their language available.
Holidata supports this by allowing you to define holiday names in multiple languages within a country implementation.

## Adding Multiple Languages

For this example we assume we want to add the language `vv` to the example from the guide on [how to add a country](add-country.md).
Use the standard [ISO 639-1 two-letter language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) for the language you want to add.

### Step 1: Update Country Class Attributes

Add the new language code to the list of supported languages in your country class:

```python
class XY(Country):
    id = "XY"
    languages = ["xy", "vv"]  # Add the additional language
    default_lang = "xy"       # Optionally, specify the default language

    def __init__(self):
        super().__init__()
        
        # Holiday definitions...
```

If necessary, you can define the default language that should be used, if it is not specified on the command line.

### Step 2: Define Multi-Language Holiday Names

If not done, replace function `with_name()` by `with_names()` which takes a dictionary of language codes and holiday names as a parameter.

```python
self.define_holiday() \
    .with_names({
        "xy": "<name in xy>",
        "vv": "<name in vv>",
    }) \
    ...
```

Add the translation to all defined holidays in the country (and its regions, if defined).
Run the test suite to create the snapshots for the new locale in the end.
