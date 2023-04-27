---
tags: Good-first-issue,typeEnhancement,typeInfrastructure
title: "Parse strings as multi-element data structures in tests"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/514"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description
Some tests require a number of arguments that are part of the same data structures (e.g. the image size, or resolution). Having a utility function in a single place to parse the input parameter strings as a multi-element data structure (e.g. a vector) would be desirable.

### Expected behavior
To be able to parse a string as a vector or whatever multi-element data structure.

### Actual behavior
Developer's are forced to parse the string on each test that requires such an input.