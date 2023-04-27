---
tags: comp-tsa,comp-tsa-statespace,type-enh
title: "ENH: Add rsquared and variants to state space models"
html_url: "https://github.com/statsmodels/statsmodels/issues/4734"
user: ChadFulton
repo: statsmodels/statsmodels
---

Currently the state space models don't compute any kind of R^2 type value, but it might be handy / desirable in some cases. "Forecasting, structural time series models and the Kalman filter" (Harvey, 1989) section 5.5.5 describes three variants:

- R^2 comparing fit to a model with just the mean (i.e. usual R^2): 1 - SSE / SSM
- R^2 comparing fit to a random walk + drift model: 1 - SSE  / SSDM (SSDM = sum of squares of first differences around the mean)
- R^2 comparing fit to a random walk + drift + seasonal dummies: 1 - SSE / SSDSM (SSDSM = sum of squares of first differences around the seasonal means)

This should not be too difficult to add (and also not urgent), so it might be good for someone who is interested in contributing a first PR.