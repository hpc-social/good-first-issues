---
tags: ,help-wanted,performance,strings,unicode
title: "Use shift based DFA for utf8 validation"
html_url: "https://github.com/JuliaLang/julia/issues/41533"
user: Keno
repo: JuliaLang/julia
---

There's a post going around on Twitter for how to write a super fast DFA, e.g. for UTF8 validation: https://twitter.com/_rsc/status/1413843059972923394?s=19. We have a UTF8 validation function, so we should try this technique. Should be reasonably simple to do.