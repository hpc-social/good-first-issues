---
tags: ,Hacktoberfest,bug,difficulty-medium,help-wanted,impact-LOW,reach-LOW
title: "WikiCorpus.filter_wiki/remove_markup don't remove heading-markup"
html_url: "https://github.com/RaRe-Technologies/gensim/issues/2561"
user: 0x0badc0de
repo: RaRe-Technologies/gensim
---

<!--
**IMPORTANT**:

- Use the [Gensim mailing list](https://groups.google.com/forum/#!forum/gensim) to ask general or usage questions. Github issues are only for bug reports.
- Check [Recipes&FAQ](https://github.com/RaRe-Technologies/gensim/wiki/Recipes-&-FAQ) first for common answers.

Github bug reports that do not include relevant information and context will be closed without an answer. Thanks!
-->

#### Problem description

I am trying to get clean wiki texts. But still getting headings markup.

#### Steps/code/corpus to reproduce

Just create WikiCorpus and call `get_texts`. Some texts will contain `==headings==` (different number of `=` and different headings, of course).
Simple test-case:
```
>>> import gensim.corpora.wikicorpus
>>> print(gensim.corpora.wikicorpus.filter_wiki('===heading==='))
===heading===
```

#### Versions

```Linux-4.9.125-linuxkit-x86_64-with-debian-10.0
Python 3.7.4 (default, Jul 13 2019, 14:04:11) 
[GCC 8.3.0]
NumPy 1.16.4
SciPy 1.3.0
gensim 3.8.0
FAST_VERSION 1
```
