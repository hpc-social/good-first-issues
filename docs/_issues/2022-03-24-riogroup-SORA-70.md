---
tags: ,documentation,effort_low
title: "AstropyDepreciationWarning"
html_url: "https://github.com/riogroup/SORA/issues/70"
user: GianmarcoBroilo
repo: riogroup/SORA
---

Hello everybody! I am new to SORA, I am trying to predict occultations of Io based on a paper that suggested occultations in 2019 and 2021. If I try to predict them, using this code:
` io = Body(name='Io',
                ephem=['/Users/gianmarcobroilo/Desktop/Tudat/SORA/input/jup365.bsp', '/Users/gianmarcobroilo/Desktop/Tudat/SORA/input/de441_part-1.bsp'])

print(io)


pred = prediction(body=io, time_beg='2019-09-09',time_end='2019-09-12',mag_lim=16)

print(pred)`

I get this issue only when it actually finds occultation possibilities:
`Searching occultations in part 1/1
Generating Ephemeris between 2019-09-09 00:00:00.000 and 2019-09-11 23:59:00.000 ...
Downloading stars ...
    65 Gaia-EDR3 stars downloaded
Identifying occultations ...
WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
Traceback (most recent call last):`

Thank you for the help!
