---
tags: Good-First-Issue,kind/feature,network,priority/medium,rootless,slirp4netns
title: "Alternate \"port_handler=slirp4netns\" not implemented for user-defined rootless cni networks"
html_url: "https://github.com/containers/podman/issues/8193"
user: usury
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

Also, there is a running list of known issues in the [Podman Troubleshooting Guide](https://github.com/containers/podman/blob/master/troubleshooting.md),
please reference that page before opening a new issue.

If you are filing a bug against `podman build`, please instead file a bug
against Buildah (https://github.com/containers/buildah/issues). Podman build
executes Buildah to perform container builds, and as such the Buildah
maintainers are best equipped to handle these bugs.
-->

**Is this a BUG REPORT or FEATURE REQUEST? (leave only one on its own line)**

/kind bug

**Description**

Alternate "port_handler=slirt4netns" provided in PR 6965 (https://github.com/containers/podman/pull/6965) for "only 127.0.0.1 within containers" **not implemented** for user-defined rootless cni networks
- specifying "port_handler=slirp4netns" when **connecting** a container to a already-created user-defined rootless cni network does **NOT** error out and does **NOT** implement the behavior provided in PR 6965
- as a result, not possible to see accurate remote address within containers connected to a user-defined rootless cni network (only "127.0.0.1")

**Steps to reproduce the issue:**

```
normaluser@containerhost $> podman network create myCNI

normaluser@containerhost $> podman run --name myNginx1 --publish 8081:80 --network=myCNI -d nginx:alpine
normaluser@containerhost $> podman run --name myNginx2 --publish 8082:80 --network=myCNI:port_handler=slirp4netns -d nginx:alpine
normaluser@containerhost $> podman run --name myNginx3 --publish 8083:80 --network=slirp4netns:port_handler=slirp4netns -d nginx:alpine

normaluser@containerhost $>  podman inspect myNginx1 | grep -i ipaddress
                "IPAddress": "10.89.0.2",
normaluser@containerhost $>  podman inspect myNginx2 | grep -i ipaddress
                "IPAddress": "",
normaluser@containerhost $>  podman inspect myNginx3 | grep -i ipaddress
                "IPAddress": "",

normaluser@containerhost $> podman exec myNginx1 ifconfig
                ## shows loopback and **eth0**, as expected
normaluser@containerhost $> podman exec myNginx2 ifconfig
                ## absolutely blank, not expected
normaluser@containerhost $> podman exec myNginx3 ifconfig
                ## shows loopback and **tap0**, as expected

otherhost $> curl --head http://_containerhost_:8081
otherhost $> curl --head http://_containerhost_:8082
`        curl: (7) Failed to connect to _containerhost_ port 8082: Connection refused`
otherhost $> curl --head http://_containerhost_:8083

normaluser@containerhost $> podman logs myNginx1 | grep HEAD
        127.0.0.1 - - [29/Oct/2020:15:51:25 -0700] "HEAD / HTTP/1.1" 200 0 "-" "curl/7.69.1" "-"
normaluser@containerhost $> podman logs myNginx2 | grep HEAD
        ## nothing to see, no connection succeeded
normaluser@containerhost $> podman logs myNginx3|grep HEAD
        192.168.0.116 - - [29/Oct/2020:15:51:31 -0700] "HEAD / HTTP/1.1" 200 0 "-" "curl/7.69.1" "-"
```
**Describe the results you received:**
"myNginx1" container has only 127.0.0.1 as remote address (confusing), though explained in PR 6965
"myNginx2" container launches without error **however** port not opened and no ip address assigned
"myNginx3" container - no problem - everything makes sense

**Describe the results you expected:**
"myNginx1:" expected to see correct remote address wihin container (though explainded in PR 6965)
"myNginx2:" expected successful ip assignment and port to open using "port_handler=slirp4netns", or contaier launch to fail
"myNginx3" container - no problem - everything makes sense

**Additional information you deem important (e.g. issue happens only occasionally):**
happens consistently and reproducably

**Output of `podman version`:**

```
        Version:      2.1.1
        API Version:  2.0.0
        Go Version:   go1.14
        Built:        Wed Dec 31 16:00:00 1969
        OS/Arch:      linux/amd64
```

**Output of `podman info --debug`:**

```
host:
  arch: amd64
  buildahVersion: 1.16.1
  cgroupManager: cgroupfs
  cgroupVersion: v1
  conmon:
    package: 'conmon: /usr/libexec/podman/conmon'
    path: /usr/libexec/podman/conmon
    version: 'conmon version 2.0.20, commit: '
  cpus: 4
  distribution:
    distribution: debian
    version: "10"
  eventLogger: journald
  hostname: arachne
  idMappings:
    gidmap:
    - container_id: 0
      host_id: 2000
      size: 1
    - container_id: 1
      host_id: 100001
      size: 65536
    uidmap:
    - container_id: 0
      host_id: 2000
      size: 1
    - container_id: 1
      host_id: 100001
      size: 65536
  kernel: 4.19.0-10-amd64
  linkmode: dynamic
  memFree: 369057792
  memTotal: 2091732992
  ociRuntime:
    name: runc
    package: 'runc: /usr/sbin/runc'
    path: /usr/sbin/runc
    version: |-
      runc version 1.0.0~rc6+dfsg1
      commit: 1.0.0~rc6+dfsg1-3
      spec: 1.0.1
  os: linux
  remoteSocket:
    path: /run/user/2000/podman/podman.sock
  rootless: true
  slirp4netns:
    executable: /usr/bin/slirp4netns
    package: 'slirp4netns: /usr/bin/slirp4netns'
    version: |-
      slirp4netns version 1.1.4
      commit: unknown
      libslirp: 4.3.1-git
      SLIRP_CONFIG_VERSION_MAX: 3
  swapFree: 746057728
  swapTotal: 1073737728
  uptime: 184h 14m 26.29s (Approximately 7.67 days)
registries:
  search:
  - docker.io
  - quay.io
version:
  APIVersion: 2.0.0
  Built: 0
  BuiltTime: Wed Dec 31 16:00:00 1969
  GitCommit: ""
  GoVersion: go1.14
  OsArch: linux/amd64
  Version: 2.1.1
```

**Package info (e.g. output of `rpm -q podman` or `apt list podman`):**

```
podman/unknown,now 2.1.1~2 amd64 [installed]
podman/unknown 2.1.1~2 arm64
podman/unknown 2.1.1~2 armhf
podman/unknown 2.1.1~2 ppc64el
```

**Have you tested with the latest version of Podman and have you checked the Podman Troubleshooting Guide?**

Yes

**Additional environment details (AWS, VirtualBox, physical, etc.):**
Container host is a VirtualBox VM running on Fedora 32
podman packages installed from OpenSuse repo
**$> cat "/etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list"**
```
## "Kubic" repo from "OpenSuse" for "podman" packages since they aren't in Debian 10 (buster) repos
deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/Debian_10/ /
```
**$> cat /etc/os-release** 
`PRETTY_NAME="Debian GNU/Linux 10 (buster)"`

