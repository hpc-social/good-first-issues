---
tags: Good-First-Issue,kind/feature
title: "`podman manifest create` should support `--format`"
html_url: "https://github.com/containers/podman/issues/16603"
user: jlebon
repo: containers/podman
---

**Is this a BUG REPORT or FEATURE REQUEST? (leave only one on its own line)**

/kind feature

**Description**

In OCP-land, we need to deal with some clients that don't yet support OCI manifest lists. Because of this, we push them in v2s2 format. Our tooling needs to be able to know the final digests of the constituent images. We currently do this using `podman manifest inspect`. However, if we push in v2s2 format, the digests on the remote will unsurprisingly not match.

Right now, we work around this by doing a `skopeo inspect --raw` of the target repo right after pushing it to get the final digests, but ideally we wouldn't have to do that. The problem is that there's no way to create the manifest in v2s2 format right from the start.