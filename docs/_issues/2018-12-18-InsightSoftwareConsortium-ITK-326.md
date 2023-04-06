---
tags: Good-first-issue,typeDocumentation
title: "Fix remote modules' PyPI documentation long description"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/326"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description

Fix the Python Package Index (PyPI) remote module documentation long description.

### Steps to Reproduce

Check that the project **long description** in a remote module's `setup.py` file has white spaces for each new line.

To check the effect of missing white spaces at the end of the line, look for a remote-module whose Python package has been uploaded to the PyPI, e.g. [ITKPhaseSymmetry](https://pypi.org/project/itk-phasesymmetry/), or more generally, looking for keywords such as [itk](https://pypi.org/search/?q=itk). Then verify that the missing white spaces makes two consecutive line words to be concatenated.

**Even if the module has not been uploaded to PyPI**, all remotes (look for the `itk-module` tag in GitHub) must be fixed.

### Expected behavior

A module's long description must be a well-written sentence.

### Actual behavior

Words at the end of a line and at the beginning of the other are concatenated.

### Reproducibility

Always.

### Versions

All.

### Environment

Any

### Additional Information

Each remote will need to be cloned locally, fixed, and a PR opened for each.