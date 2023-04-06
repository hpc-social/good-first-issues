---
tags: ,community,help-wanted
title: "Contribute !"
html_url: "https://github.com/blackjax-devs/blackjax/issues/154"
user: rlouf
repo: blackjax-devs/blackjax
---

Hey :wave: 

You are here because you considered contributing to `blackjax` for at least a split second. Thank you! But sometimes we are just not quite sure what to work on/don't want to bother the maintainer. We've been there. That is why we put together a list of the projects that are up for grabs on `blackjax`.

**You can pick any of these, open an issue to signal you are working on it and run with it.**

## Documentation :book: 

Documentation is obviously lacking, and as the user base is expanding, writing documentation is probably the biggest contribution one could make. Even setting things up (with Sphinx) would be a huge help!

- Move the documentation to ReadTheDocs (but still execute the examples)
- Move examples to a different repo to ease CI
- Add a mat plot l’on style sheet for the plots in doc
- Use `daft` to represent models in the examples
- Better API documentation

## Examples :ferris_wheel: 

Examples are useful not only to get to know the library, but also to learn about the pros and cons of different algorithms. We are looking for any example contribution, and would be extra happy with:

* Any comparison with optimization (looking at you, neural networks!);
* Comparisons between sampling algorithm;
* Examples with many dimensions / big datasets; problems where you typically wouldn't use bayesian inference;
* Examples that explains how an algorithm works.

For instance:

- Sample from CNN on MNIST blackjax-devs/sampling-book#14 
- How to write a sampling loop? blackjax-devs/blackjax#320
- How to run adaptation for several chains? blackjax-devs/blackjax#321
- Complex combination of algorithms: mgrad within Gibbs within SMC for a GP, for instance
- How to distribute gradient computation for HMC?


## Algorithms :hammer: 

We are of course always looking for new algorithms! The library currently has a focus on gradient-based algorithms and SMC, and we are currently looking for the following to expand the library's scope:

- Likelihood-free inference, blackjax-devs/blackjax#288 
- Riemannian HMC (implicit and explicit integration) blackjax-devs/blackjax#283
- Slice sampling
- Ensemble methods such as [Ensemble preconditing MCMC](https://arxiv.org/abs/1607.03954)  blackjax-devs/blackjax#176
- [Mixed HMC](https://arxiv.org/abs/1909.04852)
- [Delayed rejection sampling](https://arxiv.org/pdf/2012.14881.pdf) blackjax-devs/blackjax#368
- MALT (https://github.com/blackjax-devs/blackjax/issues/206)

## Adaptation :sparkles: 

In practice adaptation algorithms (that compute reasonable values for the sampling algorithms' parameters) are as important as samplers. Here are the algorithms that we know of and would like to implement:

- [ChEEs](https://proceedings.mlr.press/v130/hoffman21a) blackjax-devs/blackjax#282 
- [x] [MEADS](https://proceedings.mlr.press/v151/hoffman22a/hoffman22a.pdf)
- [SNAPER-HMC](https://arxiv.org/abs/2110.11576)
- [Empirical HMC](https://arxiv.org/abs/1810.04449)
- Coupled HMC blackjax-devs/blackjax#64

## Approximation 🍰 

The next best thing when you can't _easily_ sample from the posterior! There are a lot of exciting new algorithms that could be use alone or combine with MCMC

- [x] [Pathfinder](https://arxiv.org/abs/2108.03782) 
- [ ] [MUSE](https://arxiv.org/abs/2112.09354) https://github.com/marius311/muse_inference/issues/1
- [ ] [adjoint-differentiated Laplace approximation](https://arxiv.org/abs/2004.12550)
- [ ] Variational inference, especially [SVGD](https://arxiv.org/abs/1608.04471) blackjax-devs/blackjax#385 blackjax-devs/blackjax#397

## Meta-algorithms :cloud: 

- Gibbs sampling
- HMC coupling
- Parallel tempering (replica exchange)

## Testing :mag_right: 

Performance is good, accuracy and correctness is often better. We welcome implementations of the following algorihms:

- [Simulation Based Calibration](https://arxiv.org/pdf/1804.06788.pdf)
- [Kernel goodness-of-fit test](http://proceedings.mlr.press/v48/chwialkowski16.pdf)
- Better tests for the algorithms based on mathematical convergence results