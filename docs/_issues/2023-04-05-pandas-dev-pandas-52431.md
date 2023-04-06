---
tags: ,Docs,Frequency
title: "DOC: Fix docs for various offset constructors"
html_url: "https://github.com/pandas-dev/pandas/issues/52431"
user: Dr-Irv
repo: pandas-dev/pandas
---

### Pandas version checks

- [X] I have checked that the issue still exists on the latest versions of the docs on `main` [here](https://pandas.pydata.org/docs/dev/)


### Location of the documentation

Multiple places (list is just a sample):

- https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.html   missing `normalize parameter
- https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.html   missing `offset` parameter
- https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearEnd.html   missing all parameters



### Documentation problem

They are all missing a definition of the constructor, e.g., `WeekOfMonth(n=..., normalize=..., week=..., weekday=...)` should be at the top for the `WeekOfMonth` followed by a description of the parameters.




### Suggested fix for documentation

All of these should be checked to see if all the parameters are listed correctly.  The way they are defined means that positional arguments will work, but maybe we don't want to support that.  (If that's the case, that's a separate issue)

The constructors should appear at the top with their arguments, like is done for other classes.
