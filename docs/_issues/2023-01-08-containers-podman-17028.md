---
tags: Good-First-Issue,kind/feature,kube
title: "[Feature]: Disable automatic publishing of all ports for kube play"
html_url: "https://github.com/containers/podman/issues/17028"
user: Syquel
repo: containers/podman
---

### Feature request description

Currently `podman kube play` automatically publishes all ports which are defined in Kubernetes YAMLs as `containerPort`.

Kubernetes YAML example:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: all-ports-published-reproducer
spec:
  containers:
    - name: all-ports-published-reproducer-nginx
      image: "docker.io/bitnami/nginx:1.23"
      env:
        - name: NGINX_HTTP_PORT_NUMBER
          value: "8082"
      ports:
        - name: http
          containerPort: 8082
```

Podman command: `podman kube play all-ports-published-reproducer.yaml`

Output of `podman port --latest`: `8082/tcp -> 0.0.0.0:8082`

Users should be able to disable this behavior to prevent accidentally publishing ports to the outside world.  

### Suggest potential solution

Similiarly to #16880 a new flag `--publish-all` like the one in [podman run](https://docs.podman.io/en/latest/markdown/podman-run.1.html#publish-all-p) should be added to `podman kube play`.  
This flag should accept a boolean parameter which is `true` by default to preserve the current behavior.

If `--publish-all=false` is set ports should not be automatically published and only be published if the Kubernetes YAML explicitly defines the `hostPort` field.

Kubernetes YAML example with explicit `hostPort` set.
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: all-ports-published-reproducer
spec:
  containers:
    - name: all-ports-published-reproducer-nginx
      image: "docker.io/bitnami/nginx:1.23"
      env:
        - name: NGINX_HTTP_PORT_NUMBER
          value: "8082"
      ports:
        - name: http
          containerPort: 8082
          hostPort: 80
```

### Have you considered any alternatives?

Podman Quadlets would be an alternative but would prevent users from using already existing Kubernetes YAMLs / Helm charts.

### Additional context

#16766 introduces a change to publish ports on a random port instead of reusing the `containerPort` field of the Kubernetes YAML if `hostPort` is not set.  
If the new flag `--publish-all` is set to `false` and the `hostPort` field is explicitly set to `0` the port should be published on a random port.

Even if firewalld is active on the server netavark currently allows these automatically published ports to be reachable from the outside world, which might be a security concern.