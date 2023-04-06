---
tags: ,hacktoberfest,help-wanted
title: "Improve code coverage"
html_url: "https://github.com/ropensci/jstor/issues/71"
user: tklebel
repo: ropensci/jstor
---

Test coverage is good (91% atm), but it could be better. 

A good place to start would be to implement a proper test for the print-method of `jst_define_import`. I have drafted a test (the last one in https://github.com/ropensci/jstor/blob/master/tests/testthat/test-import-spec.R, which is currently skipped), but it depends on the console width and is thus not working. A good version of the test would also check that the colors set with the `crayon` package are working.

Another option would be to work on the functions for re-importing files. This involves working with the file system (checking that files are being written or being deleted), but it should also be manageable.