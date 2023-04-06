---
tags: ,enhancement
title: "Auto-Detect when changing params in `dataset_balanced_division_to_folds(reset_split=False)`"
html_url: "https://github.com/BiomedSciAI/fuse-med-ml/issues/185"
user: SagiPolaczek
repo: BiomedSciAI/fuse-med-ml
---

**Is your feature request related to a problem? Please describe.**
When calling `dataset_balanced_division_to_folds(reset_split=False)` we don't look at the parameters:
```
    if os.path.exists(output_split_filename) and not reset_split:
        return load_pickle(output_split_filename)
    else:
...
```
Meaning that if `output_split_filename` exists, the changes won't take place. Thus the user needs to change it manually or worse, be confused with the results.

**Describe the solution you'd like**
When necessary, auto-reset the split file.  

**Describe alternatives you've considered**
1. Save the parameters in the split file (or hash them) and read them each time, looking for a diff.
2. Save the parameters (or hash them) in a different file.
3. Manually inspect the parameters.

**Additional context**
:)