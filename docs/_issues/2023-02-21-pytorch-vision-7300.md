---
tags: ,enhancement,help-wanted,module-datasets,module-documentation
title: "Improve ImageNet documentation"
html_url: "https://github.com/pytorch/vision/issues/7300"
user: cemde
repo: pytorch/vision
---

### 📚 The doc issue

The [ImageNet documentation](https://pytorch.org/vision/stable/generated/torchvision.datasets.ImageNet.html#torchvision.datasets.ImageNet)  is quite short and skips a lot of steps on how to use it for the first time. A better description on how to use it would be nice.

 As far as I understand 
1. one has to download `...train.tar`, `...val.tar` and `...test.tar` files
2. one has to download the `task 1 and 2 devkit`
3. one has to unpack these into `train`, `val` and `test` folders respectively.
4. one has to use some shell script to reorganise the folder structure into `val/class_tag/image.jpeg`. For val set or for all sets?





### Suggest a potential alternative/fix

Add instructions:
- Visit [https://www.image-net.org/](https://www.image-net.org/) and download the 2012 train, test and val images for Task 1 and 2.
- In your `/data/ImageNet` folder create subfolders `train`, `val` and `test`.
- Unpack the image `.tar` files for each split.
- Copy the following [link here](link here) shell script into your train, val and test folders, respectively and run them. This will reorganize these folders to be compatible with `torchvision.dataset.ImageFolder` which bases the `ImageNet` class.
- 

cc @pmeier