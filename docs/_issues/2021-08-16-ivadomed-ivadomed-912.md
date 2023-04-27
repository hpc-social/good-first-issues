---
title: "Add support for uncertainty with microscopy data"
html_url: "https://github.com/ivadomed/ivadomed/issues/912"
user: mariehbourget
repo: ivadomed/ivadomed
---

## Issue description
This issue is part of the inference refactoring project to include microscopy data (#306). Currently, the uncertainty feature is not working as expected with microscopy data.

### Current behavior
1. Epistemic uncertainty: the output filneames of the PNG `_pred` files are not correct (ex: `sub-rat3_sample-data9_SEM_pred_00.nii.gz_seg-axon-manual_pred.png` instead of `sub-rat3_sample-data9_SEM_pred_00.png`).
2. Aleatoric uncertainty is blocked because of the PNG files alongside the NifTI files in the `pred_masks` folder. The `combine_predictions` function tries to read all files in `pred_masks` as NifTI (including the PNGs)
<details>
<summary> Error aleatoric uncertainty </summary>

```
Error: Traceback (most recent call last):
  File "/home/mhbourget/venv-ivadomed-38c/bin/ivadomed", line 11, in <module>
    load_entry_point('ivadomed', 'console_scripts', 'ivadomed')()
  File "/home/mhbourget/code/ivadomed/ivadomed/main.py", line 566, in run_main
    run_command(context=context,
  File "/home/mhbourget/code/ivadomed/ivadomed/main.py", line 470, in run_command
    pred_metrics = imed_testing.test(model_params=model_params,
  File "/home/mhbourget/code/ivadomed/ivadomed/testing.py", line 83, in test
    imed_uncertainty.run_uncertainty(ifolder=path_3Dpred)
  File "/home/mhbourget/code/ivadomed/ivadomed/uncertainty.py", line 45, in run_uncertainty
    combine_predictions(fname_pred_lst, fname_pred, fname_soft, thr=thr)
  File "/home/mhbourget/code/ivadomed/ivadomed/uncertainty.py", line 72, in combine_predictions
    mc_data = np.array([nib.load(fname).get_fdata() for fname in fname_lst])
  File "/home/mhbourget/code/ivadomed/ivadomed/uncertainty.py", line 72, in <listcomp>
    mc_data = np.array([nib.load(fname).get_fdata() for fname in fname_lst])
  File "/home/mhbourget/venv-ivadomed-38c/lib/python3.8/site-packages/nibabel/loadsave.py", line 55, in load
    raise ImageFileError(f'Cannot work out file type of "{filename}"')
nibabel.filebasedimages.ImageFileError: Cannot work out file type of "log_microscopy_sem_uncertainty/pred_masks/sub-rat3_sample-data9_SEM_pred_00.nii.gz_seg-axon-manual_pred.png"
```
</details>

### Expected behavior
Other issues may arise while fixing those. The behavior of the entire uncertainty pipeline needs to be verified with microscopy data to make sure the correct output files are created.