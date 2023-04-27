---
tags: Good-first-issue,typeCoverage,typeTesting
title: "Test default default cases for strongly typed enum serialization"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/2925"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description

Test default default cases (corresponding to non-existing enum values) for strongly typed enum serialization.

### Expected behavior

Default cases should also be tested.

### Actual behavior

Default cases are not being tested because the set of enum values for testing are systematically built using enum values corresponding to existing cases, e.g.
```
  const std::set<itk::RecursiveGaussianImageFilterEnums::GaussianOrder> allGaussianOrder{
    itk::RecursiveGaussianImageFilterEnums::GaussianOrder::ZeroOrder,
    itk::RecursiveGaussianImageFilterEnums::GaussianOrder::FirstOrder,
    itk::RecursiveGaussianImageFilterEnums::GaussianOrder::SecondOrder
  };
  for (const auto & ee : allGaussianOrder)
  {
    std::cout << "STREAMED ENUM VALUE RecursiveGaussianImageFilterEnums::GaussianOrder: " << ee << std::endl;
  }
``` 

Corresponding to:
https://github.com/InsightSoftwareConsortium/ITK/blob/828453d1bf61c487310d2d8c9570093e08798a40/Modules/Filtering/Smoothing/test/itkRecursiveGaussianImageFiltersTest.cxx#L515

### Reproducibility

%100.

### Versions

ITK `master`.

### Additional Information

When sorting directories by the uncovered lines in ascending order:
https://open.cdash.org/viewCoverage.php?buildid=7606267&filtercount=1&field1=filename/string&compare1=63&value1=&status=-1

It becomes apparent that many directories/files are 1 line away from getting a 100% code coverage, and such lines correspond to default cases (corresponding to non-existing enum values) for strongly typed enum serialization.

See, for example, the `Modules/Filtering/Smoothing/src` directory, which is only missing the following lines:
https://open.cdash.org/viewCoverageFile.php?buildid=7606267&fileid=39050963

This would be an easy change and is an easy way to increase the coverage across the code base. With this change, many of the concerned files would obtain 100% code coverage, and the number of files with such (complete) coverage rate would probably exceed those within any other coverage rate (probably for the first time), which would be a milestone.

Ideally we should also test for the actual printed values (cross-referencing #983). That can be done in a separate PR.