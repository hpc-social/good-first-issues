---
tags: ,enhancement
title: "Improve the example scripts"
html_url: "https://github.com/NeuralEnsemble/PyNN/issues/245"
user: apdavison
repo: NeuralEnsemble/PyNN
---

The current set of example scripts covers a rather limited range of functionality, with a lot of very similar examples, many of which were written a long time ago.

We should retire some of the old examples, and write some new ones, showcasing a wider range of PyNN's current functionality. The examples should also generate (optional) plots, where appropriate.
#### Ideas
- [ ] an IF neuron and an HH neuron with different levels of current injection
- [ ] single IF neuron receiving synaptic input from a Poisson source
- [ ] population of Izhikevich neurons, each with a different parameterization, responses to current injection
- [ ] ditto for AdExp neurons
- [ ] a 2D population with spatially-modulated input currents
- [ ] a demonstration of synaptic facilitation and depression
- [ ] a comparison of different STDP weight-dependencies
- [ ] a demonstration of different current sources
- [ ] Brunel
- [x] Vogels-Abbott CUBA/COBA benchmarks
- [ ] a native NEST example
- [ ] a native NEURON example
- [ ] a demonstration of distance-dependent connectivity
- [ ] an example of writing a new connector, e.g. giving Gabor-shaped connectivity.

Please feel free to add ideas below...
#### Checklist for examples
- well commented
- complete docstring, include usage instructions
- has "--plot-figure" command-line option
