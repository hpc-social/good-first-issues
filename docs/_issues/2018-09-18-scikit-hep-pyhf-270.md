---
tags: feat/enhancement
title: "Test all public methods of classes (mainly pdf.Model)"
html_url: "https://github.com/scikit-hep/pyhf/issues/270"
user: lukasheinrich
repo: scikit-hep/pyhf
---

# Description

In https://github.com/diana-hep/pyhf/pull/269 we have seen a decrease in coverage because we relied on nested calls to methods to traverse the calls. A refactoring of the internal code then left some methods uncovered.

We should make sure that all public methods of classes (mainly `pyhf.pdf.Model`) are tested explicitly or remote them to internal methods by prepending a underscore. Otherwise refactorings might break users relying on these methods

(somewhat related to semantic versioning )

Classes

* [ ] `pyhf.pdf.Model`
  * [ ] `expected_auxdata`
  * [ ] `expected_actualdata`
  * [ ] `expected_sample`
  * [ ] `expected_data`
  * [ ] `constraint_logpdf`
  * [ ] `logpdf`
  * [ ] `pdf`
  

# Relevant Issues and Pull Requests

If there are relevant issues and pull requests for this feature please list and link them here

- #269 
