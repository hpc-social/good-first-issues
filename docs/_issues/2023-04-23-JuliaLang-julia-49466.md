---
tags: REPL
title: "REPL.fuzzyscore heuristics could be better"
html_url: "https://github.com/JuliaLang/julia/issues/49466"
user: jakobnissen
repo: JuliaLang/julia
---

The heuristics don't work very well in practise, partly because a mismatch near the beginning of the string completely messes up the algorithm, whereas numerous insertions/deletions don't do much.

For example
```julia
julia> REPL.fuzzyscore("bupercalifragilisticexpialidocious", "supercalifragilisticexpialidocious")
-68.0

julia> REPL.fuzzyscore("parasid", "supercalifragilisticexpialidocious")
6.59
```
Or
```julia
julia> REPL.fuzzyscore("IJilia", "IJulia")
-3.0933333333333337

julia> REPL.fuzzyscore("IJilia", "MotionCaptureJointCalibration")
5.5633333333333335
```
Maybe it would be better to use something like Lehvenstein by default with some slight heuristics on top?