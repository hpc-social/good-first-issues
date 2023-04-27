---
title: "Kerr in harmonic coordinates"
html_url: "https://github.com/sxs-collaboration/spectre/issues/4515"
user: nilsvu
repo: sxs-collaboration/spectre
---

We need to upgrade our harmonic Schwarzschild solution to harmonic Kerr so we can produce initial data with spinning black holes in harmonic coordinates. This "superposed harmonic Kerr" initial data is one of the initial data configurations currently used routinely in the SpEC code, so it's quite important to generate in in SpECTRE too. A good place to read about harmonic coordinates is chapter 4.3 in the book "Numerical Relativity" by Baumgarte & Shapiro. The particular harmonic Kerr solution is discussed in this paper: https://journals.aps.org/prd/abstract/10.1103/PhysRevD.56.4775. First steps are:

- Get access to SpEC and read the `HarmonicKerr` class. The task is to port this class over to SpECTRE.
- Code up the solution in `src/PointwiseFunctions/AnalyticSolutions/GeneralRelativity/HarmonicKerr.{h,c}pp`.
- Test the solution thoroughly, e.g. by checking that it solves the Einstein equations numerically.
- Generate initial data sets with two spinning black holes and compare to SpEC.