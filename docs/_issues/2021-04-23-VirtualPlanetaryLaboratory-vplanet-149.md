---
tags: ,enhancement
title: "Printing of output parameters should be limited to those that are requested"
html_url: "https://github.com/VirtualPlanetaryLaboratory/vplanet/issues/149"
user: RoryBarnes
repo: VirtualPlanetaryLaboratory/vplanet
---

When the code outputs parameters, it loops over all possible values, MODULEOPTEND, which is inefficient. Instead the code should record the number of outputs per body and just loop over them. 