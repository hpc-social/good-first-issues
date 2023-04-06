---
tags: ,enhancement,help-wanted
title: "chunk_layer is memory-inefficient"
html_url: "https://github.com/aqlaboratory/openfold/issues/16"
user: gahdritz
repo: aqlaboratory/openfold
---

The `chunk_layer` function in `openfold/utils/tensor_utils.py`, which implements the "chunking" procedure described in subsection 1.11.8 of the Alphafold 2 supplement, relies on a memory-expensive expand/reshape operation at the top to standardize the batch dimensions of input tensors. This operation can be a bottleneck during inference, so some optimization here would do wonders.