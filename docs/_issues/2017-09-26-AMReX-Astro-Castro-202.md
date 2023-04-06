---
tags: gravity,help-wanted,study
title: "Recommend a new default value of gravity.abs_tol"
html_url: "https://github.com/AMReX-Astro/Castro/issues/202"
user: maxpkatz
repo: AMReX-Astro/Castro
---

The Poisson solve absolute tolerance sets the accuracy of the Poisson solve. Given the value of abs_tol, the error level targeted in the Poisson solve is abs_tol * 4 * pi * G * rho_max, where rho_max is the maximum density on the domain. For Cartesian simulations the default value is 1.e-11, and for non-Cartesian the default value is 1.e-10.

At high resolution, and/or for complicated mass distributions, this tolerance can be too tight, and the multigrid solve fails. We should study the effect of the gravity tolerance and possibly recommend a new tolerance. If it is justified, the new tolerance should be looser so that the default value fails in fewer cases. However, we should not make it so loose that the effect noticeably deteriorates the accuracy of our simulations.

Issues to study:
(1) Differences between Cartesian and cylindrical/spherical problems
(2) Performance, both for a single processor and for multiple processors
(3) Accuracy -- for a given lower tolerance, how much does the answer change?

These should be studied with a well-used problem like DustCollapse, and also one or two more complicated problems like the Evrard collapse and wdmerger.