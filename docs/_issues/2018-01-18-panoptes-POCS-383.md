---
tags: ,scheduler
title: "Account for field of view in horizon constraint"
html_url: "https://github.com/panoptes/POCS/issues/383"
user: wtgee
repo: panoptes/POCS
---

The Horizon constraint needs to account for the entire field of view for the camera rather than just the center of the image. This can be simple to start by just adding half the field to the center point that is used but could eventually account for different azimuths and camera rotation.