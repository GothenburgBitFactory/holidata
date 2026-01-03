# How to Define Holidays in Holidata

> Before defining holidays in Holidata, ensure you have set up your development environment following these [initial setup](getting-started.md) steps.

This document explains how to define holidays for your country or region in the holidata library.

## Overview

Holidays are defined in the `__init__` method of your [country](add-country.md) or [region](add-regions.md) class using a fluent API.
Each holiday definition follows this basic pattern:

```python
self.define_holiday() \
    .with_name("<name>") \
    .on(<date_function>) \
    .with_flags("<flags>")
```

## Holiday name

Holidays are identified by their name in each locale.
Holidays with the same name defined in different regions are grouped together in the final output.

The `with_name` function used here is a shortcut for countries with only a single locale.
See [this guide](add-locales.md) on how to add more languages.

## Date Functions

The _date function_ is used to define the date on which a holiday takes place.

Holidays either take place on a _fixed date_ or a _variable date_.
The Holidata library provides a set of _date functions_ to handle the different cases.

### Fixed Dates

The `date` function can be used for holidays taking place on a fixed date (_n-th day of a month_), e.g.:

```python
date(month=1, day=1)    # January 1st
date(month=12, day=25)  # December 25th
```

### Weekday Occurrences

For holidays which take place on a certain weekday of a month, there are the functions `first`, `second`, `third`, `fourth`, and `last` to handle those cases, e.g.:
```python
# n-th occurrence of a weekday in a month
first("monday").of("may")
second("tuesday").of("june")
third("wednesday").of("july")
fourth("thursday").of("august")

last("friday").of("september")
```

### Easter-Based Dates

The Easter date is a special variable holiday, but luckily there is an algorithm for it.
The `Country` class provides the function `easter()` to be used here.
Note that you have to set the field `easter_type` of the respective country class for this.

```python
# Easter Sunday (uses the easter_type defined in your country class)
self.easter()
```

### Dates Based on Other Calendars or Authorities

For holidays based on other calendars (Hindu/Chinese lunisolar, Islamic lunar,...) currently a list of hard-coded reference dates in the respective country is used.

Examples for this can be found e.g. in the implementation of Turkey (`TR`) or Singapore (`SG`).
Help on extending the Holiday API for this is highly appreciated!

### Relative Dates

For holidays which take place relative to a _reference date_ (e.g. Easter) there are `before` and `after` methods available for this.
Use the `day` function to define a fixed distance, or use the weekday occurrence functions from above to shift to a specific weekday, e.g.:

```python
# Days before/after a date
day(2).before(<date_function>)  # 2 days before 
day(1).after(<date_function>)   # 1 day after 

# Weekday before/after a date
first("monday").before(<date_function>)
second("tuesday").after(<date_function>)
```

Those calls can be nested. An example for this would be the German holiday _Buß- und Bettag_ which takes place on the 11th day before the first Advent Sunday, which is the fourth sunday before Christmas:

```python
day(11).before(fourth("sunday").before(date(month=12, day=25)))
```

### Custom Date Functions

If none of the provided date functions fits your need, you can define a custom date function in your country or region class with the following signature:

```python
def custom_date_function(year: int) -> Union[SmartDayArrow, None]:
    pass
```

If the function returns `None` the holiday will be ignored.

> Custom date functions should be seen as a last resort and avoided as much as possible.
> We are working hard to make the Holidata API accommodate for all cases.
> If such a function is absolutely necessary, consider a pull request for the Holidata API.

## Holiday Flags

Flags indicate the type of holiday:

- `N`: National holiday
- `R`: Religious holiday
- `F`: Fixed date
- `V`: Variable date

Common combinations:
- `NF`: National fixed holiday
- `NRV`: National religious variable holiday
- `NV`: National variable holiday
- `NRF`: National religious fixed holiday

## Holiday Lifecycle

Holidays can be established and be abandoned, some holidays can also be subject to special announcements.

To model the holiday 'lifecycle' Holidata provides the functions `since`, `until`, and `in_years`.

### Since a Specific Year

The `since` function can be used to define the year since when (included) the holiday is in place, e.g.:

```python
self.define_holiday() \
    .with_name("<name>") \
    .on(<date_function>) \
    .with_flags("<flags>") \
    .since(2020)
```
Holidata wants to deliver holiday data from 2011 on, so `since` is optional for holidays established before this year.

### Until a Specific Year

The `until` function can be used to the define the year until when (included) the holiday is in place, e.g.:

```python
self.define_holiday() \
    .with_name("<name>") \
    .on(<date_function>) \
    .with_flags("<flags>") \
    .until(2030)
```

### Specific Years Only

If the same holiday is subject to announcements in different years, one can use the `in_years` function, e.g.:

```python
self.define_holiday() \
    .with_name("<name>") \
    .on(<date_function>) \
    .with_flags("<flags>") \
    .in_years([2020, 2024, 2028])
```

## Adding Notes

Optionally, additional information can be added to holidays, e.g.:

```python
self.define_holiday() \
    .with_name("<name>") \
    .on(<date_function>) \
    .with_flags("<flags>") \
    .annotated_with("Lorem ipsum, dolor sit amet!")
```

## Next Steps

After defining your holidays, you will have to [update snapshots of the test suite](getting-started.md#update-snapshot-files) to ensure consistency of the data.
