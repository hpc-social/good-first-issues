---
tags: ,Documentation,Good-first-issue,topic-color/colorbar
title: "[Bug]: TwoSlopeNorm behaves like CenteredNorm"
html_url: "https://github.com/matplotlib/matplotlib/issues/22197"
user: MartenSkogh
repo: matplotlib/matplotlib
---

### Bug summary

The behavior of TwoSlopeNorm has changed from [Colormap Normalization 3.4.0]( https://matplotlib.org/3.4.0/tutorials/colors/colormapnorms.html#twoslopenorm-different-mapping-on-either-side-of-a-center) to [Colormap Normalization 3.5.1]( https://matplotlib.org/stable/tutorials/colors/colormapnorms.html#twoslopenorm-different-mapping-on-either-side-of-a-center). See the colorbar being centered and no longer a continuous linear scale.


### Code for reproduction

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cbook as cbook
from matplotlib import cm

dem = cbook.get_sample_data('topobathy.npz', np_load=True)
topo = dem['topo']
longitude = dem['longitude']
latitude = dem['latitude']

fig, ax = plt.subplots()
# make a colormap that has land and ocean clearly delineated and of the
# same length (256 + 256)
colors_undersea = plt.cm.terrain(np.linspace(0, 0.17, 256))
colors_land = plt.cm.terrain(np.linspace(0.25, 1, 256))
all_colors = np.vstack((colors_undersea, colors_land))
terrain_map = colors.LinearSegmentedColormap.from_list(
    'terrain_map', all_colors)

# make the norm:  Note the center is offset so that the land has more
# dynamic range:
divnorm = colors.TwoSlopeNorm(vmin=-500., vcenter=0, vmax=4000)

pcm = ax.pcolormesh(longitude, latitude, topo, rasterized=True, norm=divnorm,
                    cmap=terrain_map, shading='auto')
# Simple geographic plot, set aspect ratio beecause distance between lines of
# longitude depends on latitude.
ax.set_aspect(1 / np.cos(np.deg2rad(49)))
ax.set_title('TwoSlopeNorm(x)')
cb = fig.colorbar(pcm, shrink=0.6)
cb.set_ticks([-500, 0, 1000, 2000, 3000, 4000])
plt.show()
```


### Actual outcome

**In 3.5.1**  
![image](https://user-images.githubusercontent.com/7512099/148927510-d4109e88-e055-40a7-8a0d-be3c0d63d9f8.png)


### Expected outcome


**In 3.4.0**  
![image](https://user-images.githubusercontent.com/7512099/148927566-1ca4ba09-ecc2-4f60-8dcd-6a94b9224e89.png)


### Additional information

_No response_

### Operating system

Alpine (Windows Subsystem for Linux)

### Matplotlib Version

3.5.1

### Matplotlib Backend

agg

### Python version

3.8.10

### Jupyter version

3.2.5

### Installation

pip