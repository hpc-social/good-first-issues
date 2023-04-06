---
tags: ,Good-First-Issue,flakes,kind/bug
title: "e2e: play kube symlink: missing hello"
html_url: "https://github.com/containers/podman/issues/17958"
user: edsantiago
repo: containers/podman
---

```
  podman play kube should be able to run image where workdir is a symlink
...
Expected
      <string>: 
  to contain substring
      <string>: hello
```
in [int remote f37 root sqlite](https://api.cirrus-ci.com/v1/artifact/task/5944004907368448/html/int-remote-fedora-37-root-host-sqlite.log.html#t--podman-play-kube-should-be-able-to-run-image-where-workdir-is-a-symlink--1)

To my untrained eye it looks like a race: https://github.com/containers/podman/blob/2cfb6e1c0e10033d90559d2fdb682cb80616e878/test/e2e/play_kube_test.go#L1940-L1947

(there should be a "wait" somewhere, either `--wait` in the play, or a subsequent `podman wait`). Hardly seems worth the effort of filing an issue, it'd be quicker to just fix it in a PR... but the *correct* solution is to walk through the entire test file and look for other such issues, and that's a job for later.