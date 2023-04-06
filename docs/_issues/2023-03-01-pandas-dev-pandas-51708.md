---
tags: ,Code-Style
title: "STYLE enable ruff PLW2901"
html_url: "https://github.com/pandas-dev/pandas/issues/51708"
user: MarcoGorelli
repo: pandas-dev/pandas
---

Task is:

1. check the [contributing guide](https://pandas.pydata.org/docs/dev/development/contributing_environment.html) for how to set up your environment
2. remove `PLW2901` from

https://github.com/pandas-dev/pandas/blob/2c10d93b8b2ccee79434c251ac9c1cd94513cc1e/pyproject.toml#L272-L273

3. run `pre-commit run ruff --all-files`
4. fixup the errors it flags - see https://beta.ruff.rs/docs/rules/redefined-loop-name/ for more info on this error
5. stage, commit, push, open pull request