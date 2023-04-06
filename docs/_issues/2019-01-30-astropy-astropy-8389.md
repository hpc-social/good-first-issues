---
tags: ,Docs,Effort-low,Package-novice,coordinates,io.fits,wcs
title: "Intuitively manage column-wise WCS coordinates "
html_url: "https://github.com/astropy/astropy/issues/8389"
user: matteobachetti
repo: astropy/astropy
---

In the X-ray data I'm analyzing I have single photons and their X and Y coordinates. The WCS information that allows the conversion to sky coordinates is contained in the header in the form of `TXXXXNN` keywords, where `NN` indicates the column and `XXXX` the wcs parameter (`CDLT` for `cdelta`, `CRVL` for `cval` etc.). If I read the FITS data structure, I see that this information is assigned to the FITS column
```
In [15]: data.columns
Out[15]: 
ColDefs(
(...)
    name = 'X'; format = '1I'; unit = 'pixel'; null = -1; coord_type = 'RA---TAN'; coord_unit = 'deg'; coord_ref_point = 500.5; coord_ref_value = 148.9584; coord_inc = -0.0006828076
    name = 'Y'; format = '1I'; unit = 'pixel'; null = -1; coord_type = 'DEC--TAN'; coord_unit = 'deg'; coord_ref_point = 500.5; coord_ref_value = 69.67944; coord_inc = 0.0006828076
)
```
but
1. apparently it is lost if I actually try to access the fits column (e.g. `data['X']` is a numpy array, it has no attribute `coord_type` or any other)
2. there is no apparent easy way to transform these columns into coordinates (they are just treated as numpy arrays by `SkyCoord` et al.)

It would be great to have an easy way to get these columns and transform them to `SkyCoord` objects, but I couldn't find one.
For reference, what I'm doing right now as a workaround is the following, which probably duplicates some functionality already implemented in Astropy but not easily accessible.

```
def get_wcs_from_col(hdu, col):
    import re
    num_re = re.compile('^[a-zA-Z]+([0-9]+)$')
    header = hdu.header
    ttypes = [k for k in header.keys() if k.startswith('TTYP')]
    coltypes = [header[k].strip() for k in ttypes]
    typ = [ttyp for ttyp, colt in zip(ttypes, coltypes) if colt == col.strip()][0]
    num = num_re.match(typ).group(1)
    res = type('wcsinfo', (), {})()
    res.form = header['TFORM' + num]
    res.lmin = header['TLMIN' + num]
    res.lmax = header['TLMAX' + num]
    res.crval = header['TCRVL' + num]
    res.crpix = header['TCRPX' + num]
    res.cdelt = header['TCDLT' + num]
    res.ctype = header['TCTYP' + num]
    res.cunit = header['TCUNI' + num]
    return res


def get_wcs_from_bintable(hdu, xcol, ycol):
    from astropy import wcs
    header = hdu.header
    xwcs = get_wcs_from_col(hdu, xcol)
    ywcs = get_wcs_from_col(hdu, ycol)

    w = wcs.WCS(naxis=2)

    w.wcs.crpix = [xwcs.crpix, ywcs.crpix]
    w.wcs.cdelt = np.array([xwcs.cdelt, ywcs.cdelt])
    w.wcs.crval = [xwcs.crval, ywcs.crval]
    w.wcs.ctype = [xwcs.ctype, ywcs.ctype]

    return w
```

Thanks in advance for your help