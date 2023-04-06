---
tags: ,enhancement,help-wanted
title: "Argument types for MathFunctions"
html_url: "https://github.com/sxs-collaboration/spectre/issues/462"
user: nilsdeppe
repo: sxs-collaboration/spectre
---

# Feature request:

`MathFunction`s currently take `DataVector`s, which works in 1D but is not what we want in higher dimensions. We need to be able to deal with situations like `ScalarWave::Solutions::PlaneWave` where there is effective dimension collapsing happening and then the `MathFunction` is called on the resulting collapsed "coordinates". A discussion with @wthrowe @kidder @gsb76  and myself resulted in the conclusion that the current most promising path forward is for `MathFunction` to take a `tnsr::i<T, Dim, Frame>` where we generated explicit instantiations for both `Frame::Inertial` (the "normal" case where you're passing cartesian coordinates) and `Frame::NoFrame` where you are passing something like the collapsed-dimension coordinates in `ScalarWave::Solutions::PlaneWave`.