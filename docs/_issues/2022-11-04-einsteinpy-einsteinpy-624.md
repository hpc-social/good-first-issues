---
tags: plotting
title: "Geodesic Plotting improvements"
html_url: "https://github.com/einsteinpy/einsteinpy/issues/624"
user: JeS24
repo: einsteinpy/einsteinpy
---

### 🐞 **What bugs you?**
(Continued from #610)

#612 added an `aspect` ratio option to `*GeodesicPlotter`s that helps avoid skewed plots. However, at the moment, we are using `plotly`'s nomenclature for aspect modes for the `InteractiveGeodesicPlotter` and `matplotlib`'s nomenclature for the `StaticGeodesicPlotter`. This is mainly because `matplotlib` is yet to finalize the API for the aspect options ([targeted for `3.7.0`](https://github.com/matplotlib/matplotlib/pull/23552) and also see [this](https://stackoverflow.com/questions/8130823/set-matplotlib-3d-plot-aspect-ratio/73749399#73749399)).

To me, [matplotlib's names](https://matplotlib.org/3.6.0/users/prev_whats_new/whats_new_3.6.0.html#equal-aspect-ratio-for-3d-plots) for the options make more sense than [Plotly's](https://plotly.com/python/3d-axes/#fixed-ratio-axes). I think, it will be great to offer a unified set of `aspect` options, since the most used API arguments for both the plotting modules (`InteractiveGeodesicPlotter` and `StaticGeodesicPlotter`) follow the same naming convention. Of course, users can still make changes using the `fig` or `ax` attributes for both the plotters, if they want to. 

We can also take a look into arguments such as `figsize`, that are also not uniform across these modules.

<!-- Update me if PR -->

### 🎯 **Goal**
To bring uniformity to the plotting API.

### 💡 **Possible solutions**
Once matplotlib finalizes the API around aspect and scaling, we can decide on a common set of names and offer them as options for `aspect` across both the modules. `matplotlib`'s `equal` and `plotly`'s `data` are going to the most relevant ones, but others can be useful too. So, the tasks are:
- [ ] Decide on a set of options.
- [ ] Add them to both plotting modules.
- [ ] Also look into homogenizing arguments such as `figsize`.

### 📋  **Steps to solve the problem**
Refer: https://docs.einsteinpy.org/en/latest/dev_guide.html

 * Comment below about what you've started working on.
 * Add, commit, push your changes
 * Submit a pull request and add this in comments - `Addresses #<put issue number here>`
 * Ask for a review in comments section of pull request
 * Celebrate your contribution to this project 🎉
