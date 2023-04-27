---
tags: Good-First-Issue,kind/bug,kube
title: "play kube does not expand env in command"
html_url: "https://github.com/containers/podman/issues/15983"
user: reavessm
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

Variables defined in the `env` section are not expanded in the `command`/`args` section.  According to [the k8s spec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.19/#container-v1-core), env vars should be expanded using the `$(VAR_NAME)` syntax.

**Steps to reproduce the issue:**

1. Define a file called `test.yaml` with the following contents:

```yaml
---
kind: Pod
apiVersion: v1
metadata:
  name: echo
  labels:
    app: echo
spec:
  containers:
    - name: test
      env:
        - key: FOO
          value: BAR
      image: docker.io/library/alpine:latest
      command:
        - /bin/sh
        - -c
        - echo
        - $(FOO)
```

2.  verify result by running `podman play kube test.yaml && podman logs -f echo-test`

**Describe the results you received:**

no output


**Describe the results you expected:**

"BAR" to be printed


**Additional information you deem important (e.g. issue happens only occasionally):**

I also tried printing `$(PATH)` instead of `$(FOO)` and there was still no output.

**Output of `podman version`:**

```
Client:       Podman Engine
Version:      4.2.0
API Version:  4.2.0
Go Version:   go1.18.4
Built:        Thu Aug 11 10:42:17 2022
OS/Arch:      linux/amd64
```

**Output of `podman info`:**

```
host:
  arch: amd64
  buildahVersion: 1.27.0
  cgroupControllers:
  - cpu
  - io
  - memory
  - pids
  cgroupManager: systemd
  cgroupVersion: v2
  conmon:
    package: conmon-2.1.4-2.fc36.x86_64
    path: /usr/bin/conmon
    version: 'conmon version 2.1.4, commit: '
  cpuUtilization:
    idlePercent: 81.86
    systemPercent: 4.71
    userPercent: 13.43
  cpus: 8
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
  kernel: 5.19.11-200.fc36.x86_64
  linkmode: dynamic
  logDriver: journald
  memFree: 2847203328
  memTotal: 33404751872
  networkBackend: netavark
  ociRuntime:
    name: crun
    package: crun-1.6-2.fc36.x86_64
    path: /usr/bin/crun
    version: |-
      crun version 1.6
      commit: 18cf2efbb8feb2b2f20e316520e0fd0b6c41ef4d
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
  swapFree: 8548249600
  swapTotal: 8589930496
  uptime: 5h 48m 24.00s (Approximately 0.21 days)
plugins:
  authorization: null
  log:
  - k8s-file
  - none
  - passthrough
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
  configFile: /home/sreaves/.config/containers/storage.conf
  containerStore:
    number: 2
    paused: 0
    running: 1
    stopped: 1
  graphDriverName: overlay
  graphOptions: {}
  graphRoot: /home/sreaves/.local/share/containers/storage
  graphRootAllocated: 254339448832
  graphRootUsed: 135085797376
  graphStatus:
    Backing Filesystem: btrfs
    Native Overlay Diff: "true"
    Supports d_type: "true"
    Using metacopy: "false"
  imageCopyTmpDir: /var/tmp
  imageStore:
    number: 45
  runRoot: /run/user/1000/containers
  volumePath: /home/sreaves/.local/share/containers/storage/volumes
version:
  APIVersion: 4.2.0
  Built: 1660228937
  BuiltTime: Thu Aug 11 10:42:17 2022
  GitCommit: ""
  GoVersion: go1.18.4
  Os: linux
  OsArch: linux/amd64
  Version: 4.2.0
```

**Package info (e.g. output of `rpm -q podman` or `apt list podman`):**

```
podman-4.2.0-2.fc36.x86_64
```

**Have you tested with the latest version of Podman and have you checked the Podman Troubleshooting Guide? (https://github.com/containers/podman/blob/main/troubleshooting.md)**

I have not tested with latest but I have read the troubleshooting guide.

**Additional environment details (AWS, VirtualBox, physical, etc.):**

Physical F36 Workstation
