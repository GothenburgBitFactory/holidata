# holidata

`holidata` is a utility for algorithmically producing holiday data.
Its purpose is mainly for [holidata.net](https://holidata.net).

Holiday data can be produced for a given year in a supported locale and output format.

## Usage

Call `holidata` providing the necessary data, e.g.
```
$ holidata --year=2020 --locale=de-DE
```
Call `holidata` with the ` --usage` or `--help` option to get usage info or help respectively.
 
## Data

For each holiday the following data is provided:
* `locale` - language and country the holiday is defined for
* `region` - region code of the given subdivision the holiday is defined for
* `date` - actual date the holiday takes place
* `description` - name of the holiday in the given language
* `type` - holiday type flags
* `notes` - additional information

## Locales

Holidata provides holiday data in different locales, i.e. for a given country and a in given language.
See [holidata.net](https://holidata.net/locales/) for a complete overview of the currently provided locales.

If you think a locale is missing, [open a feature request on github](https://github.com/GothenburgBitFactory/holidata/issues).

## Output Formats

Holidata supports different output formats, currently `csv`, `json`, `yaml`, and `xml`.

If you think an output format is missing, [open a feature request on github](https://github.com/GothenburgBitFactory/holidata/issues).

## Limitations

Holidata focuses on holidays which are _defined by law on which business or work are suspended or reduced_ (there may be some exceptions to that rule).

Holidata only provides data for countries and their principal subdivisions (both as they are defined in ISO 3166).
Holidays for other subdivisions are either merged or ignored.
There is also no explicit representation of partial holidays.

## License

`holidata` is released under the MIT license. For details check the [LICENSE](LICENSE) file.
