---
tags: ,Good-first-issue,typeCoverage
title: "Add quantitative tests to `itk::FastMarchingImageFilterBase`."
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/599"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description

As mentioned in PR #114, the `itk::FastMarchingFilterBase` class would be better covered if the corresponding tests were quantitative (i.e. the output was compared against a baseline), and  additional test cases were included.

### Expected behavior

Improvement in the robustness of the class by:
- Making the tests quantitative adding some trial points.
- Testing non-identity spacing images.
- Testing on non-null origin images.

### Actual behavior

No comparison against a baseline is done.
Default identity spacing and null origin images tested.

### Reproducibility

%100.

### Versions

ITK `master`. 

### Additional Information

This should be relatively easy to address.
