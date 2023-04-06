---
title: "Degree to radian"
html_url: "https://github.com/pyomeca/biorbd/issues/313"
user: Ipuch
repo: pyomeca/biorbd
---

In passive torque,

We would prefer to work in radian than in degree.

We could patch it from the .biomod reader if we read a flag "in rad" we work in radian otherwise it is in degree.

It would prevent breaking all previous examples.

@Amedeo
