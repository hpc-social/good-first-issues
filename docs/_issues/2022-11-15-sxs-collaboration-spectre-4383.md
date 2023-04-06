---
tags: 
title: "Neutron star surface finder algorithm"
html_url: "https://github.com/sxs-collaboration/spectre/issues/4383"
user: nilsvu
repo: sxs-collaboration/spectre
---

Find the surface of a neutron star in numeric volume data. This is needed to adapt the computational grid to the stellar surface so the surface discontinuity doesn't spoil exponential convergence of our initial data solver. It's also useful to impose the regularity condition on the elliptic equation for the velocity potential, which we want to solve only within the star. Basic idea:

- Choose the desired angular resolution for the surface in terms of spherical harmonic `l_max` and `m_max`. Then the goal is to find the radius of the surface at each angular collocation point to construct a `Strahlkorper` representing the stellar surface (look at `NumericalAlgorithms/SphericalHarmonics/Strahlkorper.hpp`).
- Implement a root finding algorithm that determines the radius of zero density or unit enthalpy along every radial "ray" through the angular collocation points.
- Bonus points for finding the isosurface of _any_ value of the enthalpy / density / etc, so we can try to adapt the domain also to discontinuities in equations of state with phase transitions.

Literature: Read up on "surface-fitting coordinates" in the context of binary neutron star initial data. Also talk to me.