---
tags: ,enhancement,symbolic,tensor
title: "Remove the restriction that metric tensor can only be 'uu' or 'll'"
html_url: "https://github.com/einsteinpy/einsteinpy/issues/584"
user: WenyinWei
repo: einsteinpy/einsteinpy
---

The `ValueError` restriction that says`Configuration can't have one upper and one lower index in Metric Tensor` in `MetricTensor` is neither physical nor exception-safe. We all know the metric tensors would be identity tensor in 'ul' and 'lu' index, which is physically reasonable. The only benefit is that it preserves all the information because the transformation to identity tensor is avoided. The reason is not worthy to throw a severe exception and interrupt the user process.   

🎯 **Goal**

Without the thrown exception, an automated formula deduction would be smarter and it could more flexibly utilize the metric tensor. 


💡 **Possible solutions**

Sol. 1. Just remove the restriction and users would need to take the responsibilty to know it will lose all information when transformed to 'ul' or 'lu'. 

Sol. 2. Let the metric tensor memorize its 'uu' or 'll' states so that it preserves the symbol relation which would tell it how to transform from 'uu' to 'ul' and then from 'ul' to 'll'.