---
tags: Hacktoberfest,bug,difficulty-easy,performance
title: "Check what's the reason to use double-precision in topic models"
html_url: "https://github.com/RaRe-Technologies/gensim/issues/1576"
user: menshikh-iv
repo: RaRe-Technologies/gensim
---

Our TMs return vectors with double-precision `float64`, it looks like very suspicious, because `float32` is enough for all. Need to check, what's a reason of this behavior and what's a concrete method.

The first step - look at [this line in the test](https://github.com/RaRe-Technologies/gensim/blob/develop/gensim/test/basetmtests.py#L51), after it - collect all TMs, that depends on this tests and check, where and why `float64` happened.

Result - detailed description (where and why), and fixing this behavior after discussion (if needed)