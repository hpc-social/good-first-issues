---
tags: ,Difficulty-Easy,Good-first-issue,New-feature
title: "[ENH]: Add setter/getter methods for all keyword parameters to Figure.__init__"
html_url: "https://github.com/matplotlib/matplotlib/issues/24617"
user: tacaswell
repo: matplotlib/matplotlib
---

### Problem

At least 2 of the arguments passed to `Figure.__init__` do not have matching `get_{kwarg}`/`set_{kwarg}` methods on `Figure` which makes using `fig.set(...)` inconsistent with what can be done via `Figure(...)`.

xref #21549 which was motivated by this and includes an implementation of the solution (along with some additional refactoring).

### Proposed solution

See #21549 for a majority of the implementation.  cherry-picking commits from that branch and dropping the layout management refactoring is a very good start.

 - use alias mechanism for `size_inches` -> `figsize`
 - add `get/set_subplotparams`
 - use alias mechanism from `layout` -> `layout_engine`
 - tests!
 - whats new entry


Labeling this as good first issue because it is limited scope and easy because there is an existing implementation.  There will be a discussion of API consistency so I think familiarity with Matplotlib's explicit API would be very helpful.