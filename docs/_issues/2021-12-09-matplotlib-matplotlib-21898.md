---
tags: ,Difficulty-Medium,Good-first-issue,New-feature,topic-ticks-axis-labels
title: "Reprs on formatters and locaters"
html_url: "https://github.com/matplotlib/matplotlib/issues/21898"
user: story645
repo: matplotlib/matplotlib
---

As discussed in #21874, there aren't reprs on the locators and formatters. Reprs of the form where eval(repr) = call, something like 
```python
eval('AutoDateLocator(maxticks=8)') = AutoDateLocator(maxticks)
```
would mean reprs could be used in the documentation examples, which would help keep the labels in sync. This is useful for the new example #21874 & 
* https://matplotlib.org/devdocs/gallery/ticks/tick-formatters.html
* https://matplotlib.org/devdocs/gallery/ticks/tick-locators.html
and possibly reproducibility

I think it's a good first issue 'cause it's fairly standalone and rote if you know classes, only potential difficulty might be in storing the original args:

> 
> When I try `AutoDateLocator.__repr__ = lambda self: f'AutodateLocator(maxticks={self.maxticks})'` then `repr(AutoDateLocator(maxticks=8))` returns `'AutodateLocator(maxticks={0: 8, 1: 8, 3: 8, 4: 8, 5: 8, 6: 8, 7: 8})'`, i.e. the class variable `maxticks`. I don't know how to get the value passed in during the function call. But even if this is possible, I find defining all the `repr` rather verbose and a bit hacky as compared to a simple `eval`.
> 
> _Originally posted by @StefRe in https://github.com/matplotlib/matplotlib/issues/21874#issuecomment-988143221_