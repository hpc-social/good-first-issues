---
tags: ,documentation
title: "Document LineStrings and their use"
html_url: "https://github.com/MakieOrg/Makie.jl/issues/1903"
user: asinghvi17
repo: JuliaPlots/Makie.jl
---

As I understand, the LineString type allows the user to plot multiple disconnected lines in the same plot call.  However, there is no documentation to reflect this.  We should add some, and possibly consider adding documentation (in the docs of `lines`, `surface`, `heatmap`, etc.) about which types they accept.  Possibly also a listing of `convert_arguments` signatures which are applicable to each recipe?