---
tags: Makie,help-wanted,vizcon
title: "allow for `x` axis in series."
html_url: "https://github.com/MakieOrg/Makie.jl/issues/499"
user: mschauer
repo: JuliaPlots/Makie.jl
---

Currently in https://github.com/JuliaPlots/AbstractPlotting.jl/blob/3f43c46e156b1da2b80e36daedd435a64b1edfc4/src/basic_recipes/basic_recipes.jl#L320 the `x`-axis is fixed to `1:n`. A reasonable signature would be `x, Y` where `x` is vector like and `Y` is the matrix of the stacked `y`-values.