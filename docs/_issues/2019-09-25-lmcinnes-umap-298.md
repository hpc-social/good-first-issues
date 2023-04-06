---
tags: 0.4,documentation
title: "Document reproducibility guarantees"
html_url: "https://github.com/lmcinnes/umap/issues/298"
user: tomwhite
repo: lmcinnes/umap
---

Following up on the discussion [here](https://github.com/lmcinnes/umap/pull/231#issuecomment-497383435), it would be good to document how to get reproducible results with UMAP.

I think we should consider changing `random_state` in the UMAP constructor to a seed (e.g. 42, like the new `transform_seed` default) so that UMAP is reproducible by default.

We should document that users can set `random_state` to `None` to get faster results at the expense of reproducibility. In this mode there is no seed that would produce the same output due to the multithreading. (This was introduced in #294.)
