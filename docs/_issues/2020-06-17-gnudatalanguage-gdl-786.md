---
tags: ,c++-only,help-wanted
title: "simplify and document code --- code review"
html_url: "https://github.com/gnudatalanguage/gdl/issues/786"
user: GillesDuvert
repo: gnudatalanguage/gdl
---

A number of functions scattered in GDL's code more or less do the same thing and should be factorized in one place in order to be easily maintained. Especially if these functions use basic system functions that may differ with the system (macOS, unix, MSW..). And, the factorized function should be documented (with [Doxygen](https://www.doxygen.nl) in mind).
Take the example of `strtol()` . It is used in at least 4 different places, in 4 different templates functions, so potentially 4*12 or so variants, to do exactly the same thing: convert a string in a integer. Fine as long as there is no problem. But there is a problem: the function is supposed sometimes to return a byte, a long, and unsigned long64 etc, calling for differents strategies (use strtoll, strtoull..) on different architectures. Factorization is the solution. There are other examples, mostly around string manipulation, unix/windows file naming, regular expressions, array sorting...

A code review and implementation of this factorization for these (few? not sure) basic system function calls would be a very very valuable contribution from somebody willing to do it and not particularly interested in the GDL language itself.