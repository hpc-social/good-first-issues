---
tags: ,Hacktoberfest,bug,difficulty-easy,impact-MEDIUM,reach-LOW
title: "WordEmbeddingsKeyedVectors.add() doesn't clear `vectors_norm`, causing `IndexError` on later `most_similar()`"
html_url: "https://github.com/RaRe-Technologies/gensim/issues/2532"
user: gojomo
repo: RaRe-Technologies/gensim
---

As reported in a StackOverflow question/answer: https://stackoverflow.com/a/56641265/130288

An adapted version of the asker's minimal test case (which could become a unit test):

~~~Python
import numpy as np
from gensim.models.keyedvectors import WordEmbeddingsKeyedVectors

kv = WordEmbeddingsKeyedVectors(vector_size=3)
kv.add(entities=['a', 'b'],
       weights=[np.random.rand(3), np.random.rand(3)])
kv.most_similar('a')  # works

kv.add(entities=['c'], weights=[np.random.rand(3)])
kv.most_similar('c')  # fails with `IndexError`
~~~

Clearing the `vectors_norm` property (with either `del` or assignment-to-`None`) should be sufficient to trigger re-calculation upon the next `most_similar()`. 