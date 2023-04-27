---
tags: enhancement,pkgcsvviewer
title: "Comment option for CSVTable"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/11902"
user: barronh
repo: jupyterlab/jupyterlab
---

### Problem

When opening a CSV file in CSVTable, there is no option for a "comment character." Comments are common in scientific datasets where metadata about columns are important and has no natural place in a CSV. When comments are at the beginning of a file, CSVTable creates one big line for each row.

This is related to #8876, but not identical. In #8876, the number of columns changes between rows. In this case, the number of columns might be constant but is not appropriately diagnosed from any row preceded by a comment character.

A comment character could defer "first line" assessment of the number of columns.

Below is an example dataset that would open as a single column.

```
# This file is an arbitrary dataset to illustrate the problem
# The units of value are micrograms/m**3
date,lon,lat,value
2020-01-01 00:00:00Z,-97.0,40,5.00
2020-01-01 01:00:00Z,-97.0,40,6.00
```

Ideally, the columns would be based on the first line that did not start with a `#`.

The solution to #8876 would likely address many instances here, but perhaps not all.

### Proposed Solution

I propose adding a Comment option in addition to the Delimiter option. The default could be `#` or None. If None, standard parsing would occur. When set, the CSV would be reparsed ignoring comment lines when diagnosing columns.

Comment lines should still be shown; just not be used to parse the file.

### Additional context

Many CSV parsers have this capability include pandas, which allows for a comment character.

Thanks to anyone willing to take this on!