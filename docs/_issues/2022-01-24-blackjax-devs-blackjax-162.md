---
tags: enhancement,help-wanted
title: "Separate random proposals and the RMH acceptance step"
html_url: "https://github.com/blackjax-devs/blackjax/issues/162"
user: rlouf
repo: blackjax-devs/blackjax
---

The RMH acceptance step is used by many MCMC algorithms across the library and we should thus be able to import it from a separate module. Should probably go in `proposals.py`.

We can also refactor the `rmh` kernel and rename it `random_walk`. I am not certain we should expose gaussian random walk as it is rather easy to build a random walk from any proposal. TBD.