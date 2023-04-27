---
tags: Good-First-Issue,kind/feature
title: "Support special IP designator `host-gateway` in `--add-host`."
html_url: "https://github.com/containers/podman/issues/14390"
user: willmtemple
repo: containers/podman
---

**Is this a BUG REPORT or FEATURE REQUEST? (leave only one on its own line)**

/kind feature

**Description**

<!--
Briefly describe the problem you are having in a few paragraphs.
-->

Related: https://github.com/containers/podman/issues/8466

Podman doesn't support `host-gateway` as a special IP designator when creating a container. Instead it creates an automatic mapping from `host.containers.internal` to the host NIC's IP address, but unfortunately that doesn't really help in situations involving scripts that call `docker`, where the host has the podman `docker` CLI shim installed.

This is one of those argument configurations (`--add-host host.docker.internal:host-gateway`) that floats around on the web as a solution for the problem of "talking to the host" when using docker, so it ends up integrated into a fair amount of tools that call the docker CLI. It'd be nice if podman could support this argument well for compatibility.

**Steps to reproduce the issue:**

1. Try to launch a container with a `host-gateway` mapping: `podman run --rm --add-host foobar:host-gateway fedora`

**Describe the results you received:**

```
$ podman run --rm --add-host foobar:host-gateway fedora
Error: invalid IP address in add-host: "host-gateway"
```

**Describe the results you expected:**

As with moby-engine:

```
$ docker run --add-host foobar:host-gateway -it fedora
[root@87ec49b55693 /]# cat /etc/hosts
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.17.0.1      foobar
172.17.0.2      87ec49b55693
```

I'll spare you all the additional info in the issue template, since this is just a feature request.

**Notes:**

Unless `ContainerConfig.HostAdd` is used in other places, I think this can be implemented by special-casing `host-gateway` as an IP string in `ValidateExtraHost` and then in libpod/container_internal_linux `Container#createHosts` by simply mapping over the extra hosts and replacing any that have `host-gateway` as their IP string with the selected host IP from libnetwork.