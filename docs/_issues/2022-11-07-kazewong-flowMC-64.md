---
tags: ,enhancement
title: "Progress bar to be moved from inner loops to outer loops"
html_url: "https://github.com/kazewong/flowMC/issues/64"
user: marylou-gabrie
repo: kazewong/flowMC
---

Currently the tqdm runs on the local sampling steps and training steps, and no information is provided on the completion of the outer loops. It would more useful to the user to have the info on the progress at the level of the outer loops.