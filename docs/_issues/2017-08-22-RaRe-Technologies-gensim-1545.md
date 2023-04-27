---
tags: Hacktoberfest,difficulty-medium,feature,performance
title: "Improving computational time in LDASeqModel"
html_url: "https://github.com/RaRe-Technologies/gensim/issues/1545"
user: Diego999
repo: RaRe-Technologies/gensim
---

Hi,

I was training a LDASeqModel on ~40k documents through 20 years (20 time slices in my case) and after 2 days of computation, still didn't finish.

I realized that only LDAModel is used in this class. Shouldn't be better to use LDAMulticore since it can also handle the case of single core ?

Thanks