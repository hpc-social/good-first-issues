---
tags: numerical-investigation,question
title: "Why do factorial approximations generate different values"
html_url: "https://github.com/stillwater-sc/universal/issues/205"
user: Ravenwater
repo: stillwater-sc/universal
---

in the Sterling approximation of factorial(n), we use an oracle based on the sw::universal::decimal type, which is an adaptive data type, to generate a reference value. However, the direct approximation of the factorial through a native floating point type yields different approximations.

```
factorial(40) calculated with double and decimal oracle rounded to double
815915283247897734345611269596115894272000000000
8.1591528324789768e+47
8.1591528324789785e+47   TODO: explain the difference
factorial(50) calculated with double and decimal oracle rounded to double
30414093201713378043612608166064768844377641568960512000000000000
3.0414093201713376e+64
3.0414093201713381e+64   TODO: explain the difference
factorial(60) calculated with double and decimal oracle rounded to double
8320987112741390144276341183223364380754172606361245952449277696409600000000000000
8.3209871127413916e+81
8.3209871127413916e+81   TODO: explain why they show the same error
```

why is that the case?