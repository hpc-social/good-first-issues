---
tags: ,help-wanted
title: "Composition of Search Strategy with different limit"
html_url: "https://github.com/chocoteam/choco-solver/issues/567"
user: bourreauEric
repo: chocoteam/choco-solver
---

### Expected behavior
limit the first search strategy to 1 second  in solve THEN use the second strategy (to  improve the best so far solution)

### Actual behavior
search.limit Monitor are attach to search and not strategy.

### Minimal Working Example

Experienced with choco-solver-4.0.4

solv.setSearch(
  new AbstractStrategy[] { 
    Search.intVarSearch(new MaxRegret(), new IntDomainMax(), X),	
    Search.domOverWDegSearch(TableVariableCouleur)}
);
 solv.limitTime(1000);

can be 

solv.setSearch(
  new AbstractStrategy[] { 
    Search.intVarSearch(new MaxRegret(), new IntDomainMax(), X).limitTime(1000),	
    Search.domOverWDegSearch(TableVariableCouleur).limitTime(10000}
);

