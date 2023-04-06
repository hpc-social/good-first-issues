---
tags: ,Good-First-Issue,HTTP-API,documentation,kind/bug,stale-issue
title: "Mismatch between documentation and REST API"
html_url: "https://github.com/containers/podman/issues/15376"
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

When looking at the REST API documentation
https://docs.podman.io/en/latest/_static/api.html#tag/system-(compat)/operation/SystemInfo

In top right corner I see `GET /info`
and I can do a curl request like

```
curl --unix-socket /Users/benoitf/.local/share/containers/podman/machine/podman-machine-default/podman.sock 'http:///d/info'
```
it works

now if I go to the 'libpod info' page https://docs.podman.io/en/latest/_static/api.html#tag/system/operation/SystemInfoLibpod

in top right corner it says `GET /libpod/info`

but if I do a curl on `/libpod/info` as written it fails
```
curl --unix-socket /Users/benoitf/.local/share/containers/podman/machine/podman-machine-default/podman.sock 'http:///d/libpod/info'
```
I have `Not found` error

using `v4.2.0` prefix it works

```
curl --unix-socket /Users/benoitf/.local/share/containers/podman/machine/podman-machine-default/podman.sock 'http:///d/v4.2.0/libpod/info'
```

Funny thing, I can use random numbers like `v5.0.0` and it's still working but without prefix it doesn't work
```
curl --unix-socket /Users/benoitf/.local/share/containers/podman/machine/podman-machine-default/podman.sock 'http:///d/v5.0.0/libpod/info'
```

**Describe the results you received:**

not working without prefixing /libpod/ with a version scheme

**Describe the results you expected:**

working without prefixing with a version (expect to have alias to the latest API)

**Additional information you deem important (e.g. issue happens only occasionally):**

**Output of `podman version`:**

```
macOS with brew 4.2.0 
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
