---
tags: Status-Help-Wanted,Type-Documentation
title: "Suggestions for documentation improvements"
html_url: "https://github.com/jump-dev/JuMP.jl/issues/2348"
user: odow
repo: jump-dev/JuMP.jl
---

Hi there! 

This issue is a catch-all for documentation improvement suggestions. I'll keep it updated with things to work on, rather than having lots of separate issues.

 * If you have suggestions for things to add to the documentation, leave a comment below.
 * If you're looking to contribute to JuMP, picking something off this list is a great place to start!

## General editing

The easiest place to start is just to read through any portion of the docs and give it a good edit. Spelling, grammar, or edits for clarity are always good. 

The easiest way to get started is to pick a Markdown page, e.g.,:
https://github.com/jump-dev/JuMP.jl/blob/master/docs/src/index.md
and then click the "Edit this file" pencil icon:
![image](https://user-images.githubusercontent.com/8177701/138628553-531dc435-951c-4cc1-8151-05d17200d4fa.png)
Make your changes, and then scroll to the bottom of the page for instructions on how to submit a pull request. 

If you're not sure about a change, make it, open a pull request, and then we can discuss it.

<s>

## Improve current tutorials

A lot of the tutorials are quite basic and consist of just functions. We should revise the existing tutorials to show a wider range of interesting JuMP and Julia syntax and features.

I think it'd also help if each tutorial used a standardized template. Perhaps something like
````
# Title

This tutorial was contributed by XXX. It is based on the article/book/example of CITE.

## Goal

The goal of this tutorial is to demonstrate ...

## Setup

This tutorial requires the following packages
```Julia
using JuMP
import Foo
```

In addition, you need to data files [bar.txt] and [baz.json]. These files are contained in the JuMP repository 
```
const _DATA_DIR = joinpath(@__DIR__, "data")
```

## Now start the tutorial


````

- [x] linear/knapsack
- [x] linear/multicommodity-flow
- [x] linear/workforce-schedulig
- [x] linear/steel-t3
- [x] nonlinear/qcp
- [x] nonlinear/rosenbrock
- [x] nonlinear/mle
- [x] nonlinear/clnlbeam
- [x] conic/kmeans
- [x] conic/correlation
- [x] conic/sdp-max-cut
- [x] conic/min-distortion
- [x] conic/robust-uncertainty

## Add new tutorials

### Structuring larger models

I wrote a nice answer here:
https://discourse.julialang.org/t/integrating-mathoptinterface-into-an-industry-scale-project-e-g-constraint-management/71943/2?u=odow

### Improved MIP modeling tricks

People consistently ask how to reformulate `max` and `abs`. These should be added. The Mosek modeling cookbook is the gold-standard for this: https://docs.mosek.com/modeling-cookbook/mio.html

### Parallelism

I get this question quite frequently. A section should be added to the docs explaining the different options.

Links with content

 * https://stackoverflow.com/questions/64177415/create-jump-model-with-multi-threading-in-julia
 * https://discourse.julialang.org/t/parallel-solves-in-gurobi-jl/9908/8?u=odow
 * https://discourse.julialang.org/t/improve-performance-of-a-code-with-very-large-of-garbage-collection/75548/20

### How to debug a JuMP model

We need a getting started on debugging.

 0. The Julia debugger doesn't work well with JuMP.
 1. Update your packages to the latest version. JuMP will only support the LTS an the latest point release.
 2. Try a different solver
 3. Simplify the problem
 4. Comment out constraints until the infeasibility resolves itself
 5. Write tests. 

@benlauwens has a _great_ chapter on debugging: https://benlauwens.github.io/ThinkJulia.jl/latest/book.html#chap21. We should link to it, and re-phrase some of the suggestions in a JuMP context.

### Parametric problems

The same user as #2662 asked for ways to solve a collection of problems over a set of parameters. We don't have a good way of doing this in JuMP (we have `@NLparameter`, but not `@parameter`), but it could be scripted using the modification API (or even just rebuilding the problem).

We should write a tutorial with the different approaches. Here's their suggestion:

`![image](https://user-images.githubusercontent.com/8177701/129110774-cc2688d9-ac27-40e2-b6b0-390e1d7c2e0a.png)`

I like the idea of visualizing the heat map.
</s>
## Prior art

There are two existing sources of documentation that I would like us to work towards:

 * The AMPL book https://ampl.com/resources/the-ampl-book/
 * Mosek modeling cookbook https://docs.mosek.com/MOSEKPortfolioCookbook-a4paper.pdf

