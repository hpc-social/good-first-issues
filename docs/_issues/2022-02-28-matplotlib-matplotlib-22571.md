---
tags: ,Difficulty-Medium,Good-first-issue,New-feature,topic-arrow,topic-mplot3d
title: "[ENH]: FancyArrow in 3D"
html_url: "https://github.com/matplotlib/matplotlib/issues/22571"
user: patquem
repo: matplotlib/matplotlib
---

### Problem

Hello,

FancyArrow can not be used in 3D.
Some proposals (#21688) consists in creating a new class.
Could it be possible: 
1. to extend FancyArrow to 3D (as for quiver)
2. to solve -if possible- the arrow head problem representation when loocking the arrow along its axis (see the 2nd plot in the figure below)

Thanks,
Patrick

```
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyArrow
from mpl_toolkits.mplot3d import proj3d


class Arrow3D(FancyArrowPatch):
    """ Create fancy arrow (artist) for 3d matplotlib visualisation """

    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xarr, yarr, _ = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xarr[0], yarr[0]), (xarr[1], yarr[1]))
        FancyArrowPatch.draw(self, renderer)


fig, ax = plt.subplots(1, 2, figsize=(12, 5),
                       subplot_kw=dict(projection="3d",
                                       proj_type='ortho'))

ax[0].voxels(np.ones((1, 1, 1)), facecolors=[0, 0, 0, 0], edgecolors='k')
# ax[0].add_artist(FancyArrow(0, 0, 0, 1, 1, 1))
ax[0].add_artist(Arrow3D((0, 1), (0, 1), (0, 1), mutation_scale=50))

ax[1].voxels(np.ones((1, 1, 1)), facecolors=[0, 0, 0, 0], edgecolors='k')
ax[1].view_init(elev=28, azim=45)
# ax[1].add_artist(FancyArrow(0, 0, 0, 1, 1, 1)))
ax[1].add_artist(Arrow3D((0, 1), (0, 1), (0, 1), mutation_scale=50))

plt.show()
```
![image](https://user-images.githubusercontent.com/16154687/155967746-2eadecad-c976-4b29-97cd-5f8858f25698.png)



### Proposed solution

_No response_