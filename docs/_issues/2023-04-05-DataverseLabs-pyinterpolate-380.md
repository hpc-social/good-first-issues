---
tags: ,Good-First-Issue,feature,help-needed
title: "[Feature] [TheoreticalVariogram] [.autofit()] Add \"safe\" models as a one available parameter to choose from when checking theoretical models fit"
html_url: "https://github.com/DataverseLabs/pyinterpolate/issues/380"
user: SimonMolinsky
repo: DataverseLabs/pyinterpolate
---

**Is your feature request related to a problem? Please describe.**
The `.autofit()` method of the `TheoreticalVariogram` class takes an argument with model types to check which one describes data closely. The argument name Is `model_types`, and possible parameters are:

- 'all' - the same as list with all models
- 'circular'
- 'cubic'
- 'exponential'
- 'gaussian'
- 'linear'
- 'power'
- 'spherical'

There is no key to select only basic and safe model types.

**Describe the solution you'd like**
Add the key `safe` that later checks those models: `["linear", "power", "spherical"]`

**Describe alternatives you've considered**
n/a

**Additional context**
Compare it to the `all` key,