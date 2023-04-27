---
tags: please-take-this-issue
title: "CI doesn't run against updated master branch"
html_url: "https://github.com/nextstrain/auspice/issues/1108"
user: jameshadfield
repo: nextstrain/auspice
---

The GitHub CI should run tests against a merge of the PRs branch into master, via the `actions/checkout@v2` module with default settings (docs [here](https://github.com/actions/checkout), code [here](https://github.com/nextstrain/auspice/blob/master/.github/workflows/ci.yaml#L66)). 

PR #1087 [failed the bundlesize CI](https://github.com/nextstrain/auspice/pull/1087/checks?check_run_id=647790106)
```
FAIL  ./dist/auspice.bundle.js: 194.2KB > maxSize 180KB (gzip) 
```

I decided to update the allowed bundle sizes to 200KB and pushed this change to master via 90d91e94ebe19680c3cd966292ede107cfb3180b (I did not touch this PR). I then manually triggered "re-run jobs", however the CI continued to fail using the "old" limits (180KB). I merged it anyway, and the master branch CI passed as expected.

The actual checkout command (via the CI logs, link above) is `/usr/bin/git checkout --progress --force -B svg-in-md refs/remotes/origin/svg-in-md` and doesn't seem to include a merge into master, however other PRs have behaved as if they are running the CI on a merge of the PR into master (or vice versa). 

1) Can we confirm that the CI on a PR is being run on a merge of the PR into master?
2) When master has been updated, how can I re-trigger the CI to run and include the new changes present in master?
