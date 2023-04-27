---
tags: enhancement
title: "[FEATURE]: an option to show all subcommands `--help-all`"
html_url: "https://github.com/buildtesters/buildtest/issues/1453"
user: shahzebsiddiqui
repo: buildtesters/buildtest
---

### Please describe your feature

currently we see all the subcommands when running `buildtest --help`

```console
COMMANDS:
  
    build (bd)          Build and Run test
    buildspec (bc)      Buildspec Interface
    config (cg)         Query buildtest configuration
    report (rt)         Query test report
    inspect (it)        Inspect a test based on NAME or ID
    path                Show path attributes for a given test
    history (hy)        Query build history
    schema              List schema contents and examples
    cdash               Upload test to CDASH server
    unittests (test)    Run buildtest unit tests
    stylecheck (style)  Run buildtest style checks
    cd                  change directory to root of test given a test name
    clean               Remove all generate files from buildtest including
                        test directory, log files, report file, buildspec
                        cache, history files.
    docs                Open buildtest docs in browser
    schemadocs          Open buildtest schema docs in browser
    debugreport (debug)
                        Display system information and additional information
                        for debugging purposes.
    stats               Show test statistics for given test
    info                Show details regarding current buildtest setup
    help (h)            buildtest command guide
    tutorial-examples   Generate documentation examples for Buildtest Tutorial

```

This is going to be an issue going forward as we add more sub-commands. We should add some option let's say `buildtest --help-all` that will show all subcommands. For instance we don't need to show `unittests`, `stylecheck` `docs` `schemadocs` and `tutorial-examples` command since they are used for development purposes. 

That being said the `buildtest --help` should show a subset of the commands and `buildtest --help-all` should show everything. 

### Suggest potential solution

_No response_

### Additional Information

_No response_

### Post question in Slack

- [X] I agree that I posted my question in [slack](https://hpcbuildtest.slack.com/) before creating this issue

### Is there an existing issue

- [X] I confirm there is no existing [issue](https://github.com/buildtesters/buildtest/issues) for this issue