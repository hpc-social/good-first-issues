---
tags: comp-stats,type-enh
title: "ENH: weightstats CompareMeans add from_data and summary methods"
html_url: "https://github.com/statsmodels/statsmodels/issues/2569"
user: josef-pkt
repo: statsmodels/statsmodels
---

see http://stackoverflow.com/questions/31768464/confidence-interval-for-t-test-difference-between-means-in-python

to make the interface more convenient in weightstats CompareMeans, we could add `from_data` and `summary` methods.

summary could print a summary table (1 row) similar to `LikelihoodResults.t_test` and `Contrast`

Note: weightstats CompareMeans was written before Contrast results gained the summary and other enhancements, and we never checked for adding similar improvements.
