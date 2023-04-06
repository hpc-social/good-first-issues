---
tags: ,Docs,Effort-low,Package-novice,Performance,time
title: "DOC: avoid iteration for light travel time of lots of objects"
html_url: "https://github.com/astropy/astropy/issues/7755"
user: StuartLittlefair
repo: astropy/astropy
---

In our user survey, @stargaser mentioned they had issues at ZTF when calculating light travel times for tens of thousands of sources in a degree patch of the sky. It might be worth a section in the performance area of the ```Time``` documentation comparing run times of the following approaches:

```python
import numpy as np
import astropy.coordinates as coord
import astropy.units as u
from astropy.time import Time

ra = np.random.normal(0.0, 1.0, 50000)
dec = np.random.normal(0.0, 1.0, 50000)

coos = coord.SkyCoord(ra, dec, unit=u.deg)
observatory = coord.EarthLocation.of_site('lapalma')

%time time.light_travel_time(coos, location=observatory)
CPU times: user 56 ms, sys: 3.21 ms, total: 59.2 ms
Wall time: 58.2 ms
<TimeDelta object: scale='tdb' format='jd' value=[ 0.00497521  0.00495056  0.00497048 ...,  0.00499594  0.0049838
  0.00502038]>

%time ltts = [time.light_travel_time(coo, location=coos.location) for coo in coos]
CPU times: user 16min 45s, sys: 5.08 s, total: 16min 50s
Wall time: 16min 58s
```
