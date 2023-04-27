---
tags: help-wanted,tfeat
title: "Add ability to cancel current task"
html_url: "https://github.com/nextstrain/nextclade/issues/91"
user: ivan-aksamentov
repo: nextstrain/nextclade
---

We want to allow users to stop the currently running task.

For example, there might be a button, which would trigger this action. The implementation should terminate all tasks in worker pools (both, parser and analysis) and return the app into the idling state.

The partial results should probably be discarded. However we may also consider keeping them, especially if #30 is implemented. One nuance to watch out is the export button. We may or may not allow exporting the incomplete results.

In this case we may also add a button to clear the current results, which would return the app to pristine state.


This feature will be handy for users if the run takes too long and they are not willing to wait or if they are running the wrong file by accident. It will be a cleaner solution than just page refresh.
