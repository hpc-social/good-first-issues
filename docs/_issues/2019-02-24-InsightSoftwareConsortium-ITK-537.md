---
tags: ,Good-first-issue,typeBug
title: "Uninitialized member variables"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/537"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description

Several classes have uninitialized member variables.

### Steps to Reproduce

Run the tests, and check the output to the standard output:
- `itk::BSplineScatteredDataPointSetToImageFilter`: **Uninitialized members in class**:
`itk::BSplineScatteredDataPointSetToImageFilter::m_OmegaLatticePerThread`
`itk::BSplineScatteredDataPointSetToImageFilter::m_DeltaLatticePerThread`
https://open.cdash.org/testDetails.php?test=736332599&build=5770289

- `itk::ThresholdLabelerImageFilter`: **Uninitialized members in class**:
`itk::ThresholdLabelerImageFilter::m_Thresholds`
`itk::ThresholdLabelerImageFilter::m_RealThresholds`
https://open.cdash.org/testDetails.php?test=736333475&build=5770289

### Expected behavior

**All** member variables must have an initial/default value using the [convention adopted in ITK](https://discourse.itk.org/t/simpletype-m-var-initialvalue/651).

### Actual behavior

Members do not have any assigned value when being printed in tests.

### Reproducibility

100%.

### Versions

Current `master` branch.

### Environment

Independent of the environment.