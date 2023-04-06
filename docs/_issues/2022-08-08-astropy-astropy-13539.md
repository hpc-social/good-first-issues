---
tags: ,Feature-Request,nddata
title: "Avoid logger info in CCDData.read when unit specifies matches that in FITS file"
html_url: "https://github.com/astropy/astropy/issues/13539"
user: astrofrog
repo: astropy/astropy
---

At the moment, when reading a FITS file with BUNIT set to adu with ``CCDData.read``, one gets the following info message:

```
INFO:astropy:using the unit adu passed to the FITS reader instead of the unit adu in the FITS file.
```

it might make sense to avoid emitting this message if the units match? (cc @mwcraig)

