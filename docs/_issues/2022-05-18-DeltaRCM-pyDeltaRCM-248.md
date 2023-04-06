---
tags: ,documentation,help-wanted
title: "Set notated input parameters not being recognized"
html_url: "https://github.com/DeltaRCM/pyDeltaRCM/issues/248"
user: Lvulis
repo: DeltaRCM/pyDeltaRCM
---

We've been using set notation but find that the model is not recognizing these. This may be an edge case as this is an unnecessary scenario where only 1 set of alternatives is provided, not multiple.

The input yaml:
```
out_dir: 'issue_run'
Width: 20000
Length: 15000
h0: 4.0 
S0: .000133
N0_meters: 400
L0_meters: 800
Np_water: 5000
Np_sed: 3000
dx: 200
u0: 1.5
coeff_U_dep_mud: 0.4
save_eta_figs: True
save_eta_grids: True
save_depth_grids: True
save_discharge_grids: True
save_velocity_grids: True
save_sedflux_grids: True
save_sandfrac_grids: True
save_discharge_components: True
set:
  - {f_bedload: 0.24, C0_percent: 0.3}
```

The resulting log file:
```
2022-05-18 20:19:08,166 - INFO - Output log file initialized
2022-05-18 20:19:08,166 - INFO - pyDeltaRCM version 2.1.3
2022-05-18 20:19:08,166 - INFO - Python version 3.10.4 | packaged by conda-forge | (main, Mar 24 2022, 17:38:57) [GCC 10.3.0]
2022-05-18 20:19:08,166 - INFO - Platform: Linux-5.13.0-1023-aws-x86_64-with-glibc2.31
2022-05-18 20:19:08,166 - INFO - Setting up model configuration
2022-05-18 20:19:08,166 - INFO - Model type is: DeltaModel
2022-05-18 20:19:08,167 - INFO - Configuration variable `out_dir`: issue_run
2022-05-18 20:19:08,167 - INFO - Configuration variable `verbose`: 0
2022-05-18 20:19:08,167 - INFO - Configuration variable `seed`: None
2022-05-18 20:19:08,167 - INFO - Configuration variable `Length`: 15000
2022-05-18 20:19:08,167 - INFO - Configuration variable `Width`: 20000
2022-05-18 20:19:08,167 - INFO - Configuration variable `dx`: 200
2022-05-18 20:19:08,167 - INFO - Configuration variable `L0_meters`: 800
2022-05-18 20:19:08,167 - INFO - Configuration variable `S0`: 0.000133
2022-05-18 20:19:08,167 - INFO - Configuration variable `itermax`: 3
2022-05-18 20:19:08,167 - INFO - Configuration variable `Np_water`: 5000
2022-05-18 20:19:08,167 - INFO - Configuration variable `u0`: 1.5
2022-05-18 20:19:08,167 - INFO - Configuration variable `N0_meters`: 400
2022-05-18 20:19:08,167 - INFO - Configuration variable `h0`: 4.0
2022-05-18 20:19:08,167 - INFO - Configuration variable `hb`: None
2022-05-18 20:19:08,167 - INFO - Configuration variable `H_SL`: 0.0
2022-05-18 20:19:08,167 - INFO - Configuration variable `SLR`: 0.0
2022-05-18 20:19:08,167 - INFO - Configuration variable `Np_sed`: 3000
2022-05-18 20:19:08,167 - INFO - Configuration variable `f_bedload`: 0.5
2022-05-18 20:19:08,167 - INFO - Configuration variable `active_layer_thickness`: None
2022-05-18 20:19:08,167 - INFO - Configuration variable `C0_percent`: 0.1
2022-05-18 20:19:08,167 - INFO - Configuration variable `Csmooth`: 0.9
2022-05-18 20:19:08,167 - INFO - Configuration variable `toggle_subsidence`: False
2022-05-18 20:19:08,167 - INFO - Configuration variable `subsidence_rate`: 2e-09
2022-05-18 20:19:08,167 - INFO - Configuration variable `start_subsidence`: 216000
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_eta_figs`: True
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_stage_figs`: False
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_depth_figs`: False
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_discharge_figs`: False
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_velocity_figs`: False
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_sedflux_figs`: False
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_sandfrac_figs`: False
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_figs_sequential`: True
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_metadata`: False
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_eta_grids`: True
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_stage_grids`: False
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_depth_grids`: True
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_discharge_grids`: True
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_velocity_grids`: True
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_sedflux_grids`: True
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_sandfrac_grids`: True
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_discharge_components`: True
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_velocity_components`: False
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_dt`: 86400
2022-05-18 20:19:08,168 - INFO - Configuration variable `checkpoint_dt`: None
2022-05-18 20:19:08,168 - INFO - Configuration variable `save_checkpoint`: False
2022-05-18 20:19:08,168 - INFO - Configuration variable `resume_checkpoint`: False
2022-05-18 20:19:08,168 - INFO - Configuration variable `omega_sfc`: 0.1
2022-05-18 20:19:08,168 - INFO - Configuration variable `omega_flow`: 0.9
2022-05-18 20:19:08,168 - INFO - Configuration variable `Nsmooth`: 10
2022-05-18 20:19:08,168 - INFO - Configuration variable `theta_water`: 1.0
2022-05-18 20:19:08,168 - INFO - Configuration variable `coeff_theta_sand`: 2.0
2022-05-18 20:19:08,169 - INFO - Configuration variable `coeff_theta_mud`: 1.0
2022-05-18 20:19:08,169 - INFO - Configuration variable `beta`: 3
2022-05-18 20:19:08,169 - INFO - Configuration variable `sed_lag`: 1.0
2022-05-18 20:19:08,169 - INFO - Configuration variable `coeff_U_dep_mud`: 0.4
2022-05-18 20:19:08,169 - INFO - Configuration variable `coeff_U_ero_mud`: 1.5
2022-05-18 20:19:08,169 - INFO - Configuration variable `coeff_U_ero_sand`: 1.05
2022-05-18 20:19:08,169 - INFO - Configuration variable `alpha`: 0.1
2022-05-18 20:19:08,169 - INFO - Configuration variable `stepmax`: None
2022-05-18 20:19:08,169 - INFO - Configuration variable `sand_frac_bc`: 0
2022-05-18 20:19:08,169 - INFO - Configuration variable `clobber_netcdf`: False
2022-05-18 20:19:08,169 - INFO - Configuration variable `legacy_netcdf`: False
2022-05-18 20:19:08,169 - INFO - Random seed is: 2744010775 
2022-05-18 20:19:08,328 - INFO - Model initialization complete
2022-05-18 20:19:08,328 - INFO - Time: 0.0; timestep: 0
2022-05-18 20:19:10,574 - INFO - Time: 40000.0; timestep: 1
```