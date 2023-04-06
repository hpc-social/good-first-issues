---
tags: ,Good-first-issue,areaRemotes,typeInfrastructure
title: "Improve ApplyScriptToRemotes.sh script's robustness"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/1024"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description


The [ApplyScriptToRemotes](https://github.com/InsightSoftwareConsortium/ITK/blob/master/Utilities/Maintenance/ApplyScriptToRemotes.sh) script applies a script to all remote modules whose build status reports a successful build.

There are a number of aspects -many of them were already mentioned in PR #781- that could be improved to make the script more robust.

- May be the [`UpdateRemoteModules`](https://github.com/InsightSoftwareConsortium/ITK/blob/master/Utilities/Maintenance/UpdateRemoteModules.sh) should be called before this script gets called to **ensure that the cloned versions are the latest ones**, and thus avoid unnecessary changes to scripts and unnecessary branch pushing.

- The **script pushes to the remote even if no changes have been applied** by the script (e.g. the changes that the script applies have already been applied on the remote or do not apply to the remote at issue). This should be avoided.

- The philosophy behind the script does not require to build ITK with the corresponding remote modules, and thus **completing all CMake configuration steps is not necessary**. So may be we should just extract (if that is possible) the relevant parts from the `CMakeLists.txt` to clone the remotes in the ITK source tree. Or propose an alternative `CMakeLists.txt` that is only used by this script to do so. If we should build the project whenever such scripts are applied (e.g. we want the user to build the project locally to see if the script introduced build failures), then adding the commands to make the script build the project would be necessary. Building locally is not necessary: CI builds faster and its them who finally determine whether the branches will be merged. Although on the other hand, in this case all remotes' CIs should be checked individually.

- **Only remotes whose build status is successful will be updated. This may make the unsuccessful ones to lag progressively behind**. We may want to avoid this.

- The **full path of the script** to be applied must be provided. Otherwise, we could assume that only scripts that dwell in `Utilities` will be applied, since they anyways will be worthwhile maintaining there for the records and for the sake of our philosophy. The **script could also get the absolute path given any path**. Either behavior should be documented.

- The **commit message must be provided explicitly**. Many of the [ITKv5 preparation](https://github.com/InsightSoftwareConsortium/ITK/tree/master/Utilities/ITKv5Preparation) scripts do it all at once: do the changes, add them and commit with a message contained in the script itself.

We should may be **consider whether we prefer that the add and commit steps will generally be contained in the script that is applied**.

If it is decided that best is to provide the commit message as a command line argument, **multi-line (i.e. commit subject + body) commit messages should be tested**, and formatting instructions be provided.

- The script **does a direct push to each remote repository, and thus assumes the user has a fork**. A message or warning could be added at the beginning. Otherwise, we could think of checking this when configuring the remotes, and taking the necessary actions if a remote is not forked (whether to display a message, to stop the process, etc.).

- Linked to the above, no **upstream** remote is configured. As we do usually with ITK, **may be it would more orthodox** to configure the **origin** and **upstream**, **assume the user has all remotes forked**, and **push to their fork** (I have not tested push step).

- If the build directory exists, the `mkdir` prints an error message. However, the process continues and writes to the same location. We should think of the most appropriate strategy (building in a different location, warning the user, etc.).

- The case where **a remote has already been cloned, has local untracked or uncommitted changes, etc.** should be considered.

- The script assumes that a **local branch with the same name as the one provided as the feature branch does not exist**. If such event happens, we should think of the most appropriate strategy.

- The script assumes that a **remote branch with the same name as the one provided as the feature branch does not exist**. If such event happens, we should think of the most appropriate strategy.

- **Remote modules that are checked out are not deleted from the ITK source tree**. If they should be, we should handle the case where some remotes had already been cloned and had untracked, uncommitted, local branches, etc.

- When the script does not modify any files in a module (e.g. a contributor applied the changes to a given module before the script was applied), we should tell the user that the module is up to date. May some sort of final report should be displayed, instead of printing messages at each iteration of the loop over the remotes.

Many of the branch collision cases are covered by @fbudin69500 's [Slicer 3D extensions script](https://github.com/fbudin69500/NIRALSystemScripts/blob/master/UpdateSlicerExtensions.script). So it could be of help.

Other maintenance scripts, such as [UpdateRequiredITKVersionInRemoteModules.sh](https://github.com/InsightSoftwareConsortium/ITK/blob/master/Utilities/Maintenance/UpdateRequiredITKVersionInRemoteModules.sh), and [UpdateRemoteModules.sh](https://github.com/InsightSoftwareConsortium/ITK/blob/master/Utilities/Maintenance/UpdateRemoteModules.sh) may benefit of these improvements.

### Impact analysis

Although the current script already saves a lot of manual work, increasing its robustness would ease the task of maintenance of remote modules, which is already time-consuming.
 
### Expected behavior

The script should run without issues and be robust to the above situations.

### Actual behavior

The script shows error messages, does not behave as expected or pushes unnecessary branches.

### Versions

`master`

### Environment

Any.

### Additional Information

None.