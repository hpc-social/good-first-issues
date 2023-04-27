---
tags: GSOC,Python-API,design,docs,enhancement
title: "Implement and use type system"
html_url: "https://github.com/LiberTEM/LiberTEM/issues/506"
user: uellue
repo: LiberTEM/LiberTEM
---

Currently, we use type hinting only sparsely in the API.

In the future, we should pervasively specify types in such a way that they are both machine and human readable.

This helps to make our documentation clear and precise. Additionally, it may help to find issues by using automated checking routines like [mypy](http://mypy-lang.org/). The LiberTEM code base has grown to such a volume that such tests help to maintain coherence across the project.

Parts of this issue that can be solved individually:

- [x] Integrate a type checker like mypy into our CI pipeline
- [ ] Types for the `Context` class
  - [ ] Parameters
  - [X] Return types, done in #643 
- [ ] Types for all parts of the UDF interface