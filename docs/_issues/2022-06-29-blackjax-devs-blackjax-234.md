---
tags: ,documentation,enhancement,help-wanted
title: "Add a pretty printer that returns information that is useful for the user"
html_url: "https://github.com/blackjax-devs/blackjax/issues/234"
user: rlouf
repo: blackjax-devs/blackjax
---

The information that is returned should be actionable for the user:

- What family of models this sampler is compatible with / best used for;
- The parameters and their signification. A brief description of their effect on the chain;
- The adaptation schemes that can be used for the algorithm's parameters;
- Literature reference;
- Related samplers.

The pretty printer can use `functools.singledispatch` and the information can be dispatched right where the algorithms are implemented (rather than the kernel?). This will require careful work on the types beforehand.