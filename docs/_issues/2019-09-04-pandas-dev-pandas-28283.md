---
tags: Bug,metadata
title: "Various methods don't call call __finalize__"
html_url: "https://github.com/pandas-dev/pandas/issues/28283"
user: TomAugspurger
repo: pandas-dev/pandas
---

Improve coverage of `NDFrame.__finalize__`

Pandas uses `NDFrame.__finalize__` to propagate metadata from one NDFrame to
another. This ensures that things like `self.attrs` and `self.flags` are not
lost. In general we would like that any operation that accepts one or more
NDFrames and returns an NDFrame should propagate metadata by calling
`__finalize__`.

The test file at
https://github.com/pandas-dev/pandas/blob/master/pandas/tests/generic/test_finalize.py
attempts to be an exhaustive suite of tests for all these cases. However there
are many tests currently xfailing, and there are likely many APIs not covered.

This is a meta-issue to improve the use of `__finalize__`. Here's a hopefully
accurate list of methods that don't currently call finalize.

Some general comments around finalize

1. We don't have a good sense for what should happen to `attrs` when there are
   multiple NDFrames involved with differing attrs (e.g. in concat). The safest
   approach is to probably drop the attrs when they don't match, but this will
   need some thought.
2. We need to be mindful of performance. `__finalize__` can be somewhat expensive
   so we'd like to call it exactly once per *user-facing* method. This can be tricky
   for things like `DataFrame.apply` which is sometimes used internally. We may need
   to refactor some methods to have a user-facing `DataFrame.apply` that calls an internal
   `DataFrame._apply`. The internal method would *not* call `__finalize__`, just the
   user-facing `DataFrame.apply` would.

If you're interested in working on this please post a comment indicating which method
you're working on. Un-xfail the test, then update the method to pass the test. Some of these
will be much more difficult to work on than others (e.g. groupby is going to be difficult). If you're
unsure whether a particular method is likely to be difficult, ask first.

- [x] `DataFrame.__getitem__` with a scalar
- [ ] `DataFrame.eval` with `engine="numexpr"`
- [x] `DataFrame.duplicated`
- [x] `DataFrame.add`, `mul`, etc. (at least for most things; some work to do on conflicts / overlapping attrs in binops)
- [ ] `DataFrame.combine`, `DataFrame.combine_first`
- [x] `DataFrame.update`
- [x] `DataFrame.pivot`, `pivot_table`
- [x] `DataFrame.stack`
- [x] `DataFrame.unstack`
- [x] `DataFrame.explode` https://github.com/pandas-dev/pandas/pull/46629
- [x] `DataFrame.melt` https://github.com/pandas-dev/pandas/pull/46648
- [x] `DataFrame.diff`
- [x] `DataFrame.applymap`
- [x] `DataFrame.append`
- [ ] `DataFrame.merge`
- [x] `DataFrame.cov`
- [ ] `DataFrame.corrwith`
- [x] `DataFrame.count`
- [x] `DataFrame.nunique`
- [x] `DataFrame.idxmax`, `idxmin`
- [x] `DataFrame.mode`
- [x] `DataFrame.quantile` (scalar and list of quantiles)
- [x] `DataFrame.isin`
- [x] `DataFrame.pop`
- [x] `DataFrame.squeeze`
- [x] `Series.abs`
- [x] `DataFrame.get`
- [x] `DataFrame.round`
- [x] `DataFrame.convert_dtypes`
- [x] `DataFrame.pct_change`
- [x] `DataFrame.transform`
- [x] `DataFrame.apply`
- [ ] `DataFrame.any`, `sum`, `std`, `mean`, etdc.
- [x] `Series.str.` operations returning a Series / DataFrame
- [x] `Series.dt.` operations returning a Series / DataFrame
- [x] `Series.cat.` operations returning a Series / DataFrame
- [x] All groupby operations (at least some work)
- [x] `.iloc` / `.loc` https://github.com/pandas-dev/pandas/pull/46101
