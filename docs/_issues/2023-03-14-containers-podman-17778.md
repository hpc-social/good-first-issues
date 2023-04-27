---
tags: Good-First-Issue,HTTP-API,kind/bug
title: "Build image `pull` field type mismatch with Docker"
html_url: "https://github.com/containers/podman/issues/17778"
user: cristianrgreco
repo: containers/podman
---

### Issue Description

Docker accepts any string value for the `pull` field to indicate the image should be pulled:https://docs.docker.com/engine/api/v1.42/#tag/Image/operation/ImageBuild

Podman expects the value to equal either boolean `true` or string `true`:
https://docs.podman.io/en/latest/_static/api.html?version=v4.4#tag/images/operation/ImageBuildLibpod

Applications that align with Docker's spec are unable to switch to Podman as building an image with this field fails.

### Steps to reproduce the issue

1. POST to the create image endpoint with `pull` set to a string, such as `always`.


### Describe the results you received

No response stream received

### Describe the results you expected

Expected a response stream

### podman info output

```yaml
host:
  arch: amd64
  buildahVersion: 1.29.0
  cgroupControllers:
  - memory
  - pids
  cgroupManager: systemd
  cgroupVersion: v2
  conmon:
    package: conmon_2:2.1.7-0debian9999+obs15.6_amd64
    path: /usr/bin/conmon
    version: 'conmon version 2.1.7, commit: '
  cpuUtilization:
    idlePercent: 87.46
    systemPercent: 5.69
    userPercent: 6.84
  cpus: 2
  distribution:
    codename: jammy
    distribution: ubuntu
    version: "22.04"
  eventLogger: journald
  hostname: fv-az646-90
  idMappings:
    gidmap:
    - container_id: 0
      host_id: 123
      size: 1
    - container_id: 1
      host_id: 165536
      size: 65536
    uidmap:
    - container_id: 0
      host_id: 1001
      size: 1
    - container_id: 1
      host_id: 165536
      size: 65536
  kernel: 5.15.0-1034-azure
  linkmode: dynamic
  logDriver: journald
  memFree: 4857856000
  memTotal: 7281278976
  networkBackend: netavark
  ociRuntime:
    number: 0
    paused: 0
    running: 0
    stopped: 0
  graphDriverName: overlay
  graphOptions: {}
  graphRoot: /home/runner/.local/share/containers/storage
  graphRootAllocated: 89297309696
  graphRootUsed: 58336636928
  graphStatus:
    Backing Filesystem: extfs
    Native Overlay Diff: "true"
    Supports d_type: "true"
    Using metacopy: "false"
  imageCopyTmpDir: /var/tmp
  imageStore:
    number: 0
  runRoot: /run/user/1001/containers
  transientStore: false
  volumePath: /home/runner/.local/share/containers/storage/volumes
version:
  APIVersion: 4.4.2
  Built: 0
  BuiltTime: Thu Jan  1 00:00:00 1970
  GitCommit: ""
  GoVersion: go1.19.6
  Os: linux
  OsArch: linux/amd64
  Version: 4.4.2
```


### Podman in a container

Yes

### Privileged Or Rootless

Rootless

### Upstream Latest Release

Yes

### Additional environment details

`DOCKER_HOST=unix:///run/user/$(id -u)/podman/podman.sock`

### Additional information

_No response_