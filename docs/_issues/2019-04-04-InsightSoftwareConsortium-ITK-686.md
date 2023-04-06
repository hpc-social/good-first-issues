---
tags: ,Good-first-issue,typeInfrastructure
title: "Make `UpdateRequiredITKVersionInFiles.sh` fetch files automatically"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/686"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description

[UpdateRequiredITKVersionInRemoteModules.sh](https://github.com/InsightSoftwareConsortium/ITK/blob/master/Utilities/Maintenance/UpdateRequiredITKVersionInRemoteModules.sh) requires the remotes `setup.py` and `azure-pipelines.yml` files as input arguments. Making the script fetch those files automatically would be desirable.

### Impact analysis

This would allow for a more efficient use of the script, a wider adoption of the script, and would allow to save time.

### Expected behavior

Make the script fetch the `setup.py` and `azure-pipelines.yml` files automatically given the remote module name.

This would assume that both files are always at the same location (which is not the case currently for the former - rather than considering multiple paths, they should be made dwell in the same location according to the [ITKModuleTemplate](https://github.com/InsightSoftwareConsortium/ITKModuleTemplate) guidelines).

### Actual behavior

The path to the `setup.py` and `azure-pipelines.yml`  has to be provided to the script.

### Versions

`master`.

### Environment

Any.

### Additional Information

Discussion: https://github.com/InsightSoftwareConsortium/ITK/pull/641#issuecomment-477397311
Some inspiration could be taken from here (especially concerning the part of configuring, cloning, and looping over the remotes):
https://github.com/InsightSoftwareConsortium/ITK/blob/8fdb4542f2203fddee463a02cbc14587ade2375c/Utilities/Maintenance/UpdateRemoteModules.sh#L25