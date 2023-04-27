---
tags: comp-genmod,type-enh,type-refactor
title: "ENH/REF  GLM simplify computation if is_canonical"
html_url: "https://github.com/statsmodels/statsmodels/issues/4269"
user: josef-pkt
repo: statsmodels/statsmodels
---

triggered by looking at the computation of IRLS weights in #4267

We currently don't use any special casing and simplified computation in GLM when a canonical link function is used.

This would create some speed improvements, but the more important point is that it will most likely increase numerical stability and precision.

Example Pregibon 1981 on regression diagnostics points out that the weights in IRLS are zero for the corner case p=0 and p=1 in Binomial. However, we divide by the variance which divides by zero in this case, most likely 0/0. I guess we get currently around this with clipping away from the boundaries.

Other maybe more important cases are gamma and negative binomial where canonical link functions don't work so well, and the non-canonical log link works better.
I haven't checked, but my guess is that some of the messy instabilities in corner cases will likely disappear.

(a bit related: thequackdaddy added an EIM option for the hessian in fit to avoid the complicated OIM which is generic for non-canonical cases. However, we don't skip the unnecessary part for OIM in the canonical link case, where OIM==EIM, IIRC)

