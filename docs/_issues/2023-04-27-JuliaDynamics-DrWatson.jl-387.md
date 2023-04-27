---
tags: enhancement,git
title: "tag with git commit message"
html_url: "https://github.com/JuliaDynamics/DrWatson.jl/issues/387"
user: harrybooth
repo: JuliaDynamics/DrWatson.jl
---

Maybe I have overlooked this functionality, but would it be possible to add the git commit message to the result dictionary using [DrWatson.@tag!](https://juliadynamics.github.io/DrWatson.jl/v0.8/save/#DrWatson.@tag!)?

This would be really useful, as for example the git commit hash e.g. gitcommit => "96df587e45b29e7a46348a3d780db1f85f41de04" is non-descriptive, especially if you are trying to compare different versions of the same data and understand what the change was. Allowing the git commit message to be included, e.g. "changed parameter x to y" would be a nice automated way to relate code changes to experimental results. 

 
