---
tags: severity_minor,urgency_low
title: "Nuclear timescale calculation makes assumptions about core mass"
html_url: "https://github.com/TeamCOMPAS/COMPAS/issues/430"
user: TomWagg
repo: TeamCOMPAS/COMPAS
---

**Describe the bug**
Whilst plotting the nuclear timescale with Selma we noticed that it seemed off by a factor of ~3-5 from what it should be for high mass stars. The timescale doesn't seem to be used in any meaningful way except printing so only problem would be when people are using this for other things. The equation used by COMPAS is assuming that core mass makes up a certain fraction of the total mass, so it works for solar mass stars but once you get to higher mass stars things get iffy.

**Label the issue**
`urgency_low`,`severity_moderate`

**To Fix**
See [BaseStar::CalculateNuclearTimescale_Static](https://github.com/TeamCOMPAS/COMPAS/blob/production/src/BaseStar.cpp#L2230). This uses the last expression of Kalogera & Webbink 1996 Eq.3, but if you look at this equation in the text you see you should really be using the core mass expression, not using the second expression
<img width="578" alt="image" src="https://user-images.githubusercontent.com/21990332/98278169-374f4800-1f66-11eb-9b5e-d8f931e7105f.png">