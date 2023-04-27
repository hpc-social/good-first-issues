---
tags: Good-First-Issue,concept,help-needed,math-and-logic
title: "[Analysis] Analyze differences in outputs generated with LSA method and solved with linalg.solve"
html_url: "https://github.com/DataverseLabs/pyinterpolate/issues/378"
user: SimonMolinsky
repo: DataverseLabs/pyinterpolate
---

The kriging weights are solved with this piece of code:

```python

def solve_weights(weights: np.ndarray, k: np.ndarray, allow_lsa=False) -> np.ndarray:
    """
    Function solves Kriging System.

    Parameters
    ----------
    weights : numpy array
              Array of weights of size m:m.

    k : numpy array
        Array of semivariances of size m:n.

    allow_lsa : bool, default = False
                Allow algorithm to use Least Squares Approximation when solver fails.

    Returns
    -------
    solved : numpy array
             Final weights to estimate predicted value.

    Warns
    -----
    ZerosMatrixWarning : raised when weights / k matrices are full of zeros.
    """

    try:
        solved = np.linalg.solve(weights, k)
    except np.linalg.LinAlgError as linalgerr:
        if np.mean(weights) == 0 or np.mean(k) == 0:
            warnings.warn(ZerosMatrixWarning().__str__())
            solved = np.zeros(len(k))
        else:
            if allow_lsa:
                warnings.warn(LeastSquaresApproximationWarning().__str__())
                solved = np.linalg.lstsq(weights, k, rcond=None)
                solved = solved[0]
            else:
                raise linalgerr

    return solved
```

The solution of the kriging system `solved = np.linalg.solve(weights, k)` may end with `LinAlgError` when the matrix is singular. The two most common scenarios are:

- data has points with the exact coordinates (it is not deduplicated)
- one of the arrays from `weights` or `k` is full of zeros. 

In the second case, the algorithm works but returns warning and zeros. In the first scenario, the algorithm may find an approximate solution with the least squares algorithm.

The case here is to write a simple function that performs multiple tests for different data inputs and checks how values between both algorithms differ (in this context, we must avoid Singularities). Are there scenarios where LSA will give a result different from a result obtained from solving the matrix system? How significant is the difference? This task should be written as a functional, complex test limited to two `numpy` functions: `np.linalg.solve` and `np.linalg.lstsq`.