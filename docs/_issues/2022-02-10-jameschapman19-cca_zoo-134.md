---
tags: enhancement,help-wanted
title: "Add method to compute explained covariance "
html_url: "https://github.com/jameschapman19/cca_zoo/issues/134"
user: JohannesWiesner
repo: jameschapman19/cca_zoo
---

I know this is easy to compute, but still nice to have out-of-the-box: Wouldn't it make sense to also add a `compute_covariance` method to `_CCA_Base`? Like such:

```python
def explained_variance(X,y,X_weights,y_weights):
    '''Compute covariance'''

    # standardize X and y 
    X_std = zscore(X,axis=0,ddof=1)
    y_std = zscore(y,axis=0,ddof=1)
    
    # calculate covariance matrix
    covmat = X_weights.T @ X_std.T @ y_std @ y_weights
    
    # calculate covariance explained by each component
    explained_var =  np.diag(covmat)**2 / np.sum(np.diag(covmat)**2) 

    return explained_var
```