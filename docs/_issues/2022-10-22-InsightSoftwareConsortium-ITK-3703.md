---
tags: ,Good-first-issue,typeTesting
title: "IO ImageBase tests not exercised"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/3703"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description

The tests [`itkLargeImageWriteConvertReadTest`](https://github.com/InsightSoftwareConsortium/ITK/blob/23da3dfa79152648f3d38050ee147df47f41ce0a/Modules/IO/ImageBase/test/itkLargeImageWriteConvertReadTest.cxx) and [`itkLargeImageWriteReadTest`](https://github.com/InsightSoftwareConsortium/ITK/blob/23da3dfa79152648f3d38050ee147df47f41ce0a/Modules/IO/ImageBase/test/itkLargeImageWriteReadTest.cxx) are not being exercised as the corresponding `itk_add_test` command are not present in the relevant [CMakeLists.txt](
https://github.com/InsightSoftwareConsortium/ITK/blob/23da3dfa79152648f3d38050ee147df47f41ce0a/Modules/IO/ImageBase/test/CMakeLists.txt) file, despite the files being listed:
https://github.com/InsightSoftwareConsortium/ITK/blob/23da3dfa79152648f3d38050ee147df47f41ce0a/Modules/IO/ImageBase/test/CMakeLists.txt#L12
and
https://github.com/InsightSoftwareConsortium/ITK/blob/23da3dfa79152648f3d38050ee147df47f41ce0a/Modules/IO/ImageBase/test/CMakeLists.txt#L13

Thus, the corresponding executables are not created.

### Steps to Reproduce

1. Get ITK
2. Configure and build
3. Execute
```
ctest -V -R itkLargeImageWriteConvertReadTest -C Debug
```
and
```
ctest -V -R itkLargeImageWriteReadTest-C Debug
```

CTest will report the message:
```
No tests were found!!!
```

### Expected behavior

All listed tests should be exercised.

### Actual behavior

Tests are not being exercised.

### Reproducibility

100%.

### Versions

`master`.

### Environment

Any.

### Additional Information

None
