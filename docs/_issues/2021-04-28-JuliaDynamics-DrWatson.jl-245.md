---
tags: 
title: "Pkg.activate is not enough for forcing correct environment"
html_url: "https://github.com/JuliaDynamics/DrWatson.jl/issues/245"
user: fredrikekre
repo: JuliaDynamics/DrWatson.jl
---

This is perhaps a bit of a drive-by comment (I haven't used the package myself), and perhaps it has been discussed before but `Pkg.activate` is not enough to make sure you use the correct environment. Here is one example:

```
$ JULIA_LOAD_PATH=/tmp/Project.toml: julia --project=. -q
julia> Base.active_project()
"/tmp/tmp.ovN3Dd5eeE/Project.toml"

julia> Base.load_path()
4-element Vector{String}:
 "/tmp/Project.toml"
 "/tmp/tmp.ovN3Dd5eeE/Project.toml"
 "/home/fredrik/.julia/environments/v1.6/Project.toml"
 "/opt/julia/julia-1.6/share/julia/stdlib/v1.6"
```