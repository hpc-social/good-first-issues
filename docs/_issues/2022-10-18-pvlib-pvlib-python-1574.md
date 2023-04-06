---
tags: ,documentation,help-wanted
title: "\"default None\" in docstring parameter descriptions considered harmful"
html_url: "https://github.com/pvlib/pvlib-python/issues/1574"
user: kandersolar
repo: pvlib/pvlib-python
---

A common python idiom for situations where a function's parameter can be left unspecified is to set its default value to `None`.  In this usage `None` is understood not as a valid value for that parameter but rather as an indication to the function's body that it should treat the parameter as having taken no value.  We could have chosen any python value for this task; we use `None` because it is convenient and idiomatic.  One can view this pattern as a workaround to python's requirement that all parameters be specified either explicitly by the caller or implicitly by its default value.  Take Javascript as a point of comparison, where unspecified parameters are automatically set to `undefined` without the function signature having to specify that default value.

As such, I don't think there is a good reason to say `default None` in docstring parameter descriptions in these situations; `None` is more of an implementation detail than a meaningful default value that the reader would be interested in.  For example, consider `get_total_irradiance`'s `airmass` parameter:
https://github.com/pvlib/pvlib-python/blob/bdbaf4c238ce2b373d04af48193b14659662cef1/pvlib/irradiance.py#L344

Yes it's true that this parameter's default value is `None`, but I don't think that information is useful to the reader.  Either `airmass` is required and they need to pass a `numeric`, or it isn't required and they don't need to touch that parameter.  There is no situation where the user needs to say `airmass=None` in their own code.  I think it would be better to use this style:

```
     airmass : numeric, optional
```
The useful information is still there, but without the distraction of `None`.  It also renders fine in sphinx docs.

`default None` is fairly widespread in pvlib: `$ git grep -n -i -F "default None" | wc -l` returns 81.  I propose we not use `default None` in docstrings in the future (except of course in the rare case when `None` is a legitimate value) and eventually edit existing docstrings to say `optional` instead.

P.S. for anyone who doesn't get the title of this issue: https://en.wikipedia.org/wiki/Considered_harmful