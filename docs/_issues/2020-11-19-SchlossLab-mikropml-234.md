---
tags: ,documentation
title: "Better explain the groups param & batch effects in the intro vignette"
html_url: "https://github.com/SchlossLab/mikropml/issues/234"
user: kelly-sovacool
repo: SchlossLab/mikropml
---

Note from lab meeting code club on the documentation:

There was confusion about how the `groups` parameter works and why one would want to use it. Need to explicitly state that observations (rows) from the same group are kept together in the train/test split. Overfitting was brought up as a concern -- thinking that using `groups` might cause models to be overfit. But really it would reveal whether overfitting has occurred.