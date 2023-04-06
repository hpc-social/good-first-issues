---
tags: bug,documentation,visualization
title: "plot_mesh.py is undocumented in Wiki and might not show plot"
html_url: "https://github.com/PrincetonUniversity/athena/issues/204"
user: felker
repo: PrincetonUniversity/athena
---

**Summary of issue**

`vis/python/plot_mesh.py` was first added to the repository by @jmstone in 0a10fa8a53e115032013a2dc5d2e4775b89d998c on 2016-04-14 and later generalized to accept `-i`, `-o` flags by @c-white in 8b0d5f5423284d9a4e470c753e8aa113e1012dd7 on 2017-11-03.

The only page in the Wiki that mentions it is the Tutorial page [SMR and AMR](https://github.com/PrincetonUniversity/athena/wiki/SMR-and-AMR). Even there, it only tangentially appears in the example output of the `./athena -m 1` command, while the actual tutorial text instructs the user to use gnuplot to view the SMR mesh structure. 

At a minimum, I feel like it should be documented in [Plotting Scripts](https://github.com/PrincetonUniversity/athena/wiki/Plotting-Scripts) like `plot_lines.py, plot_slice.py, plot_spherical.py`. And/or it should be removed from being mentioned in the stdout output of `Mesh::OutputMeshStructure(int dim)`:
https://github.com/PrincetonUniversity/athena/blob/1da278d86e7a959331ee7eb05a290800aca0f1d1/src/mesh/mesh.cpp#L1013-L1021
(this also assumes the default directory hierarchy, e.g. that the user ran Athena++ in `bin/` subdirectory of the root repository directory)

When I was testing the SMR checks in #200, I tried to use `plot_mesh.py` to visualize the spherical-polar refined meshes, but I believe the script assumes that the `mesh_structure.dat` data was generated using the Cartesian coordinate system. This should be explicitly noted, perhaps in the script name. 

Also, the script would only work with `-o [file]`, see below. 

**Steps to reproduce**
```
make clean; python ./configure.py --prob=linear_wave; make -j
bin/athena -d temp -i inputs/hydro/athinput.linear_wave3d mesh/refinement=static meshblock/nx1=16 meshblock/nx2=16 meshblock/nx3=16 -m 1
python vis/python/plot_mesh.py -i mesh_structure.dat
```
With either Python 2 or 3 on my macOS system, the last command causes the `plt.show()` function to return immediately without displaying the image. I believe this is platform-specific behavior depending on the interactivity of the matplotlib backend (toggled with `plt.ioff()` and `plt.ion()`), but do the other `vis/python/plot*` scripts behave this way? It very much appeared like a bug in the script. 

Adding `-o test.png` to the final command produces the correct image in the file.

**To-do**
- [ ] Document `plot_mesh.py` usage and limitations in [Plotting Scripts](https://github.com/PrincetonUniversity/athena/wiki/Plotting-Scripts) 
- [ ] Fix any bugs with `plot_mesh.py`
- [ ] Adjust or remove instructions from `-m` output
- [ ] Make new directory `vis/python/utils/` and move `uniform.py`, `spherical_refinement.py`, `athena_read.py` there since none of these files directly visualize anything unlike the 4x `plot_*.py` scripts. 