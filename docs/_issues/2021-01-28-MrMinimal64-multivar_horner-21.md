---
tags: ,enhancement,help-wanted
title: "allow multi coefficient polynomials"
html_url: "https://github.com/jannikmi/multivar_horner/issues/21"
user: jannikmi
repo: MrMinimal64/multivar_horner
---

a user might want to represent and evaluate multiple polynomials (different coefficients) with the same properties.
This is useful e.g. for gradients (= partial derivative polynomial for each dimension)!
add support for 2D coefficient arrays and adjust Numba jit compilation.
then the gradient can be returned as a single polynomial with the same exponents but 2D coefficients or multiple distinct polynomials with smaller exponent matrices.
The naivel canonical polynomial evaluation for 2D coefficient arrays can benefit from reusing intermediary results.
If someone wants to work on this let me know here. I have example code ready for this already.