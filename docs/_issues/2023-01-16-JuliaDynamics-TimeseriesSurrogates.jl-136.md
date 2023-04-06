---
tags: ,enhancement,method-request
title: "Multidimensional version of `RandomShuffle` and `BlockShuffle`. "
html_url: "https://github.com/JuliaDynamics/TimeseriesSurrogates.jl/issues/136"
user: kahaaga
repo: JuliaDynamics/TimeseriesSurrogates.jl
---

## Is your feature request related to a problem? Please describe.

It would be nice to have more surrogate methods that operate on multidimensional input data. This becomes necessary in conditional independence testing for multivariate data, for example in the context of conditional mutual information with high-dimensional marginal spaces.

Currently, we only have the `ShuffleDimensions` multivariate surrogate, but shuffling the dimensions is not the desired behaviour when, for example, one wants to break temporal associations. 

## Describe the solution you'd like

The `RandomShuffle` and `BlockShuffle` surrogate methods can be straight-forwardly extended to multivariate `Dataset`s (from the `StateSpaceSets` package) Since these methods just permute the *indices* of the datasets, they can also be used to shuffle the `SVector`s of a `Dataset`.

## Implementation strategy

This should be pretty easy to implement. It is just a matter of allocating the proper re-useable storage container in the `SurrogateGenerator` struct. Instead of enforcing `surrogenerator(x::AbstractVector, rf::RandomShuffle, args...)`, the first argument should be allowed to be any iterable `surrogenerator(x, rf::RandomShuffle, args...)` and `similar(x)`/`copy(x)` should be used to allocate the re-usable container.
