---
tags: ,enhancement,help-wanted,important,vi
title: "Adding some basic VI approximation and fitting routine"
html_url: "https://github.com/blackjax-devs/blackjax/issues/397"
user: junpenglao
repo: blackjax-devs/blackjax
---

Copying over from https://github.com/blackjax-devs/blackjax/pull/392#discussion_r1020745315

After #392, we should add the 2 most basic VI algorithm: meanfield and full rank ADVI [1]. Below is a working example of Meanfield ADVI:

```python
import jax
import jax.numpy as jnp
from jax.scipy import stats

def gen_meanfield_logprob(params):
    mu_param, rho_param = params
    sigma_param = jax.tree_map(jnp.exp, rho_param)
    def meanfield_logprob(position):
        logq_pytree = jax.tree_map(
            stats.norm.logpdf, position, mu_param, sigma_param
            )
        logq = jax.tree_map(jnp.sum, logq_pytree)
        return jax.tree_util.tree_reduce(jnp.add, logq)
    return meanfield_logprob

# gen_meanfield_logprob(init_params)(init_position)

def meanfield_sample(
    rng_key, meanfield_param, num_samples: int
    ):
    if not isinstance(num_samples, tuple):
        num_samples = (num_samples,)
    mu_param, rho_param = meanfield_param
    sigma_param = jax.tree_map(jnp.exp, rho_param)
    mu_flatten, unravel_fn = jax.flatten_util.ravel_pytree(mu_param)
    sigma_flatten, _ = jax.flatten_util.ravel_pytree(sigma_param)
    flatten_sample = jax.random.normal(
        rng_key, num_samples + mu_flatten.shape
        ) * sigma_flatten + mu_flatten
    if len(num_samples) == 0:
        return unravel_fn(flatten_sample)
    return jax.vmap(unravel_fn)(flatten_sample)

# meanfield_sample(rng, init_params, ())

def meanfield_approximate(rng, init_params, log_prob_fn, optimizer, sample_size=5, num_steps=200):
    def meanfield_approximate_step(
        state, rng_key_sample
        ):
        params, opt_state = state
        def kl_fn(params):
            sample = meanfield_sample(rng_key_sample, params, sample_size)
            logq = gen_meanfield_logprob(params)(sample)
            logp = log_prob_fn(sample)
            return (logq - logp).mean()
        # compute KL divergence
        elbo, grad = jax.value_and_grad(kl_fn)(params)
        updates, opt_state = optimizer.update(grad, opt_state, params)
        params = jax.tree_map(
            lambda p, u: p + u, params, updates
            )
        return (params, opt_state), elbo
    
    def run_optimization(init_params):
        opt_state = optimizer.init(init_params)
        state = (init_params, opt_state)
        rng_key = jax.random.split(rng, num_steps)
        return jax.lax.scan(
            meanfield_approximate_step, state, rng_key
            )
    
    return run_optimization(init_params)
```

Fitting a model looks like:
```python
import matplotlib.pyplot as plt
import numpy as np

import optax
import tensorflow_probability.substrates.jax as tfp

tfd = tfp.distributions

rng = jax.random.PRNGKey(0)

seed0, seed1, rng = jax.random.split(rng, 3)
X = jax.random.normal(seed0, (100, 98))
y = X @ np.arange(98) + jax.random.normal(seed1, (100,))

@tfd.JointDistributionCoroutineAutoBatched
def model():
    sigma = yield tfd.HalfNormal(5.0, name='sigma')
    mu = yield tfd.Normal(0.0, 1.0, name='mu')
    beta = yield tfd.Sample(tfd.Normal(mu, sigma), X.shape[-1], name='beta')
    yield tfd.Normal(X @ beta, 1.0, name="y")

# init_position = model.sample(seed=rng)
pinned = model.experimental_pin(y=y)
init_position = pinned.sample_unpinned(seed=rng)

bijectors = pinned.experimental_default_event_space_bijector()
def log_prob_fn(unbound_param):
    param = bijectors.forward(unbound_param)
    log_det_jacobian = bijectors.forward_log_det_jacobian(unbound_param)
    return pinned.unnormalized_log_prob(param) + log_det_jacobian
```

```python
# This is just one way to do it. We could also use a flattened array to represent mu and rho
mu_param = jax.tree_map(jnp.zeros_like, init_position)
rho_param = jax.tree_map(jnp.zeros_like, init_position)
init_params = (mu_param, rho_param)

optimizer = optax.chain(optax.clip(10.), optax.adam(1.))
output = meanfield_approximate(rng, init_params, log_prob_fn, optimizer)
```
[1] https://arxiv.org/abs/1603.00788