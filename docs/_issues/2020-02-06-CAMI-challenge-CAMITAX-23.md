---
tags: enhancement
title: "Suggestion : Run checkm on more than 1 MAG at a time"
html_url: "https://github.com/CAMI-challenge/CAMITAX/issues/23"
user: michoug
repo: CAMI-challenge/CAMITAX
---

Hi,
I have a few hundred MAGs that I want to taxonomically check and I realized that the checkm software is run MAG per MAG as are all the other steps. However, the pplacer step in checkm takes quite some time as it needs to put the tree in memory to place the MAG each time. When running it by itself, I think that it's much faster to do it with all the MAGS at the same time.
Using the default 8 cores, the checkm software is using only 2 cores at a time and the other 6 are not used as soon as prodigal and mash are finished
Would it be possible to implement this in the pipeline or maybe doing 20-30 at once?
Best
Greg
