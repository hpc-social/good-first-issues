---
tags: Good-First-Issue,kind/bug
title: "podman events different than docker events"
html_url: "https://github.com/containers/podman/issues/14993"
user: joachimBurket
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


**Description**

<!--
Briefly describe the problem you are having in a few paragraphs.
-->

I'm not sure if it is Podman's goal to match Docker's outputs, but while trying to use Podman with a [tool](https://github.com/stepchowfun/docuum) designed with Docker CLI, I saw that the output of `podman events --format "{{json .}}"` doesn't contain the same fields as `docker events --format "{{json .}}"`, which prevents the tool to run.

**Steps to reproduce the issue:**

1. `podman events --format "{{json .}}"`

**Describe the results you received:**

```
# pull new image event ->
{"Name":"rust:alpine","Status":"pull","Time":"2022-07-19T21:26:10.143941717+02:00","Type":"image","Attributes":null}

# remove image event ->
{"ID":"3a83e7ec7491adfa83edde65f415fd133d3a47fd6be9b2b1843b46d3a188c4da","Name":"docker.io/library/rust:alpine","Status":"remove","Time":"2022-07-19T21:25:34.684610229+02:00","Type":"image","Attributes":null}
```

**Describe the results you expected:**

Same as  `docker events --format "{{json .}}"`:

```
# pull new image event ->
{"status":"pull","id":"rust:alpine","Type":"image","Action":"pull","Actor":{"ID":"rust:alpine","Attributes":{"name":" rust"}},"scope":"local","time":1658332113,"timeNano":1658332113524919324}

# remove image event ->
{"status":"untag","id":"sha256:3a83e7ec7491adfa83edde65f415fd133d3a47fd6be9b2b1843b46d3a188c4da","Type":"image","Action":"untag","Actor":{"ID":"sha256:3a83e7ec7491adfa83edde65f415fd133d3a47fd6be9b2b1843b46d3a188c4da","Attributes":{"name":"sha256:3a83e7ec7491adfa83edde65f415fd133d3a47fd6be9b2b1843b46d3a188c4da"}},"scope":"local","time":1658332211,"timeNano":1658332211177841258}
{"status":"delete","id":"sha256:3a83e7ec7491adfa83edde65f415fd133d3a47fd6be9b2b1843b46d3a188c4da","Type":"image","Action":"delete","Actor":{"ID":"sha256:3a83e7ec7491adfa83edde65f415fd133d3a47fd6be9b2b1843b46d3a188c4da","Attributes":{"name":"sha256:3a83e7ec7491adfa83edde65f415fd133d3a47fd6be9b2b1843b46d3a188c4da"}},"scope":"local","time":1658332211,"timeNano":1658332211345361391}
```

**Additional information you deem important (e.g. issue happens only occasionally):**

**Output of `podman version`:**

```
Client:       Podman Engine
Version:      4.1.1
API Version:  4.1.1
Go Version:   go1.18.3
Built:        Wed Jun 22 18:17:44 2022
OS/Arch:      linux/amd64
```

**Output of `podman info --debug`:**

```
host:
  arch: amd64
  buildahVersion: 1.26.1
  cgroupControllers:
  - cpu
  - io
  - memory
  - pids
  cgroupManager: systemd
  cgroupVersion: v2
  conmon:
    package: conmon-2.1.0-2.fc36.x86_64
    path: /usr/bin/conmon
    version: 'conmon version 2.1.0, commit: '
  cpuUtilization:
    idlePercent: 72.79
    systemPercent: 6.46
    userPercent: 20.75
  cpus: 4
  distribution:
    distribution: fedora
    variant: workstation
    version: "36"
  eventLogger: journald
  hostname: fedora
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
  kernel: 5.18.7-200.fc36.x86_64
  linkmode: dynamic
  logDriver: journald
  memFree: 355311616
  memTotal: 16457154560
  networkBackend: cni
  ociRuntime:
    name: crun
    package: crun-1.4.5-1.fc36.x86_64
    path: /usr/bin/crun
    version: |-
      crun version 1.4.5
      commit: c381048530aa750495cf502ddb7181f2ded5b400
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
    package: slirp4netns-1.2.0-0.2.beta.0.fc36.x86_64
    version: |-
      slirp4netns version 1.2.0-beta.0
      commit: 477db14a24ff1a3de3a705e51ca2c4c1fe3dda64
      libslirp: 4.6.1
      SLIRP_CONFIG_VERSION_MAX: 3
      libseccomp: 2.5.3
  swapFree: 8503521280
  swapTotal: 8589930496
  uptime: 192h 11m 59.93s (Approximately 8.00 days)
plugins:
  log:
  - k8s-file
  - none
  - passthrough
  - journald
  network:
  - bridge
  - macvlan
  - ipvlan
  volume:
  - local
registries:
  search:
  - registry.fedoraproject.org
  - registry.access.redhat.com
  - registry.centos.org
  - docker.io
store:
  configFile: /home/joachim/.config/containers/storage.conf
  containerStore:
    number: 0
    paused: 0
    running: 0
    stopped: 0
  graphDriverName: overlay
  graphOptions: {}
  graphRoot: /home/joachim/.local/share/containers/storage
  graphRootAllocated: 748592037888
  graphRootUsed: 121975619584
  graphStatus:
    Backing Filesystem: btrfs
    Native Overlay Diff: "true"
    Supports d_type: "true"
    Using metacopy: "false"
  imageCopyTmpDir: /var/tmp
  imageStore:
    number: 90
  runRoot: /run/user/1000/containers
  volumePath: /home/joachim/.local/share/containers/storage/volumes
version:
  APIVersion: 4.1.1
  Built: 1655914664
  BuiltTime: Wed Jun 22 18:17:44 2022
  GitCommit: ""
  GoVersion: go1.18.3
  Os: linux
  OsArch: linux/amd64
  Version: 4.1.1
```

**Package info (e.g. output of `rpm -q podman` or `apt list podman`):**

```
podman-4.1.1-2.fc36.x86_64
```

**Have you tested with the latest version of Podman and have you checked the Podman Troubleshooting Guide? (https://github.com/containers/podman/blob/main/troubleshooting.md)**


Yes

**Additional environment details (AWS, VirtualBox, physical, etc.):**

Physical. 

Docker --version: 

```
Docker version 20.10.12, build e91ed57
```
