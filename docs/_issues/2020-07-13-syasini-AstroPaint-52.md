---
tags: 
title: "Einasto Profile"
html_url: "https://github.com/syasini/AstroPaint/issues/52"
user: syasini
repo: syasini/AstroPaint
---

Implement the Einasto profile module. The new module should live here `astropaint/profiles/Einasto.py`. The structure can be identical to [NFW](https://github.com/syasini/AstroPaint/blob/master/astropaint/profiles/NFW.py). Essentially the only difference would be the `rho_3D` function. 

The other profiles (kSZ, deflection_angle, etc) should be factorized into a separate module and then called into NFW and Einasto. Will open another issue for this soon. 
