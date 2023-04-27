---
tags: Good-first-issue,typeInfrastructure
title: "GPU modules are listed as available even if `ITK_USE_GPU` is `OFF`"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/415"
user: fbudin69500
repo: InsightSoftwareConsortium/ITK
---

### Description

ITK GPU modules such as `ITKGPUCommon` are listed in `ITK_MODULES_ENABLED` in `ITKConfig.cmake` even if `ITK_USE_GPU` is set to `OFF`.

### Steps to Reproduce

1. Configure ITK build tree with default values (`ITK_USE_GPU` is OFF by default).
2. Open `ITKConfig.cmake` that is generated in build folder
3. Look at content of `ITK_MODULES_ENABLED` and value of `ITK_USE_GPU`.

### Expected behavior

The GPU modules should only be listed as enabled if `ITK_USE_GPU` is enabled.

### Actual behavior

GPU modules are listed in `ITK_MODULES_ENABLED` even if `ITK_USE_GPU` is `OFF`.

### Reproducibility

All the time.

### Versions

I tested this on ITK v5.0beta3 but I expect this to happen on all ITK versions prior to that.

### Environment

Tested on Ubuntu 18.04 but should happen on all systems.

### Additional Information

Looking at the CMake code, it seems that `ITK_USE_GPU` CMake variable is only used to deactivate part of the GPU modules, not fully deactivate them. 

Maybe someone could contribute a patch so that the GPU modules are not listed as enabled if `ITK_USE_GPU` is OFF. I see several ways this could be fixed:
1) `ITK_GPU` modules should be excluded from the default modules (`EXCLUDE_FROM_DEFAULT`).
2) Maybe the CMake variable `ITK_USE_GPU` could be used to activate or deactivate `ITKGPUCommon`, which should be sufficient to deactivate all the other GPU modules which I expect to require this main GPU module (I have not verified this statement).
3) There is currently no mechanism in the build system of ITK to require a CMake variable value to activate modules.  One could envision the addition of such a mechanism. 
4) A possible simple solution would be to update the individual CMake code of all these GPU modules to only activate them if `ITK_USE_GPU` is ON instead of only removing part of each module based on the value of `ITK_USE_GPU`. 
