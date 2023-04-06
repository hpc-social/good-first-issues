---
tags: enhancement
title: "Restructure Unit Tests"
html_url: "https://github.com/parmoo/parmoo/issues/16"
user: thchang
repo: parmoo/parmoo
---

Unit test suite is unorganized, and many unit tests are difficult to read.

This is due to many of the unit tests being written early-on in the development cycle, before several major refactors, and having been updated to support newer interfaces with minimal effort.

Additionally, many unit tests are extremely long and combine multiple checks into a single test function.  These should be broken apart into separate tests.

Many unit test files are extremely long, and should be divided up into separate files, perhaps in subdirectories of unit test directory.