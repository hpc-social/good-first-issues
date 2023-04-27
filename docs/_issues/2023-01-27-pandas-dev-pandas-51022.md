---
tags: Bug,Error-Reporting,Indexing
title: "BUG: Series.take needs to validate axis"
html_url: "https://github.com/pandas-dev/pandas/issues/51022"
user: jbrockmendel
repo: pandas-dev/pandas
---

```python
pd.Series([1, 2, 3]).take([1], axis="foo")
```

Nonsense "axis" fails to raise, should raise ValueError.
