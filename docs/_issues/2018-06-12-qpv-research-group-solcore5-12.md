---
tags: ,enhancement
title: "Small improvements to the LightSource class"
html_url: "https://github.com/qpv-research-group/solcore5/issues/12"
user: dalonsoa
repo: qpv-research-group/solcore5
---

The LightSource class deals with light sources (the solar spectrum or other spectra) and there are currently two things to improve:

1. Currently, the "total_power" attribute returns the total power by integrating the spectrum in the requested spectral range. It will be convenient to change it so it provides the power of the total spectrum, even if the wavelength range of interest is much smaller. For example, the "total_power" of the AM1.5g solar spectrum should be 1000 W/m2 even if we ask the spectrum just from 300nm to 900 nm because we are modelling a GaAs solar cell. 

2. The laser light source is defined by a gaussian curve... in wavelength. That does not make sense from a physical point of view it it should be defined as a gaussian curve in energy.   

