---
tags: help-wanted,internal
title: "Implement DESeq2 like normalization"
html_url: "https://github.com/miRTop/mirtop/issues/22"
user: lpantano
repo: miRTop/mirtop
---

Add the code that from a count matrix, can get the size factor to normalize the data. 

So, input would be: count data and output: normalized count data. 

In R the code is like this:

```
loggeomeans <- rowMeans(log(counts))
sf <- apply(counts, 2, function(cnts) {
      exp(median((log(cnts) - loggeomeans)[is.finite(loggeomeans) & cnts > 0]))
    })
sf <- sf/exp(mean(log(sf)))
t(t(counts)/sf)
```

This code can be inside `libs/math.py`