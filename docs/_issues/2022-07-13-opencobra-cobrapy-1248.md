---
tags: ,enhancement,help-wanted
title: "inconsistency in FBA flavour invocations"
html_url: "https://github.com/opencobra/cobrapy/issues/1248"
user: lptolik
repo: opencobra/cobrapy
---

### Checklist

<!-- Please make sure you check all these items before submitting your feature request. -->

- [ x] There are [no similar issues or pull requests](https://github.com/opencobra/cobrapy/issues) for this yet.

### Is your feature related to a problem? Please describe it.
There are three flavours of FBA in cobra: FBA, pFBA, and geometric FBA. The plain FBA (model.optimise) has the argument ` raise_error` to specify whether you want an exception to be raised.  Neither pFBA nor geometric FBA has this argument.  I think it would be nice if the invocation of all flavours of FBA would be consistent.

## Describe the solution you would like.
Within all three functions pattern

```
m.slim_optimize(error_value=None)
solution = get_solution(m, reactions=reactions)
```
is used, but only in the plain FBA (model.optimise) `raise_error` is propagated into `get_solution`.

