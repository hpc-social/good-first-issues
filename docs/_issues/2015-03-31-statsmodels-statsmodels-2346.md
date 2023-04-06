---
tags: ,comp-stats,prio-high,type-enh
title: "pairwise_tukeyhsd - retrieve \"reject\" values"
html_url: "https://github.com/statsmodels/statsmodels/issues/2346"
user: arnaldorusso
repo: statsmodels/statsmodels
---

I was thinking about how to get the numeric values of "reject" column.

```
In [140]: print(tukey_result.summary())
Multiple Comparison of Means - Tukey HSD,FWER=0.05
=============================================
group1 group2 meandiff  lower   upper  reject
---------------------------------------------
ger    tbw   14.1319  -3.3327 31.5966 False 
ger    tww   30.2923  11.3796  49.205  True 
tbw    tww   16.1604  -0.9708 33.2915 False 
---------------------------------------------
```
1. `tukey_result.reject` returns boolean results the same for attribute `reject2`. Where I can find the numeric float values of `p`?
2. why the simple `tukey_result.summary()` does not print the summary table?

Cheers,
Arnaldo. 
