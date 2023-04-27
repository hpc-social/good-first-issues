---
tags: enhancement
title: "Validate extents when creating a Mesh"
html_url: "https://github.com/sxs-collaboration/spectre/issues/2652"
user: nilsvu
repo: sxs-collaboration/spectre
---

# Feature request:

`Mesh` currently accepts any `extents`, i.e. number of points per dimension. However, each combination of spectral basis and quadrature has a minimum and maximum number of grid points. For example, any mesh with "GaussLobatto" quadrature must have at least two points (on the faces of the element). We should check this requirement when the mesh ist constructed, in particular when it is constructed from input-file options to give the user a helpful error message.

To implement this feature we need the following:
- Two functions in the `Spectral` namespace that take a `Spectral::Basis` and a `Spectral::Quadrature` at runtime and return the minimum and maximum number of grid points, respectively (in addition to the existing functions that are evaluated at compile-time).
- Logic in the `Mesh` constructors that validate the extents and give useful error messages.

### Component:

- [x] Code
- [ ] Documentation
- [ ] Build system
- [ ] Continuous integration
