---
title: "Domain diagnostics"
html_url: "https://github.com/sxs-collaboration/spectre/issues/4382"
user: nilsvu
repo: sxs-collaboration/spectre
---

We need to improve our capabilities to analyze where our computational grids need more or less resolution. This is important for many reasons:

- We need to understand if some parts of the domain are severely underresolved, leading to large numerical errors.
- Wasting resolution on regions of the domain that are overresolved significantly increases the cost of a simulation.
- These diagnostics form the basis for adaptive mesh-refinement (AMR) algorithms that adjust the resolution automatically throughout a simulation.

Here's a list of useful diagnostics. We should evaluate the strengths and limitations of these quantities carefully while implementing them. This knowledge will be important for implementing AMR algorithms, so please document your findings!

- [x] Power monitors. See Sec. 5.1 in https://arxiv.org/abs/1405.3693. @nikwit and I have implemented these partially in Python, so talk to us.
- [x] Numerical vs analytic Jacobian (see @nilsdeppe's comments below).