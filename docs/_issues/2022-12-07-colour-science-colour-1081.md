---
tags: Discussion,Feature,Good-First-Issue
title: "Helper functions for arithmetic on MSDS"
html_url: "https://github.com/colour-science/colour/issues/1081"
user: tjdcs
repo: colour-science/colour
---

In a previous discussion the need for getting the sum of an MSDS object came up. I've needed to do this twice recently. Once where I needed the sum of the spectrum because I was computing the total power of a spectroradiometer measurement between the requisite wavelengths. And another time when each of the underlying instances of SpectralDistribution represented independent control channels of a light source (RGB for a spectral display model, for example) 

So summation would need to have respect to some "axis", either the sum of the values for each SD object or the sum at every wavelength across all SDs 

> You are right, there is no easy way to do that but it would not be too hard to implement dedicated methods for that. Under the hood, the `colour.MultiSpectralDistributions` is a bunch of `colour.SpectralDistributions` instances.
> 
> I'm thinking that the following would be useful for example:
> 
> - `colour.MultiSpectralDistributions.sum`
> - `colour.MultiSpectralDistributions.average`
> - `colour.MultiSpectralDistributions.median`
> 
> What do you think @tjdcs?
> 

_Originally posted by @KelSolaar in https://github.com/colour-science/colour/discussions/1078#discussioncomment-4319112_
    