---
tags: ,enhancement,sampler
title: "Implement multipathfinder"
html_url: "https://github.com/blackjax-devs/blackjax/issues/213"
user: junpenglao
repo: blackjax-devs/blackjax
---

After #210, it should be straightforward to add multi-pathfinder (ref: https://arxiv.org/pdf/2108.03782.pdf). The code snippet below mostly work (still need implementation of Pareto Smoothed important sampling).

```python
multi_pathfinder = jax.vmap(lambda rng_key, x: blackjax.vi.pathfinder.init(rng_key, logprob_fn, x))
n_batch = 100
rng_keys = jax.random.split(rng_key, n_batch)
xs = w0 * jnp.ones((n_batch, M))
output = multi_pathfinder(rng_keys, xs)

phis, logq = jax.vmap(
    lambda key, state: blackjax.vi.pathfinder.sample_from_state(key, state, 5_000)
    )(rng_keys, output)
logp = jax.vmap(jax.vmap(logprob_fn))(phis)

logp_tilt = logp - jnp.log(n_batch)
logq_tilt = logq - jnp.log(n_batch)
# TODO: Pareto Smoothed Importance Sampling
# psi = pr_irs(phis, logp_tilt, logq_tilt, n_samples)
```

It will be a good first issue to:
- add multi-pathfinder with some test
- add example of using multi-pathfinder (maybe some example from the paper)