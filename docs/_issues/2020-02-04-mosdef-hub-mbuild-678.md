---
tags: low-priority
title: "Potential lingering issues with XYZ files"
html_url: "https://github.com/mosdef-hub/mbuild/issues/678"
user: mattwthompson
repo: mosdef-hub/mbuild
---

Copying from [Parashara's comment](https://github.com/mosdef-hub/mbuild/pull/410#pullrequestreview-352632439) 

Just comparing with MDTraj:
- MDTraj includes the date/time the file was created in the header. It could be cool to include that, but totally unnecessary 
- MDTraj uses 3 decimal places. Looks like some formats only accept 3? (https://open-babel.readthedocs.io/en/latest/FileFormats/XYZ_cartesian_coordinates_format.html). Not sure if this is something we care about, but it might be nice to include a `n_decimal_places` kwarg for the saver. 
- The xyz values for a water box mbuild system are slightly different when using MDTraj vs the new xyz saver. This is probably due to the extra decimal places in each of the xyz files saved before the PACKMOL run. Not an issue, but good to note in case someone is trying to exactly replicate a result.  