---
tags: ,IRDB,documentation,help-wanted
title: "MICADO Docs, show how to change Seeing with AnisoCADO PSF"
html_url: "https://github.com/AstarVienna/irdb/issues/59"
user: AstarVienna
repo: AstarVienna/irdb
---

JvdB
can we change the seeing? I want to see what a halo-dominated background in a semi-crowded region looks like

Add a small notebook in the MICADO docs or ScopeSim docs
- add an `AnisocadoPSF` object
- fiddle with the Seeing parameter
- display a comparison of the images

Note that this requires `AnisocadoPSF` to actually pass the seeing value from `kwargs` to `aniso.AnalyticalScaoPsf`, which it currently does not do --> enhancement needed in ScopeSim to allow this