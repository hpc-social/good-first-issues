---
tags: Docs
title: "DOC: 10 Minutes Guide has assumed knowledge on new users"
html_url: "https://github.com/pandas-dev/pandas/issues/47282"
user: Capobiaj
repo: pandas-dev/pandas
---

### Pandas version checks

- [X] I have checked that the issue still exists on the latest versions of the docs on `main` [here](https://pandas.pydata.org/docs/dev/)


### Location of the documentation

https://pandas.pydata.org/docs/dev/user_guide/10min.html#min

### Documentation problem

The 10 minutes guide has assumed knowledge on the part of the user regarding what exactly a 'Series' or 'DataFrame' are. The linked material is too complex for a 10 minute guide designed for new users to the project. 

Being that the 10 minutes to pandas guide was designed for new users to quickly get an introduction to the project and orient themselves to learn and use the project, a brief explanation of what those two data structures are would be beneficial to new users and help them better acclimate, adjust, and understand the project and its use cases.

### Suggested fix for documentation

The 10 minute guide could benefit from a very brief (1-2 sentences) explanation of what Series and DataFrames to aid new users.

Suggested fix in the documentation is: transposing part of 'Intro to data structures' definition of Series and DataFrame onto 10min.rst.

Suggest Series definition addition to documentation: 

Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.).

Suggested DataFrame definition addition to documentation:

DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. Like Series, DataFrame accepts many different kinds of input such as: Dicts of 1D ndarrays lists, dicts or series, along with 2-D numpy.ndarray, Structured or record ndarray, and another DataFrame.

