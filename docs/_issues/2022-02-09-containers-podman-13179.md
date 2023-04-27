---
tags: Good-First-Issue,HTTP-API,kind/bug,volunteers-wanted
title: "API: `PodListLibpod` returns error when deleting pods at the same time"
html_url: "https://github.com/containers/podman/issues/13179"
user: arctic-alpaca
repo: containers/podman
---

**Is this a BUG REPORT or FEATURE REQUEST? (leave only one on its own line)**

/kind bug


**Description**

I'm running multiple test of an application using the podman REST API in parallel. The tests create and delete multiple pods/containers/volumes (all with distinct names) and list all pods. The tests listing all pods fail with the error: `no pod with ID [...] found in database`. Running the list tests separate from other tests shows no issues. In the discussion in the podman discord it was mentioned that checks for similar behavior are already present when listing containers.

**Steps to reproduce the issue:**

1. Create and delete multiple pods (via API)

2. At the same time, query the `PodListLibpod` endpoint


**Describe the results you received:**

`no pod with ID [...] found in database`

**Describe the results you expected:**
A list of all currently present pods.


**Additional information you deem important (e.g. issue happens only occasionally):**
Issue only happens when running in parallel.

**Output of `podman version`:**

```
Version:      3.4.4
API Version:  3.4.4
Go Version:   go1.16.8
Built:        Wed Dec  8 22:45:07 2021
OS/Arch:      linux/amd64
```

**Output of `podman info --debug`:**

```
host:
  arch: amd64
  buildahVersion: 1.23.1
  cgroupControllers:
  - cpu
  - io
  - memory
  - pids
  cgroupManager: systemd
  cgroupVersion: v2
  conmon:
    package: conmon-2.1.0-2.fc35.x86_64
    path: /usr/bin/conmon
    version: 'conmon version 2.1.0, commit: '
  cpus: 12
  distribution:
    distribution: fedora
    variant: kde
    version: "35"
  eventLogger: journald
  hostname: arctic-alpaca-Desktop
  idMappings:
    gidmap:
    - container_id: 0
      host_id: 1000
      size: 1
    - container_id: 1
      host_id: 100000
      size: 65536
    uidmap:
    - container_id: 0
      host_id: 1000
      size: 1
    - container_id: 1
      host_id: 100000
      size: 65536
  kernel: 5.16.5-200.fc35.x86_64
  linkmode: dynamic
  logDriver: journald
  memFree: 1098022912
  memTotal: 16689455104
  ociRuntime:
    name: crun
    package: crun-1.4.2-1.fc35.x86_64
    path: /usr/bin/crun
    version: |-
      crun version 1.4.2
      commit: f6fbc8f840df1a414f31a60953ae514fa497c748
      spec: 1.0.0
      +SYSTEMD +SELINUX +APPARMOR +CAP +SECCOMP +EBPF +CRIU +YAJL
  os: linux
  remoteSocket:
    path: /run/user/1000/podman/podman.sock
  security:
    apparmorEnabled: false
    capabilities: CAP_CHOWN,CAP_DAC_OVERRIDE,CAP_FOWNER,CAP_FSETID,CAP_KILL,CAP_NET_BIND_SERVICE,CAP_SETFCAP,CAP_SETGID,CAP_SETPCAP,CAP_SETUID,CAP_SYS_CHROOT
    rootless: true
    seccompEnabled: true
    seccompProfilePath: /usr/share/containers/seccomp.json
    selinuxEnabled: true
  serviceIsRemote: false
  slirp4netns:
    executable: /usr/bin/slirp4netns
    package: slirp4netns-1.1.12-2.fc35.x86_64
    version: |-
      slirp4netns version 1.1.12
      commit: 7a104a101aa3278a2152351a082a6df71f57c9a3
      libslirp: 4.6.1
      SLIRP_CONFIG_VERSION_MAX: 3
      libseccomp: 2.5.3
  swapFree: 8589930496
  swapTotal: 8589930496
  uptime: 1h 22m 24.36s (Approximately 0.04 days)
plugins:
  log:
  - k8s-file
  - none
  - journald
  network:
  - bridge
  - macvlan
  volume:
  - local
registries:
  search:
  - registry.fedoraproject.org
  - registry.access.redhat.com
  - docker.io
  - quay.io
store:
  configFile: /home/arctic-alpaca/.config/containers/storage.conf
  containerStore:
    number: 15
    paused: 0
    running: 4
    stopped: 11
  graphDriverName: overlay
  graphOptions: {}
  graphRoot: /home/arctic-alpaca/.local/share/containers/storage
  graphStatus:
    Backing Filesystem: btrfs
    Native Overlay Diff: "true"
    Supports d_type: "true"
    Using metacopy: "false"
  imageStore:
    number: 11
  runRoot: /run/user/1000/containers
  volumePath: /home/arctic-alpaca/.local/share/containers/storage/volumes
version:
  APIVersion: 3.4.4
  Built: 1638999907
  BuiltTime: Wed Dec  8 22:45:07 2021
  GitCommit: ""
  GoVersion: go1.16.8
  OsArch: linux/amd64
  Version: 3.4.4
```

**Package info (e.g. output of `rpm -q podman` or `apt list podman`):**

```
podman-3.4.4-1.fc35.x86_64
```

**Have you tested with the latest version of Podman and have you checked the Podman Troubleshooting Guide? (https://github.com/containers/podman/blob/main/troubleshooting.md)**

No

**Additional environment details (AWS, VirtualBox, physical, etc.):**
