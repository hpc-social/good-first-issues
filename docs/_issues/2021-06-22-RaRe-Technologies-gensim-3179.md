---
tags: bug,difficulty-easy,fasttext
title: "Gensim's FastText model reads in unsupported modes from Facebook's FastText"
html_url: "https://github.com/RaRe-Technologies/gensim/issues/3179"
user: mpenkov
repo: RaRe-Technologies/gensim
---

In gensim/models/fasttext.py:

```python
    model = FastText(
        vector_size=m.dim,
        vector_size=m.dim,
        window=m.ws,
        window=m.ws,
        epochs=m.epoch,
        epochs=m.epoch,
        negative=m.neg,
        negative=m.neg,
        # FIXME: these next 2 lines read in unsupported FB FT modes (loss=3 softmax or loss=4 onevsall,
        # or model=3 supervised) possibly creating inconsistent gensim model likely to fail later. Displaying
        # clear error/warning with explanatory message would be far better - even if there might be some reason
        # to continue with the load - such as providing read-only access to word-vectors trained those ways. (See:
        # https://github.com/facebookresearch/fastText/blob/2cc7f54ac034ae320a9af784b8145c50cc68965c/src/args.h#L19
        # for FB FT mode definitions.)
        hs=int(m.loss == 1),
        hs=int(m.loss == 1),
        sg=int(m.model == 2),
        sg=int(m.model == 2),
        bucket=m.bucket,
        bucket=m.bucket,
        min_count=m.min_count,
        min_count=m.min_count,
        sample=m.t,
        sample=m.t,
        min_n=m.minn,
        min_n=m.minn,
        max_n=m.maxn,
        max_n=m.maxn,
    )
```