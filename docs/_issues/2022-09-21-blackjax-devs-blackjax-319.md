---
tags: ,documentation,help-wanted
title: "Add \"How to distribute gradient computation?\" document"
html_url: "https://github.com/blackjax-devs/blackjax/issues/319"
user: rlouf
repo: blackjax-devs/blackjax
---

The basic idea is to use JAX's interface to dispatch the gradient function. My intuition is that replacing `logprob` with the following `logprob_pmap` may work. Details need to be ironed but something along this way will probably work:

```python
import jax

pmap_logprob_and_grad= jax.pmap(jax.grad(logprob_and_grad))

@jax.custom_jvp
def logprob_pmap(x):
    return jax.lax.psum(jax.pmap(logprob))

@logprob_fn.defjvp
def logprob_pmap_jvp(primals, tangents):
    x, = primals
    x_dot, = tangents
    val, grad = pmap_logprob_and_grad(x)
    return jax.lax.psum(val), jax.lax.psum(grad) * x_dot
```