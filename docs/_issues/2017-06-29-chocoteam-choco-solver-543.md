---
title: "FiniteAutomaton : declare a factory for intersection, etc."
html_url: "https://github.com/chocoteam/choco-solver/issues/543"
user: cprudhom
repo: chocoteam/choco-solver
---

Some methods are declared in `FiniteAutomaton` but should be moved to a factory to avoid mis-interpretation.
F-ex, calling `a1.intersection(a2)` returns a new `FiniteAutomaton` which is the result of the intersection between 'a1' and 'a2' but also modifies 'a1' (which is unexpected).