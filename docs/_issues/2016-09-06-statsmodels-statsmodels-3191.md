---
tags: comp-tsa
title: "Convergence information being displayed during ARIMA.fit() regardless of disp value"
html_url: "https://github.com/statsmodels/statsmodels/issues/3191"
user: philipobrien
repo: statsmodels/statsmodels
---

``` python
>>> sm.version.full_version
'0.8.0.dev0+bb1db2b'
```

``` python
arima_model = ARIMA(transformed_data, order=(model_order[0], model_order[1], model_order[2]))
arima_results = arima_model.fit(disp=False)  # or disp=-1
```

```
RUNNING THE L-BFGS-B CODE

           * * *

Machine precision = 2.220D-16
 N =            3     M =           10
 This problem is unconstrained.

At X0         0 variables are exactly at the bounds

At iterate    0    f=  7.16189D+00    |proj g|=  1.29181D-01

At iterate    5    f=  7.00504D+00    |proj g|=  1.47562D-03

At iterate   10    f=  7.00442D+00    |proj g|=  1.79098D-02

At iterate   15    f=  6.93115D+00    |proj g|=  2.95095D-01

At iterate   20    f=  6.84326D+00    |proj g|=  7.16658D-04

           * * *

Tit   = total number of iterations
Tnf   = total number of function evaluations
Tnint = total number of segments explored during Cauchy searches
Skip  = number of BFGS updates skipped
Nact  = number of active bounds at final generalized Cauchy point
Projg = norm of the final projected gradient
F     = final function value

           * * *

   N    Tit     Tnf  Tnint  Skip  Nact     Projg        F
    3     23     25      1     0     0   4.230D-07   6.843D+00
  F =   6.8432611444769238

CONVERGENCE: NORM_OF_PROJECTED_GRADIENT_<=_PGTOL

 Cauchy                time 0.000E+00 seconds.
 Subspace minimization time 0.000E+00 seconds.
 Line search           time 0.000E+00 seconds.

 Total User time 0.000E+00 seconds.
```
