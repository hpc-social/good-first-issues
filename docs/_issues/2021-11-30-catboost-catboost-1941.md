---
title: "GPU accelerated training not available during multitasking and model retraining"
html_url: "https://github.com/catboost/catboost/issues/1941"
user: JHlozek
repo: catboost/catboost
---

I'm currently using Catboost to train multiregression models for large datasets and understandably would like as much of this as possible happening on the GPU. 

At runtime, Catboost indicates that GPU acceleration is not implemented for multitasking.

Secondly, the large datasets need to be split into batches and incrementally trained by setting catboost's 'init_model' parameter when fitting. The first batch (with no 'init_model') can be GPU accelerated but subsequent batches are bound to the CPU as Catboost warns that GPU acceleration is not available when the 'init_model' parameter is set.

Are either of these features planned as they seem like natural next steps considering Catboost's current partial GPU implementation?