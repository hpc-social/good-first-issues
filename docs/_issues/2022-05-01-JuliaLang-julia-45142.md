---
tags: ,doc
title: "Explicitly document the `missing` behavior for all functions that handle `missing` values"
html_url: "https://github.com/JuliaLang/julia/issues/45142"
user: CameronBieganek
repo: JuliaLang/julia
---

I think that every function that handles `missing` values should have its handling of `missing` values documented in its docstring. There are two possible ways to do this:

- Add discussion of the handling of `missing` values to the generic `foo(x)` docstring.
- Add separate docstrings for all the `foo(::Missing)`, `bar(::Missing, ::Any)`, etc, methods.
    - This approach won't work for methods that take iterators, like `all`, `any`, `maximum`, and `minimum`.

Functions that handle missing values currently do not have fully specified APIs, since their docstrings make no mention of `missing` values. My position is that docstrings should always strive to fully specify the API of their functions, so that in theory a person could write an entire application by referring only to the docstrings. In other words, you shouldn't have to run `foo(missing)` in the REPL in order to determine whether `foo` handles `missing` values.