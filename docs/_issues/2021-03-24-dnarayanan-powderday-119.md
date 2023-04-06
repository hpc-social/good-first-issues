---
tags: ,bug,variable-extinction
title: "dust masses for gizmo with OTF dust"
html_url: "https://github.com/dnarayanan/powderday/issues/119"
user: dnarayanan
repo: dnarayanan/powderday
---

right now the dust masses for gizmo/gadget datasets with on-the-fly dust won't work for `manual` mode because it will look for `PartType0`.   

a possible way to fix this would be:

1.  in `front_ends/gadget2pd.py` in `_dustsmoothedmasss`, have a clause if `otf_extinction` is set to change:

```    def _dustsmoothedmasses(field, data):
        if yt.__version__ == '4.0.dev0':
            dsm = ds.arr(data.ds.parameters['octree'][('PartType0','Dust_Masses')],'code_mass')
            #return (data.ds.parameters['octree'][('PartType0','Dust_Masses')])
            return dsm
	else:
            return (data.ds.arr(data[("deposit", "PartType0_sum_Dust_Masses")].value, 'code_mass'))```
            
            to take `PartType3` instead.   I think this should deposit the dust masses into the octree (we may need to include a ```ds._sph_ptypes=('PartType0','PartType3')``` line in there as well)