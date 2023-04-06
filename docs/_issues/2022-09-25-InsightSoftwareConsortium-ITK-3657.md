---
tags: ,Good-first-issue,typeTesting
title: "Make the `itkMultiLabelSTAPLEImageFilterTest` quantitative"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/3657"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description

Make the `itkMultiLabelSTAPLEImageFilterTest` quantitative:
https://github.com/jhlegarreta/ITK/blob/1800d81600f247421532667c3c59fd35e42a24de/Modules/Segmentation/LabelVoting/test/itkMultiLabelSTAPLEImageFilterTest.cxx

As mentioned in https://github.com/InsightSoftwareConsortium/ITK/commit/b64bc4f4d63044fec3874c8ba713e56b1c5a84c1, a regression error was introduced by setting the `m_MaximumNumberOfIterations` instance variable value to 0. As the output of the test is only displayed in the standard output but not checked, the regression had gone unnoticed until the coverage decrease was spot.

### Steps to Reproduce

Check the expected confusion matrices.

### Expected behavior

The output value of the confusion matrices should be verified in order to ensure that no regressions are introduced in the filter's expected outputs.

### Actual behavior

The value of the confusion matrices is not checked, and thus, if the filter implementation or the test is modified, changes might go unnoticed.

### Reproducibility

100%

### Versions

`master`

### Environment

Applies to any environment.

### Additional Information

Cross-reference https://github.com/InsightSoftwareConsortium/ITK/pull/3627#issuecomment-1249939595.