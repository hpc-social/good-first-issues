---
tags: Good-First-Issue,kind/bug
title: "json-file log-driver not producing valid json"
html_url: "https://github.com/containers/podman/issues/16317"
user: andrin55
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

Using "--log-driver=json-file" does not produce valid json output.

**Steps to reproduce the issue:**

1. Run a container with "--log-driver=json-file" 

2. Check log output (default path: /var/lib/containers/storage/overlay-containers/ID/userdata/ctr.log)

**Describe the results you received:**
Log output with podman-4.1.1-1.el9_0.x86_64 (podman run --rm --name test --log-driver=json-file nginx):
```
# cat /var/lib/containers/storage/overlay-containers/e0a3b432faa3dfaa3a9c246cfd3174019134e780640d974777cfe59f4a572c74/userdata/ctr.log
2022-10-27T10:22:43.572624525+02:00 stdout F /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
2022-10-27T10:22:43.572624525+02:00 stdout F /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
2022-10-27T10:22:43.573025248+02:00 stdout F /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
2022-10-27T10:22:43.577819858+02:00 stdout F 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
2022-10-27T10:22:43.584440662+02:00 stdout F 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
2022-10-27T10:22:43.584712901+02:00 stdout F /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
2022-10-27T10:22:43.587296664+02:00 stdout F /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
2022-10-27T10:22:43.588653045+02:00 stdout F /docker-entrypoint.sh: Configuration complete; ready for start up
2022-10-27T10:22:43.593931067+02:00 stderr F 2022/10/27 08:22:43 [notice] 1#1: using the "epoll" event method
2022-10-27T10:22:43.594067138+02:00 stderr F 2022/10/27 08:22:43 [notice] 1#1: nginx/1.23.2
2022-10-27T10:22:43.594229290+02:00 stderr F 2022/10/27 08:22:43 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6)
2022-10-27T10:22:43.594297605+02:00 stderr F 2022/10/27 08:22:43 [notice] 1#1: OS: Linux 5.14.0-70.26.1.el9_0.x86_64
2022-10-27T10:22:43.594357664+02:00 stderr F 2022/10/27 08:22:43 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2022-10-27T10:22:43.594512869+02:00 stderr F 2022/10/27 08:22:43 [notice] 1#1: start worker processes
2022-10-27T10:22:43.594735144+02:00 stderr F 2022/10/27 08:22:43 [notice] 1#1: start worker process 24
2022-10-27T10:22:43.594958416+02:00 stderr F 2022/10/27 08:22:43 [notice] 1#1: start worker process 25
```

**Describe the results you expected:**
Log output with docker-ce-20.10.21-3.el8.x86_64 (docker run --rm --name test --log-driver=json-file nginx):
```
# cat /var/lib/docker/containers/d491b7a02ada92f9fff01dfd3eda1bddd4a5229dac363aacd3baac709e584fda/d491b7a02ada92f9fff01dfd3eda1bddd4a5229dac363aacd3baac709e584fda-json.log
{"log":"/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration\n","stream":"stdout","time":"2022-10-27T08:28:36.857465821Z"}
{"log":"/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/\n","stream":"stdout","time":"2022-10-27T08:28:36.857510671Z"}
{"log":"/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh\n","stream":"stdout","time":"2022-10-27T08:28:36.857514736Z"}
{"log":"10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf\n","stream":"stdout","time":"2022-10-27T08:28:36.869718113Z"}
{"log":"10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf\n","stream":"stdout","time":"2022-10-27T08:28:36.892047308Z"}
{"log":"/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh\n","stream":"stdout","time":"2022-10-27T08:28:36.892242103Z"}
{"log":"/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh\n","stream":"stdout","time":"2022-10-27T08:28:36.895829393Z"}
{"log":"/docker-entrypoint.sh: Configuration complete; ready for start up\n","stream":"stdout","time":"2022-10-27T08:28:36.8976303Z"}
{"log":"2022/10/27 08:28:36 [notice] 1#1: using the \"epoll\" event method\n","stream":"stderr","time":"2022-10-27T08:28:36.907738495Z"}
{"log":"2022/10/27 08:28:36 [notice] 1#1: nginx/1.23.1\n","stream":"stderr","time":"2022-10-27T08:28:36.90776666Z"}
{"log":"2022/10/27 08:28:36 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6) \n","stream":"stderr","time":"2022-10-27T08:28:36.907769848Z"}
{"log":"2022/10/27 08:28:36 [notice] 1#1: OS: Linux 4.18.0-372.26.1.el8_6.x86_64\n","stream":"stderr","time":"2022-10-27T08:28:36.907772136Z"}
{"log":"2022/10/27 08:28:36 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576\n","stream":"stderr","time":"2022-10-27T08:28:36.907774285Z"}
{"log":"2022/10/27 08:28:36 [notice] 1#1: start worker processes\n","stream":"stderr","time":"2022-10-27T08:28:36.90898142Z"}
{"log":"2022/10/27 08:28:36 [notice] 1#1: start worker process 30\n","stream":"stderr","time":"2022-10-27T08:28:36.909330305Z"}
{"log":"2022/10/27 08:28:36 [notice] 1#1: start worker process 31\n","stream":"stderr","time":"2022-10-27T08:28:36.909532236Z"}
```

