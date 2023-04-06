---
tags: ,Good-First-Issue,kind/feature,kube,podman-desktop
title: "RFE: Add tracking/monitoring/events of what will/is currently performed by `kube play` command"
html_url: "https://github.com/containers/podman/issues/15902"
user: benoitf
repo: containers/podman
---

<!--
---------------------------------------------------
BUG REPORT INFORMATION
---------------------------------------------------
Use the commands below to provide key information from your environment:
You do NOT have to include this information if this is a FEATURE REQUEST

**NOTE** A large number of issues reported against Podman are often found to already be fixed
in more current versions of the project.  Before reporting an issue, please verify the
version you are running with `podman version` and compare it to the latest release
documented on the top of Podman's [README.md](../README.md).  If they differ, please
update your version of Podman to the latest possible and retry your command before creating
an issue.

Also, there is a running list of known issues in the [Podman Troubleshooting Guide](https://github.com/containers/podman/blob/main/troubleshooting.md),
please reference that page before opening a new issue.

If you are filing a bug against `podman build`, please instead file a bug
against Buildah (https://github.com/containers/buildah/issues). Podman build
executes Buildah to perform container builds, and as such the Buildah
maintainers are best equipped to handle these bugs.
-->

**Is this a BUG REPORT or FEATURE REQUEST? (leave only one on its own line)**


/kind feature

**Description**

Today, we have the nice `podman kube play` command and REST API that is accepting a yaml file.

The issue that UI client are facing, is the lack of 'progress/report' of what the command will do or is doing.
For example you may wait a couple of minutes before having the command succeeding and it's only returning a status at the end but we don't have progress.


**Describe the results you expected:**

Several ways are possible.
- we could have extra information in the events of pods/images/containers being created/pulled/etc to know that these objects are part of a given yaml that is being provided. (for example if the path to the yaml file is in the events)
- we could have a stream specific to the play kube REST API that could also provide the operations being performed

From UI POV, it will be great if we know in advance the number of items that will be performed, so we can provide a better progress system.



**Additional information you deem important (e.g. issue happens only occasionally):**

**Output of `podman version`:**

```
(paste your output here)
```

**Output of `podman info`:**

```
(paste your output here)
```

**Package info (e.g. output of `rpm -q podman` or `apt list podman`):**

```
(paste your output here)
```

**Have you tested with the latest version of Podman and have you checked the Podman Troubleshooting Guide? (https://github.com/containers/podman/blob/main/troubleshooting.md)**


Yes/No

**Additional environment details (AWS, VirtualBox, physical, etc.):**
