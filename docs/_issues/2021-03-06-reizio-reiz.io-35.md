---
title: "reizql: META(filename=...) matcher"
html_url: "https://github.com/reizio/reiz.io/issues/35"
user: isidentical
repo: reizio/reiz.io
---

Currently, there is no way to search in a specific project while using Reiz. Considering the intended dataset size (thousands of packages) it might be a cool idea to somehow add `META()` matcher for searching custom filenames. Here is an example;

```py
Call(
    Name('something'),
    __metadata__ = META(
        filename=f'requests/%'
    )
)
```

this would match files only under `requests/` prefix, which internally means only the `requests/` repo.