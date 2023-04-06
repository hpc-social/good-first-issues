---
tags: ,chore,docs
title: "Update `test` dependency from `nteract-scrapbook` to `scrapbook`"
html_url: "https://github.com/scikit-hep/pyhf/issues/1725"
user: matthewfeickert
repo: scikit-hep/pyhf
---

### Summary

Running the notebook tests generates the warning

```pytb
warnings.warn("'nteract-scrapbook' package has been renamed to `scrapbook`. No new releases are going out for this old package name.", FutureWarning)
```

as [`nteract-scrapbook`](https://pypi.org/project/nteract-scrapbook/) is now [`scrapbook`](https://pypi.org/project/scrapbook/). All that needs to be done is to change the name used in `steup.py` for the `test` extra:

https://github.com/scikit-hep/pyhf/blob/29bc6daed55b40711fabd9b22d3e76f9ee15657d/setup.py#L42

### Additional Information

_No response_

### Code of Conduct

- [X] I agree to follow the Code of Conduct