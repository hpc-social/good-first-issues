---
tags: enhancement
title: "Plots.jl recipes"
html_url: "https://github.com/MakieOrg/Makie.jl/issues/368"
user: asinghvi17
repo: JuliaPlots/Makie.jl
---

Plots.jl has a lot of small, easy-to-implement convenience functions and recipes that would be nice to have in AbstractPlotting, or StatsMakie.

- [ ] `stephist`: 
```julia
    stephist(x)
    stephist(x)

Make a histogram step plot (bin counts are represented using horizontal lines
instead of bars). See `histogram`. 
```


- [ ] `scatterhist`: 
```julia
    scatterhist(x)
    scatterhist!(x)

Make a histogram scatter plot (bin counts are represented using points 
instead of bars). See `histogram`. 
```

- [x] `sticks`:
```julia
    sticks(x,y)
    sticks!(x,y)

Draw a stick plot of y vs x. 
```
![sticks](https://user-images.githubusercontent.com/32143268/60090423-f6350a00-975b-11e9-9d4b-d14e95b3655e.png)

- [x] `hexbin`: Note that Plots doesn't seem to have support for this.
```julia
    hexbin(x,y)
    hexbin!(x,y)

Make a hexagonal binning plot (a histogram of the observations `(x[i],y[i])` 
with hexagonal bins)
```

- [x] `hline`: 
```julia
    hline(y)
    hline!(y)

Draw horizontal lines at positions specified by the values in 
the AbstractVector `y`
```

- [x] `vline`: 
```julia
    vline(x)
    vline!(x)

Draw vertical lines at positions specified by the values in 
the AbstractVector `x`
```

- [ ] `ohlc`:    
```julia
    ohlc(x,y::Vector{OHLC})
    ohlc!(x,y::Vector{OHLC})

Make open-high-low-close plot. Each entry of y is represented by a vertical 
segment extending from the low value to the high value, with short horizontal 
segments on the left and right indicating the open and close values, respectively.
```


- [ ] `curves`: 
```julia
    curves(x,y)
    curves!(x,y)

Draw a Bezier curve from `(x[1],y[1])` to `(x[end],y[end])` 
with control points `(x[2],y[2]), ..., (x[end-1],y[end]-1)`
```

- [x] `pie`:  Plot a pie diagram

- [ ] `areaplot`:
```julia
    areaplot([x,] y)
    areaplot!([x,] y)
Draw a stacked area plot of the matrix y.
```