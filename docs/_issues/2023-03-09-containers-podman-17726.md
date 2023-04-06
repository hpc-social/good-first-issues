---
tags: ,Good-First-Issue,kind/bug
title: "Distribution API seems missing"
html_url: "https://github.com/containers/podman/issues/17726"
user: lnnwvr
repo: containers/podman
---

### Issue Description

DockerApi 1.41 describes a distribution api path to query image data. This seems to be missing int he current podman socket api implementation

### Steps to reproduce the issue

podman system service --time=0 unix:///tmp/podman.sock

curl -v --unix-socket /tmp/podman.sock -X POST http://localhost/v1.41/distribution/docker.io/library/postgres:latest/json

### Describe the results you received

```
*   Trying /tmp/podman.sock:0...
* Connected to localhost (/tmp/podman.sock) port 80 (#0)
> POST /v1.41/distribution/docker.io/library/postgres:latest/json HTTP/1.1
> Host: localhost
> User-Agent: curl/7.87.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 404 Not Found
< Content-Type: text/plain; charset=utf-8
< X-Content-Type-Options: nosniff
< Date: Thu, 09 Mar 2023 15:27:57 GMT
< Content-Length: 10
< 
Not Found
* Connection #0 to host localhost left intact

````

### Describe the results you expected

The json containing the data

### podman info output

```yaml
$ podman info
host:
  arch: amd64
  buildahVersion: 1.30.0-dev
  cgroupControllers:
  - cpu
  - memory
  - pids
  cgroupManager: systemd
  cgroupVersion: v2
  conmon:
    package: /usr/bin/conmon is owned by conmon 1:2.1.6-1
    path: /usr/bin/conmon
    version: 'conmon version 2.1.6, commit: 158b5421dbac6bda96b1457955cf2e3c34af29bc'
  cpuUtilization:
    idlePercent: 97.3
    systemPercent: 0.72
    userPercent: 1.98
  cpus: 16
  databaseBackend: boltdb
  distribution:
    distribution: manjaro
    version: unknown
  eventLogger: journald
  hostname: unimportant
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
  kernel: 5.15.94-1-MANJARO
  linkmode: dynamic
  logDriver: journald
  memFree: 1965797376
  memTotal: 46107783168
  networkBackend: netavark
  ociRuntime:
    name: crun
    package: /usr/bin/crun is owned by crun 1.8-1
    path: /usr/bin/crun
    version: |-
      crun version 1.8
      commit: 0356bf4aff9a133d655dc13b1d9ac9424706cac4
      rundir: /run/user/1000/crun
      spec: 1.0.0
      +SYSTEMD +SELINUX +APPARMOR +CAP +SECCOMP +EBPF +CRIU +YAJL
  os: linux
  remoteSocket:
    exists: true
    path: /run/user/1000/podman/podman.sock
  security:
    apparmorEnabled: false
    capabilities: CAP_CHOWN,CAP_DAC_OVERRIDE,CAP_FOWNER,CAP_FSETID,CAP_KILL,CAP_NET_BIND_SERVICE,CAP_SETFCAP,CAP_SETGID,CAP_SETPCAP,CAP_SETUID
    rootless: true
    seccompEnabled: true
    seccompProfilePath: /etc/containers/seccomp.json
    selinuxEnabled: false
  serviceIsRemote: false
  slirp4netns:
    executable: /usr/bin/slirp4netns
    package: /usr/bin/slirp4netns is owned by slirp4netns 1.2.0-1
    version: |-
      slirp4netns version 1.2.0
      commit: 656041d45cfca7a4176f6b7eed9e4fe6c11e8383
      libslirp: 4.7.0
      SLIRP_CONFIG_VERSION_MAX: 4
      libseccomp: 2.5.4
  swapFree: 49937981440
  swapTotal: 50793357312
  uptime: 78h 33m 52.00s (Approximately 3.25 days)
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
registries: {}
store:
  configFile: /home/mleinweber/.config/containers/storage.conf
  containerStore:
    number: 0
    paused: 0
    running: 0
    stopped: 0
  graphDriverName: overlay
  graphOptions: {}
  graphRoot: /home/mleinweber/.local/share/containers/storage
  graphRootAllocated: 452606554112
  graphRootUsed: 203020681216
  graphStatus:
    Backing Filesystem: extfs
    Native Overlay Diff: "true"
    Supports d_type: "true"
    Using metacopy: "false"
  imageCopyTmpDir: /var/tmp
  imageStore:
    number: 27
  runRoot: /run/user/1000/containers
  transientStore: false
  volumePath: /home/mleinweber/.local/share/containers/storage/volumes
version:
  APIVersion: 4.5.0-dev
  Built: 1678375483
  BuiltTime: Thu Mar  9 16:24:43 2023
  GitCommit: 747369c82df67d83f65d064855d83a40f0ee99cc-dirty
  GoVersion: go1.20
  Os: linux
  OsArch: linux/amd64
  Version: 4.5.0-dev
```


### Podman in a container

No

### Privileged Or Rootless

Rootless

### Upstream Latest Release

No

### Additional environment details

Additional environment details

### Additional information

Additional information like issue happens only occasionally or issue happens with a particular architecture or on a particular setting