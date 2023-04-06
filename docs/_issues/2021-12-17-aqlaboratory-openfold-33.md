---
tags: ,enhancement,help-wanted
title: "Low-memory attention a little slow"
html_url: "https://github.com/aqlaboratory/openfold/issues/33"
user: gahdritz
repo: aqlaboratory/openfold
---

I've implemented low-memory attention (9670958) using an algorithm from a recent preprint (https://arxiv.org/pdf/2112.05682.pdf), enhanced a little bit with the ability to add multiple biases + batch dimensions. Lacking the JAX map & scan used in the original implementation, which I've had to replace with for loops, ours is quite a bit slower (exact figures depend heavily on the choice of chunk sizes, but it seems to be in the ballpark of 2x slower than our own standard Attention implementation). It would be nice to speed it up a little.