---
tags: ,bug,enhancement
title: "STELLAR module: issues with output density"
html_url: "https://github.com/VirtualPlanetaryLaboratory/vplanet/issues/133"
user: jbirky
repo: VirtualPlanetaryLaboratory/vplanet
---

I found two issues with the density output using the STELLAR module:

1. Density is listed under 'system properties' in the output log file instead of 'stellar parameters'
2. The log file says that the density is in solar units, but it's actually a factor of ~12 off from solar (see plot)

plot:
![density_evol.pdf](https://github.com/VirtualPlanetaryLaboratory/vplanet/files/5974581/density_evol.pdf)

infiles and log:
[star.txt](https://github.com/VirtualPlanetaryLaboratory/vplanet/files/5974587/star.txt)
[vpl.txt](https://github.com/VirtualPlanetaryLaboratory/vplanet/files/5974589/vpl.txt)
[Trappist.log](https://github.com/VirtualPlanetaryLaboratory/vplanet/files/5974593/Trappist.log)

