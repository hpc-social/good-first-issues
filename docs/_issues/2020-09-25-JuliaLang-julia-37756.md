---
tags: bug,display-and-printing,help-wanted
title: "bad print format for Complex{Unsigned}"
html_url: "https://github.com/JuliaLang/julia/issues/37756"
user: vtjnash
repo: JuliaLang/julia
---

Complex number printing assumes that simple concatenation will produce something meaningful:
```
julia> 0x1e*im
0x00 + 0x1eim

julia> 0x1eim
ERROR: syntax: invalid numeric constant "0x1ei"
```