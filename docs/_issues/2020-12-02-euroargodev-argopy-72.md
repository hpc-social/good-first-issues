---
tags: argo-core,enhancement,invalid,stale
title: "TEOS-10 Accessor Improvement Suggestions"
html_url: "https://github.com/euroargodev/argopy/issues/72"
user: DocOtak
repo: euroargodev/argopy
---

Hi @gmaze 

I was poking though the xarray accessor code and noticed some things in the teos10() method:

* There is a [pressure to depth](https://github.com/euroargodev/argopy/blob/9dcd108e5ab166776121a98b0ddd2b1b5a082e77/argopy/xarray.py#L731) conversion before [calculating conservative temperature](https://github.com/euroargodev/argopy/blob/9dcd108e5ab166776121a98b0ddd2b1b5a082e77/argopy/xarray.py#L737). The last parameter of the [CT_from_t](https://teos-10.github.io/GSW-Python/gsw_flat.html#gsw.CT_from_t) function is pressure.
* If the "standard_name" attribute is meant to be CF compliant (the GDAC argo data themselves claim to be CF compliant), the value of it needs to come from the [CF Standard Name](http://cfconventions.org/Data/cf-standard-names/76/build/cf-standard-name-table.html) table, the buoyancy frequency and Potential Vorticity variable do not have a standard name, but there is a proposal process for getting names added to the list if we want to.
* I think it might be a good idea to match the "variable names" in the GSW libraries (including case):
  * SA
  * CT
  * SIG0 -> sigma0
  * N2 -> Nsquared
  * PV (maybe IPV? I don't know if this is the same thing, the TEOS-10 manual talks a lot of about isopycnal potential vorticity)
  * PTEMP -> pt
* It should be documented that the Nsquared has been shifted back to the CT pressure levels rather than midpoints.
* The PV value is not directly from the gsw toolbox, I'm not too familiar with these calculations, but maybe should also be noted in the docstring.

The first point about pressure and depth in CT is an actual bug.

I can prepare a PR to address some/all of these.

One other comment, the recent gsw 3.4 release has support for directly operating on xarray objects, including Datasets/arrays that are backed by some sort of chunked storage (e.g. dask), I think the calls to `.values` would need to be removed if support for this was desired.