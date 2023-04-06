---
tags: ,documentation
title: "Allow custom link text in `\\mylinkref` in docs"
html_url: "https://github.com/MakieOrg/Makie.jl/issues/2802"
user: asinghvi17
repo: JuliaPlots/Makie.jl
---

This would be pretty nice, noticed in #2787.  

Some background: Makie's docs use Franklin.jl, which allows you to create custom commands which it picks up on and executes.  These commands are defined in `docs/utils.jl`, so you would just have to change the implementation of the `lx_mylinkref` function there to accept a keyword argument `text` which would determine the text of the link.