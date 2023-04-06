---
tags: ,Enhancement,Package-novice,table,unified-io
title: "Reading and writing Excel spreadsheets in the unified table interface"
html_url: "https://github.com/astropy/astropy/issues/3744"
user: hamogu
repo: astropy/astropy
---

tl;dr: look at #8381 and add support for the `pandas.read_excel` function and tests.

The use of spreadsheet programs is not uncommon in astronomy. We, as a programming community sometimes tend to think of spreadsheet programs as an inferior way to view and manipulate data, but in fact `astropy.table.Table` by now (or after open PRs are merged) supports many features that are either directly borrowed from spreadsheet editors or at least can be found in spreadsheet editors as well: Output values can be formatted for displaying in a particular way, columns can be hidden from display, columns can have a certain data dtype (e.g. a time in mixin columns), columns can be calculated automatically based on values from other columns...

Given how many people use spreadsheets and how often I get xlsx files from collaborartors by email it does not seem unreasonable to provide an xlsx reader and writer for the astropy unified table reader and writer interface like so `tab = astropy.table.Table.read('mysheet.xlsx')`

Note that #1562 modified the csv reader so that `io.ascii` can read cvs files written by Microsoft Excel and similar spreadsheet programs, but more could be done if we could read those files directly. In particular, dates and times (difficult when exporting to a csv first) and the column formatting could be preserved (bonus points for hidden colums).

Obviously, reading and writing a spreadsheet as a table requires some assumptions which need to be documented, e.g. column headers are in the first row, units (if any) are in the second row, the formatting of numbers is the same for all numbers in a column, the data is read from the active sheet if no sheet name is given, etc. and will never be feature complete (e.g. xlsx files can contain plots and graphics).
Yet, many tables conform to "reasonable" formatting.

Using openpyxl (https://openpyxl.readthedocs.org/en/latest/) as a dependency, this should not be too hard to implement for a set of basic features.

In my opinion, this has a low priority.
