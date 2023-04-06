---
tags: ,Hacktoberfest,bug,difficulty-easy,impact-LOW,reach-LOW
title: "bug in gensim.summarization.mz_entropy.mz_keywords"
html_url: "https://github.com/RaRe-Technologies/gensim/issues/2523"
user: bbaranow
repo: RaRe-Technologies/gensim
---

**Problem statement:**

It seems to be a bug if the text is too short and number of words is lower than blocksize. In my case the values were: `n_words (232.0) ` and `blocksize (1024)`.

**Log:**

```
gensim\summarization\mz_entropy.py:127: RuntimeWarning: invalid value encountered in double_scalars
  - __log_combinations(n_words, blocksize)
```

**Dirty solution:**

Override `blocksize` value from the default `1024` to something lower:

`mz_keywords(text, blocksize=128)`

