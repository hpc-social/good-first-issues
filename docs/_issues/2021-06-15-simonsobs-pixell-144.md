---
tags: ,documentation
title: "Improve IAU/COSMO documentation in enmap.read_map"
html_url: "https://github.com/simonsobs/pixell/issues/144"
user: zatkins2
repo: simonsobs/pixell
---

* pixell version: 0.12.1
* Python version: 3.9.5
* Operating System: Ubuntu 20.04

### Description

Currently `enmap.read_map` flips the U component of an `ndmap` in an opaque way, depending on the contents of the fits header. The fits header needs to have specific cards/values for the introspection to flip the component. These conditions (all evaluated in `enmap.get_stokes_flips`) should be documented. Also, the default behavior of the function (to convert **to COSMO**) should be documented, or amended and documented if we want to run with IAU going forward.

Even better, it would be nice to have some user arguments supply optional information about the data, e.g. which axes might need to be flipped, and what the desired output convention is, which could help handle the case of "simple" fits headers (as are produced with the `enmap.write_map` defaults) when the automatic introspection of the polarization convention, according to the conditions, might fail. 

### What I Did

Playing with fits header of a file with a known polarization convention. I believe all these conditions (see `enmap.get_stokes_flips`) must be true for `enmap.read_fits` to flip the polarization convention:

1.  There must be a "CTYPEn" card with value "STOKES", where "n" is the "NAXIS" index of each stokes-like component, for each stokes-like component.
2. If included in the header, "CRPIXn", "CRVALn", and "CRDELTn" (with "n" as above) must be set so that `(3-crval)/cdelt+crpix - 1` gives the 0-indexed index of the U component in "NAXISn".
3. If "CRPIXn", "CRVALn", and "CRDELTn" are **not** included in the header, the U component in "NAXISn" must be at index 2 of the 0-indexed axis (i.e., their default values are all `1.0` such that `(3-crval)/cdelt+crpix - 1` is 2).
4. A "POLCONV" or "POLCCONV" card must be supplied with either "COSMO" or "IAU". If previous conditions met and either card is not supplied, **assume data in IAU and convert to COSMO**. If previous conditions met and the card value is not "COSMO" or "IAU," **assume data in IAU and do no conversion**.

I agree there is no clean way of avoiding the need for specific set of cards/values for automatic introspection, but the behavior should be made clear for new users I think.