---
tags: easy-problem,enhancement
title: "Support build avatars sourced from non-GitHub URLs"
html_url: "https://github.com/nextstrain/auspice/issues/1441"
user: huddlej
repo: nextstrain/auspice
---

## Context

Each Nextstrain build displays an avatar in the build's byline on nextstrain.org. [This avatar is sourced from the GitHub repository associated with the build](https://github.com/nextstrain/auspice/blob/a0e9080dcd61249f24f6c822dfcf6478e4e07ac2/src/components/info/byline.js#L36-L51) in the Auspice config JSON's `build_url` parameter. This approach allows Nextstrain Groups and community builds, like the Neher lab's European builds to include attribution for their group with the icon shown below:

<img width="808" alt="image" src="https://user-images.githubusercontent.com/85372/147007302-882f862b-b59e-45a0-b909-b63db2a7de0a.png">

## Description

Users (or groups of users) who deploy their data through Nextstrain Groups may not wish (or may not be allowed) to use GitHub to source their workflows. However, they do want a way to include their group logo in the byline of their Nextstrain builds.

Could we allow users to define a path to a custom avatar that is not hosted on GitHub?

## Examples

For example, we could allow users to define their own avatar path in the Auspice JSON config like so:

```json
{
  "title": "Genomic epidemiology of novel coronavirus",
  "build_url": "https://nextstrain.org",
  "build_avatar": "https://path.to/avatar.png",
  "maintainers": [
    {"name": "Someone Great", "url": "https://nextstrain.org"}
  ],
```

## Possible solution

It seems like we could modify [the existing `renderAvatar` method](https://github.com/nextstrain/auspice/blob/a0e9080dcd61249f24f6c822dfcf6478e4e07ac2/src/components/info/byline.js#L36-L51) to look for an `avatarUrl` before it falls back to looking for a GitHub avatar associated with the build URL.