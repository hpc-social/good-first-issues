---
tags: ,Hacktoberfest,difficulty-medium,feature,wishlist
title: "potential Doc2Vec feature: reverse inference, to synthesize doc/summary words"
html_url: "https://github.com/RaRe-Technologies/gensim/issues/2459"
user: gojomo
repo: RaRe-Technologies/gensim
---

Motivated by the SO question: https://stackoverflow.com/questions/55768598/interpret-the-doc2vec-vectors-clusters-representation/55779049#55779049

`Doc2Vec` could plausibly have a function that's reverse-inference: take a doc-vector, return a (ranked) list of words most-predicted by that input vector. It'd work highly analogously to `Word2Vec.predict_output_word()`. Such a list of words *might* be useful as a sort-of summary or label for a doc-vector.