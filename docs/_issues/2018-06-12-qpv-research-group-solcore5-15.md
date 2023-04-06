---
tags: ,Hacktoberfest,enhancement
title: "Rigorous models for tunnel junctions"
html_url: "https://github.com/qpv-research-group/solcore5/issues/15"
user: dalonsoa
repo: qpv-research-group/solcore5
---

Solcore has built in a simple resistive model for tunnel junctions, and also a parametric model, defined in terms of peak and valley currents and voltages. It also allows for externally defined tunnel junctions, by getting the tunnel junction IV curve as input. 

More rigorous models will allow to calculate the tunnel current from the layer structure of the junction. Some simple models that could be implemented are:

- Semiclassical Tunnel Diode model - S. M. Sze, Physics of Semiconductor devices (Chapter 8: Tunnel Devices).
- Louarn, K., Fontaine, C., Arnoult, A., Olivié, F., Lacoste, G., Piquemal, F., Bounouh, A., Almuneau, G.: Modelling of interband transitions in GaAs tunnel diode. Semicond. Sci. Technol. 31(6), 06LT01-6 (2016)