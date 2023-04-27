---
tags: Documentation
title: "PDD solver: error in the documentation on how to access the output"
html_url: "https://github.com/qpv-research-group/solcore5/issues/109"
user: dalonsoa
repo: qpv-research-group/solcore5
---

The documentation for the PDD solver states that the output is provided as a nested dictionary. However, that is not correct: it is provided as a `State` object with the different keys accesible as attributes. For example:

```python
solar_cell[junction_index]['QE']['EQE']
```
should be:
```python
solar_cell[junction_index].qe.EQE
```
[The examples are incorrect](http://docs.solcore.solar/en/master/Solvers/DriftDiffusionUtilities.html#drift-diffusion-utilities) and so is the [description of the dictionary](http://docs.solcore.solar/en/master/Solvers/DriftDiffusionUtilities.html#output-dictionary) at the end. 