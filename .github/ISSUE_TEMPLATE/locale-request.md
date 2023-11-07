---
name: Locale request
about: Request a new locale
title: 'Add locale for LANG-COUNTRY'
labels: 'locale'
assignees: ''

---

**Basic information**
* What is the language code according to [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)?
* What is the country code according to [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)?

(please replace `LANG` and `COUNTRY` in the issue title accordingly)

* Provide a list of all holidays, i.e. days "which are defined by law on which business or work are suspended or reduced"
* Are holidays moved to a different date, e.g. if they fall on a saturday/sunday/...? If yes, which holidays and what is the algorithm?
* Are holidays observed on a different date (is there a substitute holiday), e.g. if they fall on a saturday/sunday/...? If yes, which holidays and what is the algorithm?
* If possible, provide the legal sources which define the holidays.

**For each holiday**
* What is the official name?
* Is it a regional or nation-wide holiday?
* If regional, what are the regions the holiday is observed in? (Note: currently only regions defined in ISO_3166-2 are supported)
* Is it a fixed or variable date?
* If fixed, provide the date in format `MM-DD`
* If a holiday has a variable date: What is the algorithm to calculate it (e.g. `nth <weekday>/<day> in <month>`,...)? If it depends on the easter date: Is it the western or orthodox easter date?
* If the holiday is proclaimed by the government: Can you provide the source?
