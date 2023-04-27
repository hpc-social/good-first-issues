---
tags: Good-first-issue,areaIO,typeEnhancement
title: "oldmin/oldmax aren't handled properly"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/582"
user: tashrifbillah
repo: InsightSoftwareConsortium/ITK
---

### Description

cc: @jcfr @lassoan @pieper 

Nifti1 has [scl_slope and scl_inter](https://nifti.nimh.nih.gov/nifti-1/documentation/nifti1fields/nifti1fields_pages/scl_slopeinter.html). The equivalent attributes in the NRRD are [oldmin and oldmax](http://teem.sourceforge.net/nrrd/format.html#oldmin) as if:

```
    # define oldmin and oldmax when scl_slope and scl_inter are present
    img= nibabel.load('filename')
    dtype= img.header.get_data_dtype().name
    scl_slope= img.dataobj.slope
    scl_inter= img.dataobj.inter

    if scl_slope!=1.0 or scl_inter!=0:
        info= np.iinfo(dtype)
        oldmin= info.min*scl_slope+scl_inter
        oldmax= info.max*scl_slope+scl_inter
        print(f'old min: {oldmin}')
        print(f'old max: {oldmax}')
```

(you can also look at this [commit](https://github.com/rordenlab/dcm2niix/commit/177c4c37eabbb54ec183c750117e4957f0fc65c3) by Chris Rorden)

### Actual behavior

However, after I defined old min and old max in the NRRD header, the data reported in Slicer aren't scaled. The difference becomes stark when you load both NIFTI and NRRD image in Slicer. NIFTI voxels are scaled while NRRD aren't. On the other hand, fslview, NIBABEL both report the data after scaling.

### Expected behavior

So, we should report NRRD data after scaling them as follows:

find scl_slope and scl_inter from above and
scaled_data= unscaled_data*scl_slope+ scl_inter

### Additional Information

Work with the following public data: the T1_echo*.nii.gz have scaling present in the NIFTI.
http://people.cas.sc.edu/rorden/SW/dcm2niix/odd/multiechotest_Philips_Vanderbilt.zip
dcm2niix should do the DICOM-->NIFTI conversion for you. Then you can use [conversion](https://github.com/pnlbwh/conversion) repository to convert NIFTI-->NHDR
