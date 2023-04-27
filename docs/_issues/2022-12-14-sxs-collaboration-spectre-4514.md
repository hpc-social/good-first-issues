---
title: "Compute ADM quantities in initial data sets"
html_url: "https://github.com/sxs-collaboration/spectre/issues/4514"
user: nilsvu
repo: sxs-collaboration/spectre
---

We need to compute ADM quantities in our initial data sets to understand the physical properties of the data that we're evolving. To learn about ADM quantities, a good place to start is chapter 3.5 in the book "Numerical Relativity" by Baumgarte & Shapiro. For example, we want to compute M_ADM by Eq. (3.149) in the book. It involves a surface integral over the excision boundaries that represent the two black holes, and a volume integral over the rest of the domain. First steps are:

- Write functions that compute the integrands of Eq. (3.149). They can go in `src/PointwiseFunctions/Xcts/Adm.{h,c}pp`. The volume integrand function can look like this:

  ```cpp
  void adm_mass_volume_integrand(gsl::not_null<Scalar<DataVector>*> result,
      const Scalar<DataVector>& conformal_factor, const tnsr::ii<DataVector, 3>& conformal_metric,
      const tnsr::Ijj<DataVector, 3>& conformal_christoffel_second_kind, const Scalar<DataVector>& conformal_ricci_scalar,
      const tnsr::ii<DataVector, 3>& extrinsic_curvature, const Scalar<DataVector>& trace_extrinsic_curvature,
      const Scalar<DataVector>& energy_density, const Mesh<3>& mesh,
      const InverseJacobian<DataVector, 3, Frame::ElementLogical, Frame::Inertial>& inv_jacobian);
  ```
  
  We can use tensor expressions to compute quantities. Search for `tenex::evaluate` in the code to find examples. We can take derivatives using the `partial_derivative` function from `NumericalAlgorithms/LinearOperators/PartialDerivatives.hpp`.

- Test the functions by computing the ADM mass of a Schwarzschild black hole in Kerr-Schild coordinates. This can be written in `tests/Unit/PointwiseFunctions/Xcts/Test_Adm.cpp`.
- Write compute tags for both integrands and add them to the `SolveXcts` executable.
- Observe the volume integral using the `ObserveVolumeIntegrals` event and the surface integral using the excision surface observer.
- Then we can compute also ADM momentum and angular momentum.