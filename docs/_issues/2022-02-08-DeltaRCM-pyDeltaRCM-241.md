---
tags: ,help-wanted
title: "Getting starting cells for parcels implicitly assumes that inlet is located along x=0 coordinate"
html_url: "https://github.com/DeltaRCM/pyDeltaRCM/issues/241"
user: amoodie
repo: DeltaRCM/pyDeltaRCM
---

Getting starting cells for parcels implicitly assumes that inlet is located along `x=0` coordinate.

* https://github.com/DeltaRCM/pyDeltaRCM/blob/edf69276adfd1f61ef6bf3ed3f59a0827fee6346/pyDeltaRCM/water_tools.py#L93-L94
* https://github.com/DeltaRCM/pyDeltaRCM/blob/edf69276adfd1f61ef6bf3ed3f59a0827fee6346/pyDeltaRCM/sed_tools.py#L567-L568

This has not been an issue so far, but could be better generalized to have `self.inlet` be a list of flat cell indices, or a `nx2` list of x-y indices (probably preferring the former).