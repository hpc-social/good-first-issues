---
tags: argo-traj,enhancement,stale
title: "Add Yamazaki et al (2020) terrain-following interpolation algorithm "
html_url: "https://github.com/euroargodev/argopy/issues/213"
user: gmaze
repo: euroargodev/argopy
---

Hi folks,
A great new method was developed [here](https://github.com/euroargodev/terrain-following) to interpolate Argo float trajectories under ice.
I think this would be worth implementing in argopy, as suggested by https://github.com/euroargodev/terrain-following/issues/1

The new API could look like this:
```python
from argopy import DataFetcher as ArgoDataFetcher
argoset = ArgoDataFetcher(mode='expert').float(2900114)
ds = argoset.load().data.argo.traj_interp_terrain_following()
```
and the data set would have new LAT_INTERP/LON_INTERP variables with interpolated values

Getting topographic data could be made with [argopy Topo fetcher](https://argopy.readthedocs.io/en/latest/generated/argopy.TopoFetcher.html) so that users wouldn't have to manage this
