---
title: "Cannot use automate_training on Compute Canada cluster"
html_url: "https://github.com/ivadomed/ivadomed/issues/496"
user: jcohenadad
repo: ivadomed/ivadomed
---

Based on internal discussions, it appears that the script `automate_training.py` does not run on Compute Canada. The problem might be coming from the allocation of specific GPUs via this script. 

The purpose of this issue is to document the problem, what has been tried, the communication with Compute Canada, and (ultimately) the solution. So that, in the future, if others run into the same problem, they can start from this issue thread instead of re-investigating from the beginning (and re-emailing Compute Canada folks with the same question). 