---
tags: improvement
title: "collect_results! : path"
html_url: "https://github.com/JuliaDynamics/DrWatson.jl/issues/116"
user: JonasIsensee
repo: JuliaDynamics/DrWatson.jl
---

When collecting results using `collect_results!` the path to the files is automatically added.
This is great but we currently add the full system-path.
For better portability one could change this to just save the path relative to the project-rootfolder.
Then things would stay coherent over different machines.