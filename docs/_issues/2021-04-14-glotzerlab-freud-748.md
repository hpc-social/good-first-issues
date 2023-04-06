---
tags: ,locality
title: "NeighborList should be constructible from system-like object and 2D array of bond indices"
html_url: "https://github.com/glotzerlab/freud/issues/748"
user: bdice
repo: glotzerlab/freud
---

**Is your feature request related to a problem? Please describe.**
Occasionally I need to construct a NeighborList from bond topology data, which is currently somewhat hard to do. I've written the pattern below at least a dozen times, and it would be much better as a single function.

**Describe the solution you'd like**
A new class method like `NeighborList.from_system(system, indices, weights)` would be helpful.

Here's a rough implementation that needs to be improved/tested. Note that this snippet will break with #738 (distances need to be replaced by vectors).
```python
    @classmethod
    def from_system(cls, system, indices, weights=None):
        R"""Create a NeighborList from a system-like object and indices.

        Example::

            import freud
            import numpy as np
            box = freud.box.Box(2, 3, 4, 0, 0, 0)
            points = np.array([[0, 0, -1], [0.5, -1, 0]])
            indices = np.array([[0, 1], [1, 0]])
            nlist = freud.locality.NeighborList.from_system(
                system=(box, points),
                indices=indices,
            )

        Args:
            system:
                Any object that is a valid argument to
                :class:`freud.locality.NeighborQuery.from_system`.
            indices (:math:`\left(N_{bonds}, 2\right)` :class:`np.ndarray`):
                Array of integers corresponding to indices in the sets of
                query points and points.
            weights (:math:`\left(N_{bonds}, \right)` :class:`np.ndarray`, optional):
                Array of per-bond weights (if :code:`None` is given, use a
                value of 1 for each weight) (Default value = :code:`None`).
        """
        cdef NeighborQuery nq = NeighborQuery.from_system(system)
        query_point_indices = indices[:, 0]
        point_indices = indices[:, 1]
        distances = np.linalg.norm(
            system.box.wrap(system.points[point_indices] - system.points[query_point_indices])
            axis=-1,
        )
        return cls.from_arrays(
            num_query_points=len(system.points),
            num_points=len(system.points),
            query_point_indices=query_point_indices,
            point_indices=point_indices,
            distances=distances,
            weights=weights,
        )
```