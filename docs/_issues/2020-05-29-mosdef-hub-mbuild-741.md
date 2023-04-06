---
tags: ,bug
title: "lammpsdata box parameters"
html_url: "https://github.com/mosdef-hub/mbuild/issues/741"
user: amorshedi
repo: mosdef-hub/mbuild
---

In lammpsdata.py the box data are written as:
            data.write('{0:.6f} {1:.6f} xlo xhi\n'.format(
                xlo_bound, xhi_bound))
            data.write('{0:.6f} {1:.6f} ylo yhi\n'.format(
                ylo_bound, yhi_bound))
            data.write('{0:.6f} {1:.6f} zlo zhi\n'.format(
                zlo_bound, zhi_bound))

This seems to be a remnant of lammpstrj.py. However, the data file does NOT use box bounds to define the cell and directly takes xlo,xhi;ylo,yhi;zlo,zhi.
Is this a bug or am I missing something?