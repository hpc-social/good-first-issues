---
tags: documentation,easy,help-wanted,testing
title: "Add examples to docstrings"
html_url: "https://github.com/pvlib/pvlib-python/issues/62"
user: bmu
repo: pvlib/pvlib-python
---

We should decide whether we want to add examples to the docstrings of the functions or not.
While (I think) examples are not included in every pandas object, they are in numpy. [numpydoc](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt#docstring-standard) has an _optional_ section for examples.

I would like to include examples and also I would like to use doctests.
For the moment we have some examples, but some doctests fail 
(see output of `nosetests -v -w pvlib --with-coverage --cover-package=pvlib --with-doctest`).
I once had a discussion with pandas developers (see pydata/pandas#3439) and they didn't see their examples as tests. 
However for pvlib, `doctest` may have an additional benefit for testing purposes and also it tests if our documentation is up to date with the state of the objects we document. 
