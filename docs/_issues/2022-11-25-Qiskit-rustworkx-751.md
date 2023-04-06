---
tags: ,enhancement
title: "Push generators into rustworkx-core"
html_url: "https://github.com/Qiskit/rustworkx/issues/751"
user: rtzoeller
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues to confirm this idea does not exist. -->

### What is the expected enhancement?

I have a use case where I want to create graphs from Rust code, in the same way that `networkx`/`rustworkx` allows one to create graphs from Python. Unfortunately `rustworkx` contains the graph generators, rather than `rustworkx_core`, so the existing generators are not accessible to me.

I would like to see the generators abstracted of any Python-specific logic and moved into `rustworkx_core`.

Some quick prototyping showed something like this could work (obviously would need to think further about error handling):

```rust
// rustworkx-core/src/generators.rs

use petgraph::prelude::*;

#[inline]
fn get_num_nodes<W>(num_nodes: &Option<usize>, weights: &Option<Vec<W>>) -> usize {
    if weights.is_some() {
        weights.as_ref().unwrap().len()
    } else {
        num_nodes.unwrap()
    }
}

pub fn mesh_graph<N, E, FN, FE>(
    num_nodes: Option<usize>,
    weights: Option<Vec<N>>,
    default_node: FN,
    default_edge: FE,
) -> Result<StableGraph<N, E, Undirected>, &'static str> where FN: Fn() -> N, FE: Fn() -> E {
    if weights.is_none() && num_nodes.is_none() {
        return Err("num_nodes and weights list not specified");
    }
    let node_len = get_num_nodes(&num_nodes, &weights);
    if node_len == 0 {
        return Ok(StableGraph::<N, E, Undirected>::default());
    }
    let num_edges = (node_len * (node_len - 1)) / 2;
    let mut graph = StableGraph::<N, E, Undirected>::with_capacity(node_len, num_edges);
    match weights {
        Some(weights) => {
            for weight in weights {
                graph.add_node(weight);
            }
        }
        None => (0..node_len).for_each(|_| {
            graph.add_node(default_node());
        }),
    };

    for i in 0..node_len - 1 {
        for j in i + 1..node_len {
            let i_index = NodeIndex::new(i);
            let j_index = NodeIndex::new(j);
            graph.add_edge(i_index, j_index, default_edge());
        }
    }

    Ok(graph)
}
```

```rust
// src/generators.rs

#[pyfunction(multigraph = true)]
#[pyo3(text_signature = "(/, num_nodes=None, weights=None, multigraph=True)")]
pub fn mesh_graph(
    py: Python,
    num_nodes: Option<usize>,
    weights: Option<Vec<PyObject>>,
    multigraph: bool,
) -> PyResult<graph::PyGraph> {
    let graph = rustworkx_core::generators::mesh_graph::<PyObject, PyObject, _, _>(
        num_nodes,
        weights,
        || py.None(),
        || py.None(),
    );
    return match graph {
        Ok(g) => Ok(graph::PyGraph {
            graph: g,
            node_removed: false,
            multigraph,
            attrs: py.None(),
        }),
        Err(s) => Err(PyIndexError::new_err(s)),
    };
}
```

Alternatively I can re-implement these generators in my own application directly on top of `petgraph`, but that seems less than ideal.