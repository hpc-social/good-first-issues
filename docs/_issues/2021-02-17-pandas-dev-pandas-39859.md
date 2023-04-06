---
tags: ,Docs,Needs-Discussion
title: "DOC: add button to edit on GitHub"
html_url: "https://github.com/pandas-dev/pandas/issues/39859"
user: afeld
repo: pandas-dev/pandas
---

#### Location of the documentation

https://pandas.pydata.org/docs/

#### Documentation problem

I'll write it as a user story:

_As a pandas user, when I come across a small problem with the documentation (like a typo), I want to be able to suggest a fix with minimal friction._

Currently, contributors need to search the repository to find the corresponding source file.

#### Suggested fix for documentation

Having an "Edit this page on GitHub" button would help people contribute to documentation quickly. A couple of resources explaining how to do this with Sphinx:

- https://mg.pov.lt/blog/sphinx-edit-on-github.html
- https://gist.github.com/mgedmin/6052926

Could limit to non-API pages to keep things simple. Possible it makes more sense to do this in [the theme](https://github.com/pydata/pydata-sphinx-theme).