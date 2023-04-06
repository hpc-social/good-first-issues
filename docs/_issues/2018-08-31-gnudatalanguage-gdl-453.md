---
tags: ,Low-priority
title: "multiple usage of same keyword (IDL --> duplicate keyword)"
html_url: "https://github.com/gnudatalanguage/gdl/issues/453"
user: alaingdl
repo: gnudatalanguage/gdl
---

e.g.

plot, findgen(10), psym=3, psym=5, psym=6, xstyle=2, xstyle=4

IDL : % Duplicate keyword PSYM in call to: PLOT

GDL : seems to use last occurrence of given keyword