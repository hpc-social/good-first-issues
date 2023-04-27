---
tags: enhancement
title: "Add boundary conditions for different sides in Brick and Rectangle"
html_url: "https://github.com/sxs-collaboration/spectre/issues/2871"
user: nilsdeppe
repo: sxs-collaboration/spectre
---

# Feature request:

The boundary conditions being applied are controlled through the input file, with the domain creator controlling which boundaries the boundary conditions are applied to. The `Rectangle` and `Brick` (and their `Rotated` counter parts) all assume a single boundary condition for all sides. It would be good to add to `Rectangle` and `Brick` an `Options::Alternatives` that allows specifying one boundary condition for all sides, or one per side. Some granularity in the middle could also be possible, but I think that's overkill. This would be good to do with:
- [ ] `Rectangle`
- [ ] `Brick`

Note: I don't think it's worth doing for the `Rotated` variants since those are mostly there for testing communication between elements, not for actual simulations.

A good, but much more involved one to do would be `AlignedLattice`, but it's unclear that's worth the effort. Probably the best thing there would be for each block the user lists the directions in which boundary conditions will be applied, and which boundary condition. This is _extremely_ verbose in the input file.