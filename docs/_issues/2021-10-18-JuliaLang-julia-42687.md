---
tags: ,REPL
title: "shell mode: switch to pkg mode with ']'"
html_url: "https://github.com/JuliaLang/julia/issues/42687"
user: timholy
repo: JuliaLang/julia
---

From `julia>` mode, `;` switches to `shell>` and `]` switches to `pkg>`.
From `pkg>` mode, `;` switches to `shell>`
From `shell>` mode, `]` does **not** switch into `pkg>`

It would be great to fix the last one.
