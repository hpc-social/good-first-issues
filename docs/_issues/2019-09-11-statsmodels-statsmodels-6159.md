---
tags: ,comp-tsa,type-enh
title: "ENH: Improvements to new ARIMA-type estimators"
html_url: "https://github.com/statsmodels/statsmodels/issues/6159"
user: ChadFulton
repo: statsmodels/statsmodels
---

Collection of follow-ups to #5827. These can/should be broken out into individual PRs. Many are relatively straightforward and would make a good first PR.

### General

- [x] Documentation (none was added in original PR).
- [x] Release notes.
- [ ] Example notebook.
- [x] Double-check how `sm.tsa.arima.ARIMA` works with `fix_params` (it should fail except when the fit method is `statespace`).
- [ ] Estimators that do not support seasonal models per se should support models where the only seasonal part is seasonal differencing.

### GLS

- [ ] Add support for fixed parameters
- [ ] Improve "Returns" documentation for `other_results`.
- [ ] Add documentation for why we have e.g. `include_constant` but not other trend specifications (e.g. that it is to maintain consistency with estimation methods with assumptions that require demeaned series).
- [ ] Fix the following test and put it back into the GLS test suite:

```python
@pytest.mark.low_precision('Test against Example 6.6.3 in Brockwell and Davis'
                           ' (2016)')
# @pytest.mark.xfail(reason="Source appears to find suboptimal parameters")
def test_brockwell_davis_example_663():
    # TODO: the parameters described by BD appear to be suboptimal (based on
    # llf computed from state space form), so that this test fails. Should try
    # to confirm with ITSM2000 (i.e. see if we can get it to find better
    # parameters closer to what we find, or compare llf, or something).
    # TODO: quite a slow test, and xfail anyway due to finding better
    # parameters...
    # Get the data, perform seasonal differencing
    endog = sbl.diff(12).iloc[12:]

    exog = pd.Series((sbl.index > '1983-01-01').astype(int),
                     index=sbl.index).diff(12).iloc[12:]

    res, _ = gls(endog, exog, order=(0, 0, 12), max_iter=3)

    assert_allclose(res.exog_params, -328.45, atol=1e-2)
    assert_allclose(res.ma_params,
                    [.219, .098, .031, .064, .069, .111, .081,
                     .057, .092, -0.28, .183, -.672], atol=1e-3)
    assert_allclose(res.sigma2, 12581, atol=1)
```

### Hannan Rissanen

- [ ] Better warnings / errors when series are short relative to lag length
- [x] Add support for fixed parameters
- [ ] Seems like we could add support for seasonal parameters in this model.
- [ ] Tests for the case with the bias-corrected estimator.

### Innovations MLE

- [ ] Add support for fixed parameters

### Innovations algorithm

- [ ] Add support for ARMA models; see Brockwell and Davis (2016) p.154 and Example 5.1.6.  This estimator should be feasible given the Cython versions of the general innovations algorithm that introduced in #5947.
