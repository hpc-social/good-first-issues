---
tags: ,enhancement
title: "Map remaining pymatgen/atomate sets and workflows"
html_url: "https://github.com/jacksund/simmate/issues/157"
user: jacksund
repo: jacksund/simmate
---

At the moment, our tasks and workflows are simply re-implementations of vasp sets from pymatgen (and by extension atomate). This issue outlines a to-do list of writing all sets in Simmate.

Because of the quantity, this will take some time to implement all sets/workflows. This is still a straightforward process for each, so this is a good spot to jump in and help for new contributors -- even if it's just one or two sets.

From [pymatgen.io.vasp.sets](https://pymatgen.org/pymatgen.io.vasp.sets.html):
- [ ] LobsterSet (requires [lobster](http://www.cohp.de/) package)
- [x] MITMDSet
- [x] MITRelaxSet
- [x] MITNEBSet
- [x] MPHSEBSSet
- [x] MPHSERelaxSet
- [x] MPMDSet
- [x] MPMetalRelaxSet
- [x] MPNMRSet
- [x] MPNonSCFSet
- [x] MPRelaxSet
- [ ] MPSOCSet
- [x] MPScanRelaxSet (requires VASP v6)
- [x] MPScanStaticSet (requires VASP v6)
- [x] MPStaticSet
- [x] MVLElasticSet
- [x] MVLGBSet
- [ ] ~~MVLGWSet~~ (seems more like a utility than a preset)
- [x] MVLNPTMDSet
- [ ] ~~MVLRelax52Set~~  (simply updates potcars to newer versions, which simmate already does)
- [ ] MVLScanRelaxSet (requires VASP v6)
- [ ] MVLSlabSet (when should this be used over MVLGBSet(slab_mode=True)?)


From [pymatgen.analysis.diffusion.neb.io](https://github.com/materialsvirtuallab/pymatgen-analysis-diffusion/blob/master/pymatgen/analysis/diffusion/neb/io.py):
- [x] MVLCINEBEndPointSet
- [x] MVLCINEBSet


Overall workflows from [atomate.vasp.workflows.base.library](https://github.com/hackingmaterials/atomate/tree/main/atomate/vasp/workflows/base/library):

- [x] bandstructure
- [ ] bandstructure_boltztrap
- [x] bandstructure_hse
- [x] bandstructure_hse_full
- [x] bandstructure_hse_gap
- [x] bandstructure_noopt
- [ ] dielectric_constant
- [ ] dielectric_constant_no_opt
- [ ] magnetic_deformation
- [ ] metagga_optimization
- [x] neb
- [ ] nmr
- [x] optimize_only
- [ ] piezoelectric_constant
- [ ] spinorbit_coupling
- [x] static_only
- [ ] transmuter

(note, several of these workflows exist, but have not been tested for compatibility with atomate yet)







