---
tags: ,enhancement,help-wanted,io
title: "[ENH] download and use horizon data to affect sky diffuse and far shading"
html_url: "https://github.com/pvlib/pvlib-python/issues/1290"
user: mikofski
repo: pvlib/pvlib-python
---

**Problem statement**
1. most satellite data (CPR, SGIS, PSM3, ...) doesn't include effects of horizon, this info is downloaded separately, but pvlib doesnt' currently have any iotools for horizon download. Some sources for horizon data are pvgis and meteonorm, but make sure to follow the correct conventions. Also it's possible that horizon data can be derived from GIS elevation data like USGS or SRTM.
2. once horizon data is obtained in the format {azimuth, elevation} then it can be applied to (a) reduce the sky dome of isotropic diffuse sky irradiance by integrating the ratio of the solid angles and (b) account for "far shading" or shade that affects the entire PV array uniformly, _eg_ like the sun being partially obscured by a very distant (typically >30-km) mountain, 

**Describe the solution you'd like**
1. add pvgis horizon download to iotools
2. complete #758 which given a horizon profile (azimuth, elevation) calculates the effect on diffuse sky
3. ditto for far shading

**Describe alternatives you've considered**
require users to account for horizon effects in the satellite data separately. pvgis already offers this option, but afaik, psm3 does not. Not sure about cpr or sgis

**Additional context**
- related to #758 
- @annalisemckenzie adding the pvgis download could be a good first contribution, interested?