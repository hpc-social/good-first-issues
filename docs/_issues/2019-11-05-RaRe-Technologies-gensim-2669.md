---
tags: difficulty-easy,documentation
title: "word2vec doc-comment example of KeyedVectors usage broken"
html_url: "https://github.com/RaRe-Technologies/gensim/issues/2669"
user: gojomo
repo: RaRe-Technologies/gensim
---

The usage example in the word2vec.py doc-comment regarding `KeyedVectors` uses inconsistent paths and thus doesn't work. 

https://github.com/RaRe-Technologies/gensim/blob/e859c11f6f57bf3c883a718a9ab7067ac0c2d4cf/gensim/models/word2vec.py#L73

https://github.com/RaRe-Technologies/gensim/blob/e859c11f6f57bf3c883a718a9ab7067ac0c2d4cf/gensim/models/word2vec.py#L76

If vectors were saved to a tmpfile-path based on the filename `'wordvectors.kv'`, they need to loaded from that same path, not some other local-directory file named 'model.wv'.

(Also, in my opinion the use of `get_tmpfile()` adds unnecessary extra complexity to this example. People usually **don't** want their models in a "temp" directory, which some systems will occasionally delete, so the examples might as well do the simplest possible thing: store in the current working directory with simple string filenames. The example code above this is also confused, because it creates a temp-file path, but then doesn't actually use it, choosing to do the simple & right thing with a local file instead.)