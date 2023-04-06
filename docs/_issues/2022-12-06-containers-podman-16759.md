---
tags: ,Good-First-Issue,kind/bug
title: "Define better error message for container name conflicts with \"external\" storage"
html_url: "https://github.com/containers/podman/issues/16759"
user: baude
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

/kind bug

/kind feature

**Description**

When you have a database failure or the database gets nuked, containers may still "exist" in the filesystem, also referred to as "external storage".  When attempting to recreate a container with the same name as a container in external storage, you receive a poor error message,
<!--
Briefly describe the problem you are having in a few paragraphs.
-->

**Steps to reproduce the issue:**

1. podman create --name foobar alpine top

2. rm /var/lib/containers/storage/bolt_state.db

3. podman create --name foobar alpine top

**Describe the results you received:**
sudo podman create --name foobar alpine top
Error: creating container storage: the container name "container1" is already in use by e77786c096e083b258bad2e196255f7dc1a2859cfb9dd35436648e1541bdce23. You have to remove that container to be able to reuse that name: that name is already in use

**Describe the results you expected:**

The error message should say it is in external storage.  It should also suggest the use of --replace

**Additional information you deem important (e.g. issue happens only occasionally):**

**Output of `podman version`:**

```
(paste your output here)
```

**Output of `podman info`:**

```
Client:       Podman Engine
Version:      4.4.0-dev
API Version:  4.4.0-dev
Go Version:   go1.19.3
Git Commit:   c942f7788707ee565b657d8a5c1fb56d7dec0347-dirty
Built:        Mon Dec  5 12:52:27 2022
OS/Arch:      linux/amd64

```

**Package info (e.g. output of `rpm -q podman` or `apt list podman` or `brew info podman`):**

```
NA, upstream
```

**Have you tested with the latest version of Podman and have you checked [the Podman Troubleshooting Guide](https://github.com/containers/podman/blob/main/troubleshooting.md)?**

Yes
Yes/No

**Additional environment details (AWS, VirtualBox, physical, etc.):**
