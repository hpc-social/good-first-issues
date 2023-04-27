---
tags: Good-first-issue,HelpUs
title: "Improve documentation on coordinate systems"
html_url: "https://github.com/healpy/healpy/issues/841"
user: Cameron-Van-Eck
repo: healpy/healpy
---

Hello!

Love the module, thanks for working on it. I have one peeve I want to share with you, because it cost me two hours of debugging today:

I would be very happy if you could make the documentation on coordinate systems more clear throughout. Many of the functions (e.g., `visufunc.mollview`) have a coordinate keyword that uses 'E', 'G', and 'C' as shorthand for the coordinate systems and to set up transformations -- this functionality is great. What's missing is clarifying what those 3 stand for. I, naively, assumed 'E' was for 'Equatorial', and used 'EG' to try to convert my equatorial-coordinate data to Galactic coordinates, and was stumped for why the output positions were wrong.

Digging through the documentation (after two hours of eliminating all other possible sources of error), the ONLY place I could find the shorthands explained was in the docstring for `fitsfunc.write_map` (a function I've never needed, and so otherwise would not have looked at); this finally let me solve my problem. It would be fantastic if you could propagate this information throughout the documentation (e.g., other docstrings that use this convention, such as `visufunc.mollview`), so that others don't fall into the same confusion as I did.

Thanks very much,
Cameron Van Eck