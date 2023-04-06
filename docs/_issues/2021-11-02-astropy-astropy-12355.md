---
tags: ,Feature-Request,Package-intermediate,cosmology,unified-io
title: "Register ``latex`` to ``Cosmology.write``"
html_url: "https://github.com/astropy/astropy/issues/12355"
user: nstarman
repo: astropy/astropy
---

Cosmology can now read and write to files.
It would be nice to register with ``Cosmology.write`` a  method for exporting a Cosmology to a Latex table.
There are good examples of IO with Cosmology at https://github.com/astropy/astropy/tree/main/astropy/cosmology/io
and documentation at https://docs.astropy.org/en/latest/cosmology/io.html#cosmology-io

I'm thinking the ``write_latex(...)`` method would call ``cosmology.io.table.to_table()``, format the table to e.g. make `H0` -> `$H_0 \rm{[Mpc]}$` or something and then call the `QTable.write(..., format='latex')`.
