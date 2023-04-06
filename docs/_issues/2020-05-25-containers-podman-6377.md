---
tags: ,Good-First-Issue,kind/feature,volunteers-wanted
title: "can not use fluentd log driver"
html_url: "https://github.com/containers/podman/issues/6377"
user: Hendrik-H
repo: containers/podman
---

/kind bug

**Description**
According to the bash completion script in https://github.com/containers/libpod/blob/master/completions/bash/podman it seems like podman is supporting several log drivers, including fluentd. However when starting a container with the fluentd log driver `fluentd` is stated to be an invalid argument.

**Steps to reproduce the issue:**

1. podman run --name nginx --rm -it --log-driver fluentd nginx

**Describe the results you received:**
```Error: error running container create option: invalid log driver: invalid argument```

**Describe the results you expected:**
That logging via the fluentd log driver works just like it does for Docker.

**Additional information you deem important (e.g. issue happens only occasionally):**

**Output of `podman version`:**

```
Version:            1.9.2
RemoteAPI Version:  1
Go Version:         go1.13.10
OS/Arch:            linux/amd64
```

**Output of `podman info --debug`:**

```
debug:
  compiler: gc
  gitCommit: ""
  goVersion: go1.13.10
  podmanVersion: 1.9.2
host:
  arch: amd64
  buildahVersion: 1.14.8
  cgroupVersion: v2
  conmon:
    package: conmon-2.0.16-2.fc31.x86_64
    path: /usr/bin/conmon
    version: 'conmon version 2.0.16, commit: aec991fec16dc45935de184f2ea06a6ffca200a0'
  cpus: 12
  distribution:
    distribution: fedora
    version: "31"
  eventLogger: file
  hostname: p52
  idMappings:
    gidmap: null
    uidmap: null
  kernel: 5.6.13-200.fc31.x86_64
  memFree: 10336419840
  memTotal: 33334947840
  ociRuntime:
    name: crun
    package: crun-0.13-2.fc31.x86_64
    path: /usr/bin/crun
    version: |-
      crun version 0.13
      commit: e79e4de4ac16da0ce48777afb72c6241de870525
      spec: 1.0.0
      +SYSTEMD +SELINUX +APPARMOR +CAP +SECCOMP +EBPF +YAJL
  os: linux
  rootless: false
  slirp4netns:
    executable: ""
    package: ""
    version: ""
  swapFree: 16768823296
  swapTotal: 16768823296
  uptime: 46h 2m 29.96s (Approximately 1.92 days)
registries:
  search:
  - registry.fedoraproject.org
  - registry.access.redhat.com
  - registry.centos.org
  - docker.io
store:
  configFile: /etc/containers/storage.conf
  containerStore:
    number: 0
    paused: 0
    running: 0
    stopped: 0
  graphDriverName: overlay
  graphOptions:
    overlay.mountopt: nodev,metacopy=on
  graphRoot: /var/lib/containers/storage
  graphStatus:
    Backing Filesystem: extfs
    Native Overlay Diff: "false"
    Supports d_type: "true"
    Using metacopy: "true"
  imageStore:
    number: 2
  runRoot: /var/run/containers/storage
  volumePath: /var/lib/containers/storage/volumes
```

