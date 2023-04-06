---
tags: ,enhancement,help-wanted
title: "Simplify `minimize_lbfgs` and `pathfinder_adaptation`"
html_url: "https://github.com/blackjax-devs/blackjax/issues/387"
user: junpenglao
repo: blackjax-devs/blackjax
---

We are [computing the inverse hessian from factors](https://github.com/blackjax-devs/blackjax/blob/1aaa6f64bbcb0557b658604b2daba826e260cbc6/blackjax/optimizers/lbfgs.py#L291) as in formula II.1 in the Pathfinder paper. And we have a [test](https://github.com/blackjax-devs/blackjax/blob/1aaa6f64bbcb0557b658604b2daba826e260cbc6/tests/test_optimizers.py#L110-L125) comparing the inverse hessian from pathfinder compare to from `jaxopt`.

It should be ok to use the gamma directly output from `jaxopt`, as the result seems to be equivalent numerically (from that 1 test at least). It will be great to compare the calculation to understand what is the difference and make a decision.