**Additional information you deem important (e.g. issue happens only occasionally):**

**Output of `podman version`:**

```
Client:       Podman Engine
Version:      4.1.1
API Version:  4.1.1
Go Version:   go1.17.12
Built:        Wed Jul 27 16:26:10 2022
OS/Arch:      linux/amd64
```

**Output of `podman info`:**

```
host:
  arch: amd64
  buildahVersion: 1.26.2
  cgroupControllers:
  - cpuset
  - cpu
  - io
  - memory
  - hugetlb
  - pids
  - rdma
  - misc
  cgroupManager: systemd
  cgroupVersion: v2
  conmon:
    package: conmon-2.1.2-2.el9_0.x86_64
    path: /usr/bin/conmon
    version: 'conmon version 2.1.2, commit: 1ed53517f446a779f9d0edafe090ce821a41e255'
  cpuUtilization:
    idlePercent: 93.75
    systemPercent: 0.6
    userPercent: 5.64
  cpus: 2
  distribution:
    distribution: '"rhel"'
    version: "9.0"
  eventLogger: journald
  hostname: localhost
  idMappings:
    gidmap: null
    uidmap: null
  kernel: 5.14.0-70.26.1.el9_0.x86_64
  linkmode: dynamic
  logDriver: journald
  memFree: 764809216
  memTotal: 3775676416
  networkBackend: netavark
  ociRuntime:
    name: crun
    package: crun-1.4.5-2.el9_0.x86_64
    path: /usr/bin/crun
    version: |-
      crun version 1.4.5
      commit: c381048530aa750495cf502ddb7181f2ded5b400
      spec: 1.0.0
      +SYSTEMD +SELINUX +APPARMOR +CAP +SECCOMP +EBPF +CRIU +YAJL
  os: linux
  remoteSocket:
    exists: true
    path: /run/podman/podman.sock
  security:
    apparmorEnabled: false
    capabilities: CAP_NET_RAW,CAP_CHOWN,CAP_DAC_OVERRIDE,CAP_FOWNER,CAP_FSETID,CAP_KILL,CAP_NET_BIND_SERVICE,CAP_SETFCAP,CAP_SETGID,CAP_SETPCAP,CAP_SETUID,CAP_SYS_CHROOT
    rootless: false
    seccompEnabled: true
    seccompProfilePath: /usr/share/containers/seccomp.json
    selinuxEnabled: true
  serviceIsRemote: false
  slirp4netns:
    executable: /usr/bin/slirp4netns
    package: slirp4netns-1.2.0-2.el9_0.x86_64
    version: |-
      slirp4netns version 1.2.0
      commit: 656041d45cfca7a4176f6b7eed9e4fe6c11e8383
      libslirp: 4.4.0
      SLIRP_CONFIG_VERSION_MAX: 3
      libseccomp: 2.5.2
  swapFree: 3911172096
  swapTotal: 4202688512
  uptime: 124h 56m 26.47s (Approximately 5.17 days)
plugins:
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
  - registry.access.redhat.com
  - registry.redhat.io
  - docker.io
store:
  configFile: /etc/containers/storage.conf
  containerStore:
    number: 10
    paused: 0
    running: 10
    stopped: 0
  graphDriverName: overlay
  graphOptions:
    overlay.mountopt: nodev,metacopy=on
  graphRoot: /var/lib/containers/storage
  graphRootAllocated: 20923285504
  graphRootUsed: 8976498688
  graphStatus:
    Backing Filesystem: xfs
    Native Overlay Diff: "false"
    Supports d_type: "true"
    Using metacopy: "true"
  imageCopyTmpDir: /var/tmp
  imageStore:
    number: 14
  runRoot: /run/containers/storage
  volumePath: /var/lib/containers/storage/volumes
version:
  APIVersion: 4.1.1
  Built: 1658931970
  BuiltTime: Wed Jul 27 16:26:10 2022
  GitCommit: ""
  GoVersion: go1.17.12
  Os: linux
  OsArch: linux/amd64
  Version: 4.1.1
```

**Package info (e.g. output of `rpm -q podman` or `apt list podman` or `brew info podman`):**

```
podman-4.1.1-1.el9_0.x86_64
```

**Have you tested with the latest version of Podman and have you checked the Podman Troubleshooting Guide? (https://github.com/containers/podman/blob/main/troubleshooting.md)**


Yes (latest rhel podman)

**Additional environment details (AWS, VirtualBox, physical, etc.):**
Virtualized
