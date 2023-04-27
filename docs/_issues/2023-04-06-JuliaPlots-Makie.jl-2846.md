---
tags: documentation
title: "Can't turn of the grid of two axis simultaneously"
html_url: "https://github.com/MakieOrg/Makie.jl/issues/2846"
user: pabloemontes
repo: JuliaPlots/Makie.jl
---

The following code does not give the desired output
```
using CairoMakie

Fig = Figure()

ax1 = Axis(Fig[1, 1], title = "Axis 1")
ax2 = Axis(Fig[1, 2], title = "Axis 2")

hidedecorations!(ax1, grid = false)
hidexdecorations!(ax2, grid = false)

Fig
```
I expect this to give me two axis side by side with no grids, but both grids appear. If by the contrary one of the grids is set to true, then only one grid appears and the other one is hidden.