---
tags: ,future
title: "Triply jagged branches"
html_url: "https://github.com/JuliaHEP/UnROOT.jl/issues/119"
user: aminnj
repo: JuliaHEP/UnROOT.jl
---

One day someone will ask about this :) (eg. each event has N tracks each of which has M subdetectors which have P hits). The doubly jagged interpretation is ~15 lines of julia, so I don't think this will be so complicated to add.

```python
>>> import uproot4
>>> t = uproot4.open("tree_with_triply_jagged.root")["t1"]
>>> t["bi"].array()
<Array [[[[1, 2], [2]], ... []]], [[[100]]]] type='7 * var * var * var * int64'>
>>> t["bi"].array().tolist()
[[[[1, 2], [2]], [[3, 5]]], [[[7, 9, 11], [13, 15, 16]]], [[[17, 18], [19]], []], [], [[]], [[[]]], [[[100]]]]
```
file generated with
```python
#!/usr/bin/env python
import ROOT as r
f = r.TFile("tree_with_triply_jagged.root", "recreate")
t = r.TTree("t1","t1")
vvvi = r.vector("vector<vector<int>>")()
vvvf = r.vector("vector<vector<float>>")()
t.Branch("bi", vvvi)
t.Branch("bf", vvvf)
data = [
        [[[1,2],[2]], [[3,5]]],
        [[[7,9,11], [13,15,16]]],
        [[[17,18], [19]], []],
        [],
        [[]],
        [[[]]],
        [[[100]]],
        ]
for row in data:
    vvvi.clear()
    vvvf.clear()
    for subrow in row:
        vvi = r.vector("vector<int>")()
        vvf = r.vector("vector<float>")()
        for subsubrow in subrow:
            vi = r.vector("int")()
            vf = r.vector("float")()
            for e in subsubrow:
                vi.push_back(e)
                vf.push_back(e + 0.5)
            vvi.push_back(vi)
            vvf.push_back(vf)
        vvvi.push_back(vvi)
        vvvf.push_back(vvf)
    t.Fill()
t.Write()
f.Close()
```