---
tags: enhancement
title: "Test coverage of special parameterizations"
html_url: "https://github.com/netsiphd/netrd/issues/202"
user: sdmccabe
repo: netsiphd/netrd
---

There are some methods that have parameterizations that have different behavior; these are not always tested explicitly in the test suites, where we tend to favor the defaults. Examples:

* Correlation matrix (regularization)
* Laplacian distances (kernel, norm, etc.)

I'm sure there are others. Ideally we would have a full account of these and make sure they are fully covered by the tests.