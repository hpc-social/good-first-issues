---
tags: ,Docs,MultiIndex
title: "DOC: MultiIndex methods not grouped together"
html_url: "https://github.com/pandas-dev/pandas/issues/50496"
user: mcp292
repo: pandas-dev/pandas
---

### Pandas version checks

- [X] I have checked that the issue still exists on the latest versions of the docs on `main` [here](https://pandas.pydata.org/docs/dev/)


### Location of the documentation

https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.html#pandas.MultiIndex

### Documentation problem

Full list of `MultiIndex` methods not provided in docs and separated in the hamburger menu:

![2022-12-29_1540](https://user-images.githubusercontent.com/49123398/210018351-29e4f7e5-fa48-4c36-ab72-5fe9f7e1279d.png)

![2022-12-29_1550](https://user-images.githubusercontent.com/49123398/210018481-09b2219b-bd91-4c65-826d-20cc7eedb441.png)

### Suggested fix for documentation

These should be grouped together and documented in the [MultiIndex doc page](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.html#pandas.MultiIndex), with the goal of making the page self-contained.

In documenting this issue I came across the [MultiIndex API Reference](https://pandas.pydata.org/docs/dev/reference/indexing.html#multiindex). I've been using pandas for almost 2 years and this is the first time I'm finding this useful page.

Based on my experience, I would also recommend linking to the API Reference from within doc pages, the way the User Guide is often referred to therein:

![2022-12-29_1557](https://user-images.githubusercontent.com/49123398/210018955-35cc7640-c819-4a50-ac66-da9be7b652d4.png)
