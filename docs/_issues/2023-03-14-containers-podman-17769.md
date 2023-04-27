---
tags: Good-First-Issue,bugweek,kind/bug
title: "REST API: \"\\u003cmissing\\u003e\" instead of \"<missing>\" in returned Id attribute ( /v1.24/images/${img}/history )"
html_url: "https://github.com/containers/podman/issues/17769"
user: eriksjolund
repo: containers/podman
---

### Issue Description

In the JSON ouput from the REST API (/v1.24/images/${img}/history)

docker returns
```
<missing>
```

podman returns
```
\u003cmissing\u003e
```


I guess both variants are just two ways to represent the same JSON content so one could argue if this issue is really a bug, but I think there will be less incompatibility issues with docker if podman would use the same output.

(There might be buggy clients that are using the REST API although I haven't seen any examples of problems related to this issue)






### Steps to reproduce the issue


On a Fedora 37 computer (arch: amd64)

1. `sudo -i`
2. `dnf install -y podman`
3. `dnf install -y moby-engine`
4. `systemctl start docker`
5. `useradd test1`
6. `usermod -aG docker test1`
7. `machinectl shell test1@`
8. `podman pull alpine:3.17.2`
9.  run `podman images` and detect the image id. Record the result in a shell variable
     ` img=b2aa39c304c2`
10. `docker pull alpine:3.17.2`
11. `systemctl --user start podman.socket`
12. `curl -s --unix-socket /var/run/docker.sock http://localhost/v1.24/images/${img}/history | grep -o -P '.{0,7}missing.{0,7}'`
13. `curl -s --unix-socket $XDG_RUNTIME_DIR/podman/podman.sock  http://localhost/v1.24/images/${img}/history  | grep -o -P '.{0,7}missing.{0,7}'`


### Describe the results you received

```
$ curl -s --unix-socket /var/run/docker.sock http://localhost/v1.24/images/${img}/history | grep -o -P '.{0,7}missing.{0,7}'
"Id":"<missing>","Siz
$ curl -s --unix-socket $XDG_RUNTIME_DIR/podman/podman.sock  http://localhost/v1.24/images/${img}/history  | grep -o -P '.{0,7}missing.{0,7}'
"\u003cmissing\u003e"
$ 
```

### Describe the results you expected

```
$ curl -s --unix-socket /var/run/docker.sock http://localhost/v1.24/images/${img}/history | grep -o -P '.{0,7}missing.{0,7}'
"Id":"<missing>","Siz
$ curl -s --unix-socket $XDG_RUNTIME_DIR/podman/podman.sock  http://localhost/v1.24/images/${img}/history  | grep -o -P '.{0,7}missing.{0,7}'
"Id":"<missing>","Siz
$ 
```

### podman info output

```yaml
host:
  arch: amd64
  buildahVersion: 1.29.0
  cgroupControllers:
  - cpu
  - io
  - memory
  - pids
  cgroupManager: systemd
  cgroupVersion: v2
  conmon:
    package: conmon-2.1.6-3.fc37.x86_64
    path: /usr/bin/conmon
    version: 'conmon version 2.1.6, commit: '
  cpuUtilization:
    idlePercent: 99.92
    systemPercent: 0.02
    userPercent: 0.06
  cpus: 16
  distribution:
    distribution: fedora
    variant: workstation
    version: "37"
  eventLogger: journald
  hostname: asus
  idMappings:
    gidmap:
    - container_id: 0
      host_id: 50147
      size: 1
    - container_id: 1
      host_id: 37020512
      size: 65536
    uidmap:
    - container_id: 0
      host_id: 50147
      size: 1
    - container_id: 1
      host_id: 37020512
      size: 65536
  kernel: 6.1.15-200.fc37.x86_64
  linkmode: dynamic
  logDriver: journald
  memFree: 838037504
  memTotal: 7691788288
  networkBackend: netavark
  ociRuntime:
    name: crun
    package: crun-1.8.1-1.fc37.x86_64
    path: /usr/bin/crun
    version: |-
      crun version 1.8.1
      commit: f8a096be060b22ccd3d5f3ebe44108517fbf6c30
      rundir: /run/user/50147/crun
      spec: 1.0.0
      +SYSTEMD +SELINUX +APPARMOR +CAP +SECCOMP +EBPF +CRIU +LIBKRUN +WASM:wasmedge +YAJL
  os: linux
  remoteSocket:
    path: /run/user/50147/podman/podman.sock
  security:
    apparmorEnabled: false
    capabilities: CAP_CHOWN,CAP_DAC_OVERRIDE,CAP_FOWNER,CAP_FSETID,CAP_KILL,CAP_NET_BIND_SERVICE,CAP_SETFCAP,CAP_SETGID,CAP_SETPCAP,CAP_SETUID
    rootless: true
    seccompEnabled: true
    seccompProfilePath: /usr/share/containers/seccomp.json
    selinuxEnabled: true
  serviceIsRemote: false
  slirp4netns:
    executable: /usr/bin/slirp4netns
    package: slirp4netns-1.2.0-8.fc37.x86_64
    version: |-
      slirp4netns version 1.2.0
      commit: 656041d45cfca7a4176f6b7eed9e4fe6c11e8383
      libslirp: 4.7.0
      SLIRP_CONFIG_VERSION_MAX: 4
      libseccomp: 2.5.3
  swapFree: 7691300864
  swapTotal: 7691300864
  uptime: 11h 10m 1.00s (Approximately 0.46 days)
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
  configFile: /home/test612/.config/containers/storage.conf
  containerStore:
    number: 0
    paused: 0
    running: 0
    stopped: 0
  graphDriverName: overlay
  graphOptions: {}
  graphRoot: /home/test612/.local/share/containers/storage
  graphRootAllocated: 407822663680
  graphRootUsed: 378301325312
  graphStatus:
    Backing Filesystem: xfs
    Native Overlay Diff: "true"
    Supports d_type: "true"
    Using metacopy: "false"
  imageCopyTmpDir: /var/tmp
  imageStore:
    number: 1
  runRoot: /run/user/50147/containers
  transientStore: false
  volumePath: /home/test612/.local/share/containers/storage/volumes
version:
  APIVersion: 4.4.2
  Built: 1677669779
  BuiltTime: Wed Mar  1 12:22:59 2023
  GitCommit: ""
  GoVersion: go1.19.6
  Os: linux
  OsArch: linux/amd64
  Version: 4.4.2
```


### Podman in a container

No

### Privileged Or Rootless

Rootless

### Upstream Latest Release

Yes

### Additional environment details

_No response_

### Additional information

_No response_