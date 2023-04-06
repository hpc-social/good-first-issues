---
tags: ,CLI,build,feat/enhancement,help-wanted
title: "Switch to using Typer over Click"
html_url: "https://github.com/scikit-hep/pyhf/issues/1674"
user: matthewfeickert
repo: scikit-hep/pyhf
---

### Summary

@dantrim has shown very nicely with his [`hamming-codec`](https://github.com/dantrim/hamming-codec) project that [Typer](https://typer.tiangolo.com/) provides a nice Click based CLI interface with typing support to minimize the amount of code that needs to be written. I now also see that Typer nicely motivates shell completions for the user

```console
$ docker run --rm -ti python:3.9 /bin/bash
root@c66abf9f4a80:/# python -m venv venv && . venv/bin/activate
(venv) root@c66abf9f4a80:/# python -m pip --quiet install --upgrade pip setuptools wheel
(venv) root@c66abf9f4a80:/# python -m pip install hamming-codec
(venv) root@c66abf9f4a80:/# hamming --help
Usage: hamming [OPTIONS] COMMAND [ARGS]...

  Top-level entrypoint into hamming-codec commandline utilities

Options:
  -v, --verbose                   Verbose output
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  decode  Decode the input message that is the specified number of bits...
  encode  Encode the provided input data word, which is interpreted as...
(venv) root@c66abf9f4a80:/# hamming --install-completion bash
bash completion installed in /root/.bash_completions/hamming.sh
Completion will take effect once you restart the terminal
(venv) root@c66abf9f4a80:/# . ~/.bashrc  # As in Docker manually source, as can't make a new tab easily
(venv) root@c66abf9f4a80:/# hamming  # tab here
decode  encode  
(venv) root@c66abf9f4a80:/# hamming
```

To me this is a huge selling point on its own. :+1: 

### Additional Information

https://github.com/click-contrib/click-completion is no longer developed (last commit in 2019) so probably best to move off of it.

This is Click's current approach to shell completion: https://click.palletsprojects.com/en/8.0.x/shell-completion/

### Code of Conduct

- [X] I agree to follow the Code of Conduct