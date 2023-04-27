---
tags: help-wanted
title: "Model calculation is not able to read features from stdin"
html_url: "https://github.com/catboost/catboost/issues/200"
user: vpd
repo: catboost/catboost
---

There is currently a disappointing exception when trying to read features from stdin:
`(TCatboostException) catboost/libs/data/load_data.cpp:181: pool file is not found -`

Streaming calculation is quite a valuable feature when running a calculation on a large stream of data generated on fly because otherwise there is an inevitable cost of disk i/o operations and process start/termination.

