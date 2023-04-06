---
tags: ,help-wanted
title: "change to standard NLL fit objective"
html_url: "https://github.com/scikit-hep/pyhf/issues/1006"
user: lukasheinrich
repo: scikit-hep/pyhf
---

right now we use "twice_nll" as a fit objective and in the test statistic a simple diffence

`twice_nll_constrfit - twice_nll_globalfit`

but rather we should just to a NLL fit and in the test stat do

`2*(nll_constrfit - nll_globalfit)`


this will require updating some test reference numbers in the tests
