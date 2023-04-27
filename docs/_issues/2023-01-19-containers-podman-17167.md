---
tags: Good-First-Issue,kind/bug
title: "[Bug]: host's /etc/hosts file overrides private network dns settings in podman"
html_url: "https://github.com/containers/podman/issues/17167"
user: hcldan
repo: containers/podman
---

### Issue Description

Moving over to a new machine with podman instead of docker, still ironing out the issues using docker-compose with podman.

I used to have a custom domain let's call it foo.bar.com, car.bar.com, etc mapped to 127.0.0.1 in my host's /etc/hosts file.
In the docker-compose.yml I had a private network with those same hosts set.
Inside the containers attached to the network, they would get the private network address, using podman they get 127.0.0.1

### Steps to reproduce the issue

on host machine:
```
127.0.0.1 foo.bar.com proxy.bar.com
```

docker-compose.yml:
```yaml
version: '3.3'

services:
  proxy:
    image: nginx:stable-alpine
    ports:
      - 80:80
      - 443:443
    hostname:  proxy.bar.com
    networks:
      mynet:
        aliases:
          -  proxy.bar.com
  foo:
    image: some-server:latest
    ports:
      - 9555:9555
    hostname:  foo.bar.com
    networks:
      mynet:
        aliases:
          -  foo.bar.com
    volumes:
networks:
  mynet:
    driver: bridge
    ipam:
      driver: default
      config:
      - subnet: 10.10.0.0/16
```

### Describe the results you received

exec into proxy.bar.com

ping foo.bar.com

get 127.0.0.1

### Describe the results you expected

I expected an ip inside the mynet address space

### podman info output

```shell
host:
  arch: amd64
  buildahVersion: 1.27.1
  cgroupControllers:
  - memory
  - pids
  cgroupManager: systemd
  cgroupVersion: v2
  conmon:
    package: conmon-2.1.4-1.el9.x86_64
    path: /usr/bin/conmon
    version: 'conmon version 2.1.4, commit: 56561007b6a59ea175ee9a67384639721499e160'
  cpuUtilization:
    idlePercent: 99.42
    systemPercent: 0.23
    userPercent: 0.36
  cpus: 20
  distribution:
    distribution: '"rhel"'
    version: "9.1"
  eventLogger: journald
  hostname: frisbee
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
  kernel: 5.14.0-162.6.1.el9_1.x86_64
  linkmode: dynamic
  logDriver: journald
  memFree: 26817802240
  memTotal: 66804899840
  networkBackend: netavark
  ociRuntime:
    name: crun
    package: crun-1.5-1.el9.x86_64
    path: /usr/bin/crun
    version: |-
      crun version 1.5
      commit: 54ebb8ca8bf7e6ddae2eb919f5b82d1d96863dea
      spec: 1.0.0
      +SYSTEMD +SELINUX +APPARMOR +CAP +SECCOMP +EBPF +CRIU +YAJL
  os: linux
  remoteSocket:
    exists: true
    path: /run/user/1000/podman/podman.sock
  security:
    apparmorEnabled: false
    capabilities: CAP_NET_RAW,CAP_CHOWN,CAP_DAC_OVERRIDE,CAP_FOWNER,CAP_FSETID,CAP_KILL,CAP_NET_BIND_SERVICE,CAP_SETFCAP,CAP_SETGID,CAP_SETPCAP,CAP_SETUID,CAP_SYS_CHROOT
    rootless: true
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
  swapFree: 33592176640
  swapTotal: 33592176640
  uptime: 41h 58m 30.00s (Approximately 1.71 days)
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
  - registry.access.redhat.com
  - registry.redhat.io
  - docker.io
store:
  configFile: /home/ddumont/.config/containers/storage.conf
  containerStore:
    number: 5
    paused: 0
    running: 1
    stopped: 4
  graphDriverName: overlay
  graphOptions: {}
  graphRoot: /home/ddumont/.local/share/containers/storage
  graphRootAllocated: 988412391424
  graphRootUsed: 45282320384
  graphStatus:
    Backing Filesystem: xfs
    Native Overlay Diff: "true"
    Supports d_type: "true"
    Using metacopy: "false"
  imageCopyTmpDir: /var/tmp
  imageStore:
    number: 13
  runRoot: /run/user/1000/containers
  volumePath: /home/ddumont/.local/share/containers/storage/volumes
version:
  APIVersion: 4.2.0
  Built: 1666809014
  BuiltTime: Wed Oct 26 14:30:14 2022
  GitCommit: ""
  GoVersion: go1.18.4
  Os: linux
  OsArch: linux/amd64
  Version: 4.2.0


```


### Podman in a container

No

### Privileged Or Rootless

Rootless

### Upstream Latest Release

Yes

### Additional environment details

RHEL 9.1

### Additional information

_No response_