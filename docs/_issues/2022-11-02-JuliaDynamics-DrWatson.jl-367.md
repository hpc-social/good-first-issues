---
tags: ,enhancement,running-listing
title: "Allow `dict_list` to return other types than dictionaries"
html_url: "https://github.com/JuliaDynamics/DrWatson.jl/issues/367"
user: Datseris
repo: JuliaDynamics/DrWatson.jl
---

In many cases users may want to have the configuration parameters of their programs to be a dedicated Julia composite type. This has many advantages, including customizing `savename`. It would be nice if `dict_list` could create objects of a given composite type instead of dictionaries. Would also make the whole integration with `produce_or_load` simpler.

A very simple, but probably not the most performant way to do this, is to leave dict_list as is, and add a final conversion step by using our functions `dict2struct` and/or `ntuple2struct`.