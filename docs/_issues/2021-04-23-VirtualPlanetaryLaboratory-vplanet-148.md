---
tags: ,enhancement
title: "Read in input files only once"
html_url: "https://github.com/VirtualPlanetaryLaboratory/vplanet/issues/148"
user: RoryBarnes
repo: VirtualPlanetaryLaboratory/vplanet
---

Right now the code opens and read the input files for every option. It'd be better to open them once and read the entire file into an array of chars, one line per element.