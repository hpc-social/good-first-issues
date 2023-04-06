---
tags: ,ci,help-wanted
title: "Replace uses of tempname in CI by mktemp"
html_url: "https://github.com/JuliaLang/julia/issues/43597"
user: Keno
repo: JuliaLang/julia
---

As of #38879 our temp path generation depends on the global RNG. That's probably not a bad idea in general, except that various parts of the test suite seed the global RNG, so this will cause reliable collisions in the test suite, so we'll get in trouble with tests stomping on each other. We should audit all uses of `tempname` in the test suite and replace them with mktemp unless they test the tempname function specifically.