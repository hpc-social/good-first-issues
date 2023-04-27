---
tags: tests
title: "Add coverage to pdf.Model.expected_auxdata and pdf.Model.mainlogpdf"
html_url: "https://github.com/scikit-hep/pyhf/issues/603"
user: matthewfeickert
repo: scikit-hep/pyhf
---

# Description

In PR #596 the `codecov/patch` test failed as the relative coverage was below the total project coverage. This was confusing, as none of the code was new and just some lines were getting switched out. However, as ["relative" coverage in Codecov](https://docs.codecov.io/docs/codecov-delta#section-relative) is defined as

> Coverage concerning only lines adjusted in the commit diff (aka the diff coverage)
>
> Read as "The lines I changed in this commit are 72% covered."

then this means that if the lines that were changed in the commit were not **already** covered by a test then they will be counted against the PR's relative coverage.

The [lines in question for causing the relative coverage to fail](https://codecov.io/gh/diana-hep/pyhf/commit/33282e1dd5b260088fc8f9b12ee6da8dadf87682) were

https://github.com/diana-hep/pyhf/blob/33282e1dd5b260088fc8f9b12ee6da8dadf87682/src/pyhf/pdf.py#L569-L570

and 

https://github.com/diana-hep/pyhf/blob/33282e1dd5b260088fc8f9b12ee6da8dadf87682/src/pyhf/pdf.py#L592-L593

If one runs

```
git grep "expected_auxdata" tests/
git grep "mainlogpdf" tests/
```
no tests are found that contain them. I think this was the cause of the failing tests, and can be fixed if tests are added for these methods.