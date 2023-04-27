---
tags: bug
title: "Initial ice sheets heights shouldn't be negative!"
html_url: "https://github.com/VirtualPlanetaryLaboratory/vplanet/issues/150"
user: RoryBarnes
repo: VirtualPlanetaryLaboratory/vplanet
---

The option dinitIceSheetHeight in POISE allows negative arguments, which shouldn't be allowed. It'd be better to change it so that if the user inputs a negative value, it defaults to meters since the ice sheet height is positive definite.