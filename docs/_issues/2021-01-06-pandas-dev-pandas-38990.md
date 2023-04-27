---
tags: Docs,IO-Excel
title: "DOC: add comparison to spreadsheets"
html_url: "https://github.com/pandas-dev/pandas/issues/38990"
user: afeld
repo: pandas-dev/pandas
---

#### Location of the documentation

https://pandas.pydata.org/docs/dev/getting_started/comparison/comparison_with_spreadsheets.html

#### Documentation problem

From https://github.com/pandas-dev/pandas/pull/38554:

> I teach [a class on pandas for public policy students](https://github.com/afeld/python-public-policy/blob/master/syllabus.md#readme), and for many of them, spreadsheets are the only point of reference they have for working with tabular data.

There are [a number of unofficial resources](https://www.google.com/search?q=excel+vs+pandas), but no official, living documentation to point them to.

#### Suggested fix for documentation

The idea is to add a "Comparison to spreadsheets" page alongside [the other comparison pages](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/index.html). That new page already got merged in https://github.com/pandas-dev/pandas/pull/38554; creating this issue to keep a running checklist of the TODOs.

- [x] start with what @rotuna did in https://github.com/pandas-dev/pandas/pull/23042
- [x] link from Getting Started pages
- [ ] incorporate structure from [SAS](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sas.html)/[STATA](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_stata.html) comparison pages
   - [x] Data structures
   - [x] Data input / output
      - [x] Mention `read_excel()`
   - [x] Data operations
   - [x] String processing
   - [x] Merging
   - [ ] Missing data
   - [ ] GroupBy
   - [x] Other considerations
- [ ] standardize datasets used for examples, for greater consistency and reduced cognitive burden on the readers
   - [`tips`](https://raw.github.com/pandas-dev/pandas/master/pandas/tests/io/data/csv/tips.csv) probably works for most
- [ ] add info about charting
- [x] [add example showing round trip to/from Excel](https://github.com/pandas-dev/pandas/pull/38554#discussion_r549409566)
- [ ] [have pivot table examples match](https://github.com/pandas-dev/pandas/pull/38554#issuecomment-752767183)
- [ ] add [quick reference](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_r.html#quick-reference)