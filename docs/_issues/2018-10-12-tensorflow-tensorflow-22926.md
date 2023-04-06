---
tags: ,statcontribution-welcome,typefeature
title: "Feature Request: GPUOptions for Go binding"
html_url: "https://github.com/tensorflow/tensorflow/issues/22926"
user: mattn
repo: tensorflow/tensorflow
---

Current implementation of Go binding can not specify options.

GPUOptions struct is in internal package. And `go generate` doesn't work for protobuf directory. So we can't specify GPUOptions for `NewSession`.
