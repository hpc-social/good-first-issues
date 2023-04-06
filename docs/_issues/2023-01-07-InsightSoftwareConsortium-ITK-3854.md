---
tags: ,Good-first-issue,typeTesting
title: "Check initialization values in tests"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/3854"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description

For any given class, we should test that their ivars are initialized to the values in their corresponding declaration/class constructor. This would allow to detect and track changes/bugs related to a given initialization value.

### Steps to Reproduce

Prior to testing the Set/Get methods, check that all member variables have been initialized to the values in their corresponding declaration/class constructor files.

Some macros might be helpful (e.g. checking that a given array contains all zeros, or has a given length; checking that a string contains a zero-length, etc.), but the macro will need to be called manually for each member/value pair. 

### Expected behavior

All members are initialized to some default value, and the exact value is tested.

### Actual behavior

No testing is done for default initialization values.

### Reproducibility

100%.

### Versions

`master`.

### Environment

Any.

### Additional Information

None.