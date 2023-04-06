---
tags: ,enhancement
title: "Moving from autograd to jax"
html_url: "https://github.com/mirapy-org/mirapy/issues/35"
user: ericmjl
repo: mirapy-org/mirapy
---

The next generation autograd is now called `jax`, and is built by the same guys who built autograd + more, with a somewhat nicer API. One other attractive feature is the ability to JIT compile functions to CPU, GPU and TPU!

As such, I'd like to propose switching over from autograd to jax in `requirements.txt`. Naturally, this is just a suggestion; I simply thought I'd check out the repo having seen @mattjj star it.

cc: @mattjj, @dougalm