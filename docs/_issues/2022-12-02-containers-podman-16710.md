---
tags: Good-First-Issue,kind/feature
title: "Consider adding machine provider prefix to ssh keys"
html_url: "https://github.com/containers/podman/issues/16710"
user: arixmkii
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

For machine settings they are stored under provider directory. E.g. for QEMU it will have `/qemu/` part.
```
podman machine inspect | grep .json
               "Path": "~/.config/containers/podman/machine/qemu/podman-machine-default.json"
```

But ssh keys are named with only machine name. This will become an issue if multiple providers are available for the same platform: like Applehv and QEMU for MacOS or QEMU and WSL2 for Windows.

Even if there will be different binaries/builds to support only single provider per build, this could cause issues when backup restore happens as it might overwrite keys (the data), which actually belongs to another provider and should be isolated.

Adding provider prefix would not make it 100% error prone, but will mitigate at least some cases. And it will also allow to use same named machines for different providers (like calling `podman machine init` with defaults for either of them w/o chances to break something for another provider).

Example of this collision is described in https://github.com/containers/podman/issues/13006#issuecomment-1227302679

Preventing such name collision is difficult as every provider will maintain own set of data (list of machines and their states) w/o knowing about other providers.

<!--
Briefly describe the problem you are having in a few paragraphs.
-->

**Steps to reproduce the issue:**

1. `podman machine init`

2. `ls ~/.ssh | grep podman`

**Describe the results you received:**

`podman-machine-default` and `podman-machine-default.pub` are created.

**Describe the results you expected:**

`qemu-podman-machine-default` and `qemu-podman-machine-default.pub`

**Additional information you deem important (e.g. issue happens only occasionally):**

**Output of `podman version`:**

```
Built from latest main
```

**Output of `podman info`:**

```
Skipped.
```

**Package info (e.g. output of `rpm -q podman` or `apt list podman` or `brew info podman`):**

```
Skipped.
```

**Have you tested with the latest version of Podman and have you checked [the Podman Troubleshooting Guide](https://github.com/containers/podman/blob/main/troubleshooting.md)?**


Yes

**Additional environment details (AWS, VirtualBox, physical, etc.):**

Podman machine on darwin