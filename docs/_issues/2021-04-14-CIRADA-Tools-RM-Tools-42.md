---
tags: enhancement
title: "Polarization angles use wrong convention"
html_url: "https://github.com/CIRADA-Tools/RM-Tools/issues/42"
user: Cameron-Van-Eck
repo: CIRADA-Tools/RM-Tools
---

Currently, the polarization angles are in the range (-90,90], but the RMTable convention asks for angles in the range [0,180). It would be better to be consistent.
This is only for the band-center polarization angles; the derotated angles seem to be OK already? This should be confirmed.