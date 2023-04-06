---
tags: Good-first-issue,enhancement
title: "replace `pytorch_testing_utils` with native PyTorch solution"
html_url: "https://github.com/pystiche/pystiche/issues/524"
user: pmeier
repo: pmeier/pystiche
---

A long long time ago, I was fed up that PyTorch didn't provide an solution for testing two tensors for approximate equality. To overcome this I started [`pytorch_testing_utils`](https://github.com/pmeier/pytorch_testing_utils), which is still used in our test suite:

https://github.com/pystiche/pystiche/blob/74d7bc51b73e33c98135ee8bd721a34bc8c6137f/tox.ini#L19-L20

Since `torch==1.9.0` we have access to [`torch.testing.assert_close`](https://pytorch.org/docs/stable/testing.html#torch.testing.assert_close) that makes the other project obsolete and should work as a drop-in replacement. 

Since we also support older PyTorch versions, I suggest we provide minimal working alternative with the undocumented [`torch.testing.assert_allclose`](https://github.com/pytorch/pytorch/blob/e85d494707b835c12165976b8442af54b9afcb26/torch/testing/__init__.py#L201-L223) similar to what I did in kornia/kornia#1031.