---
tags: Code-Style
title: "STYLE: specify encodings when opening files"
html_url: "https://github.com/pandas-dev/pandas/issues/52963"
user: MarcoGorelli
repo: pandas-dev/pandas
---

Opening a file without an encoding can cause issues on Windows, there's been some reports from people trying to contribute on Windows running into this

pylint has a check for this, so let's enable it (I've been learning some Rust, so I'll try to get it in to Ruff so it can run in a reasonable amount of time and we can later use that instead - but for now a manual pylint check is fine)

Task here is:

1. make the following change to `.pre-commit-config.yaml`

```diff
diff --git a/.pre-commit-config.yaml b/.pre-commit-config.yaml
index 43b3699907..34cd91940f 100644
--- a/.pre-commit-config.yaml
+++ b/.pre-commit-config.yaml
@@ -83,9 +83,6 @@ repos:
     hooks:
     -   id: pylint
         stages: [manual]
--   repo: https://github.com/pycqa/pylint
-    rev: v2.16.2
-    hooks:
     -   id: pylint
         alias: redefined-outer-name
         name: Redefining name from outer scope
@@ -99,6 +96,11 @@ repos:
             |^pandas/conftest\.py  # keep excluded
         args: [--disable=all, --enable=redefined-outer-name]
         stages: [manual]
+    -   id: pylint
+        alias: unspecified-encoding
+        name: Using open without explicitly specifying an encoding
+        args: [--disable=all, --enable=unspecified-encoding]
+        stages: [manual]
 -   repo: https://github.com/PyCQA/isort
     rev: 5.12.0
     hooks:
```

2. run `pre-commit run unspecified-encoding --all-files`
3. fixup all the violations it reports (by using `encoding='utf-8'`), stage, commit, push, open pull request, celebrate

No need to ask for permission to work on this:
- just comment `take` and it will be assigned to you
- if someone else has commented `take` a week has passed and they haven't done anything (a common occurrence, unfortunately), then feel free to take over. Please only comment `take` if you intend to work on this