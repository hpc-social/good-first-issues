---
tags: ,help-wanted,tests
title: "Ensure doctests are not providing sole coverage for any code"
html_url: "https://github.com/scikit-hep/pyhf/issues/1653"
user: matthewfeickert
repo: scikit-hep/pyhf
---

### Summary

PR #1467 showed that the doctests are currently providing coverage to some areas of the codebase that the tests themselves never reach (e.g., when moving the doctests to their own report, the coverage from running the tests dipped)

[![coverage](https://user-images.githubusercontent.com/5142394/137968026-eca337b9-79ff-4a8d-9ffc-1d99ef57d004.png)](https://codecov.io/gh/scikit-hep/pyhf/pull/1467?src=pr&el=continue&utm_medium=referral&utm_source=github&utm_content=comment&utm_campaign=pr+comments&utm_term=scikit-hep)

This isn't really good and the only thing that the doctests should be providing is testing of the docstring examples. We should add coverage of the codebase that is now provided by the doctests into the main tests.


### Additional Information

_No response_

### Code of Conduct

- [X] I agree to follow the Code of Conduct