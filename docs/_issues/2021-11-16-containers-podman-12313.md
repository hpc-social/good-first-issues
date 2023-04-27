---
tags: Good-First-Issue,kind/feature
title: "podman machine do not use a `tab` but instead `spaces` to list the VM machines"
html_url: "https://github.com/containers/podman/issues/12313"
user: cmoulliard
repo: containers/podman
---

**Is this a BUG REPORT or FEATURE REQUEST? (leave only one on its own line)**

/kind feature

**Description**

The format used to stdout the list of the podman machine do not use a `tab` but instead `spaces`.
The list of the machines displayed should respect the format defined and documented and add a tab between the columns result
```
podman machine list --format "{{.Name}}\t{{.VMType}}\t{{.Created}}\t{{.LastUp}}\t{{.CPUs}}\t{{.Memory}}\t{{.DiskSize}}" | awk -F '\t' '{ print $2 }'

podman machine list --format "{{.Name}}\t{{.VMType}}\t{{.Created}}\t{{.LastUp}}\t{{.CPUs}}\t{{.Memory}}\t{{.DiskSize}}" | awk -F '\t' '{ print $1 }'
macvm*      qemu        2 hours ago  About an hour ago  1           2.147GB     10.74GB

OR

podman machine list | head -n 2 | awk -F '\t' '{ print $2 }'


podman machine list | head -n 2 | awk -F '\t' '{ print $1 }'
NAME        VM TYPE     CREATED      LAST UP            CPUS        MEMORY      DISK SIZE
macvm*      qemu        2 hours ago  About an hour ago  1           2.147GB     10.74GB
```

**Additional information**

podman version: 3.4.2
OS: MacOS

