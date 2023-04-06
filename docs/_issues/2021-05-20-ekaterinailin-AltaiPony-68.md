---
tags: ,enhancement
title: "Pass detrended_flux and detrended_flux_err directly to constructor"
html_url: "https://github.com/ekaterinailin/AltaiPony/issues/68"
user: ekaterinailin
repo: ekaterinailin/AltaiPony
---

At the moment, you can only pass 'flux' and 'flux_err' to 'FlareLightCurve'. 

#### What needs to be created or improved?
We also want to  pass 'detrended_flux' and 'detrended_flux_err' to 'FlareLightCurve' directly, too. 

#### Can you provide an example?
<!-- Provide a link or minimal code snippet that demonstrates the issue. -->

This is how it works now:
```python
lc = FlareLightCurve(data['TIME'])
lc["detrended_flux"] = data['detrended_flux']
lc["detrended_flux_err"] = data['detrended_flux_err']

# OR

lc = FlareLightCurve(data, targetid=999)
# data can be a simple dict or an astropy Table
```

This is how we may want it to work, too:


```python
lc = FlareLightCurve(data['TIME'], detrended_flux=data['detrended_flux'], detrended_flux_err=data['detrended_flux_err'], )
```
#### What is the goal / expected behaviour?
<!-- Describe the behavior you expected and how it differs from the behavior observed in the example. -->


