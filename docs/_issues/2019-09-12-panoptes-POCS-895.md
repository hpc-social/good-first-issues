---
tags: ,Enhancement,mount
title: "Consider astroalign for tracking corrections"
html_url: "https://github.com/panoptes/POCS/issues/895"
user: wtgee
repo: panoptes/POCS
---

We currently plate-solve each image and do a comparison with the pointing image in order to determine the x and y pixel offsets that are used for tracking correction. This works but can be slow depending on the plate-solve, especially when operating from a Raspberry Pi.

Look into using the new [astroalign](https://github.com/toros-astro/astroalign) library to obtain pixel offsets.

**Describe the solution you'd like**
Replace the plate-solving in `pocs.observatory.Observatory.analyze_recent` with an astroalign offset.

https://github.com/panoptes/POCS/blob/develop/pocs/observatory.py#L492-L498


**Related Issues/PRs**
#489 