---
tags: areadeployment,typebug
title: "streamlit's webserver not working when using BAZEL for installation bug"
html_url: "https://github.com/streamlit/streamlit/issues/4576"
user: rubenverhack
repo: streamlit/streamlit
---

### Summary

Related to https://github.com/streamlit/streamlit/issues/3132 .

An internal check to see if streamlit is running in development mode or not. This checks if some strings are present in the script's file path. This check is not valid for other installation types, e.g. bazel.

The script path in a bazel build is for example:
`/home/{user}/.cache/bazel/_bazel_{user}/b775940771a888524b9eed82a7f43708/execroot/{organization}/bazel-out/k8-fastbuild/bin/apps/daq/streamlit_main.runfiles/pip_deps_pypi__streamlit/streamlit/hello/hello.py`

This could be solved by also checking for "pip_deps_pypi__streamlit" in the development_mode check, or by just having a better check in general.

### Steps to reproduce

Code snippet:

streamlit_main.py
```
import sys
from streamlit import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "hello"]
    sys.exit(stcli.main())

```

BUILD.bazel
```python
load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "streamlit_main",
    srcs = [
        "streamlit_main.py",
    ],
    main = "streamlit_main.py",
    visibility = ["//visibility:public"],
    deps = [
        requirement('streamlit')
    ],
)
```
If applicable, please provide the steps we should take to reproduce the bug:

run "bazel build streamlit_main"

**Expected behavior:**

To not run in development mode;

**Actual behavior:**

Runs in development mode. 

### Is this a regression?

no

### Debug info

- Streamlit version: 1.8.1
- Python version: 3.7
- Using Conda? PipEnv? PyEnv? Pex? BAZEL
- OS version: Ubuntu 20.04
- Browser version:

### Additional information

Workaround: explicitly set developmentMode to false:

```
import sys
from streamlit import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "hello", "--global.developmentMode", "0"]
    sys.exit(stcli.main())

```