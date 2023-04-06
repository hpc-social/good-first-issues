---
tags: ,enhancement
title: "Add \"completely symmetric\" fourth-order tensors to notation.ExplicitConverter"
html_url: "https://github.com/JulianKarlBauer/mechkit/issues/40"
user: JulianKarlBauer
repo: JulianKarlBauer/mechkit
---

Exchange of completely symmetric tensors, such as fiber orientation tensors of fourth order in a
minimal, i.e., nearly redundancy-free notation is a common task for engineers working with short fiber reinforced composites.

Support of
```
tensors = <bunch of  fourth order fiber orientation tensors>

con = mechkit.notation.ExplicitConverter()
con.convert(
inp=tensors, source="tensor", target="exchange", quantity="fiber_orientation"
)
```

with "exchange", e.g., being
```
[
N_1111, N_2222, N_3333,
N_2233, N_1133, N_1122,
N_1123, N_2223, N_3323, 
N_1113, N_2213, N_3313, 
N_1112, N_2212, N_3312, 
]
```
See also equations (38) to (40) in 
[Variety of fiber orientation tensors, Bauer and Böhlke 2021](https://journals.sagepub.com/doi/full/10.1177/10812865211057602)


It is clear, that, e.g., N_3333 could be omitted, as only 14 components are independent, but 
not omitting it, will enable usage for, e.g., diffusion-weighted magnet resonance tomography tensors of fourth order, 
which have no normalized trace.