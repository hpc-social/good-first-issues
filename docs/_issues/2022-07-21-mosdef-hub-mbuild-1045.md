---
tags: low-priority
title: "Polymer Builder issue"
html_url: "https://github.com/mosdef-hub/mbuild/issues/1045"
user: CalCraven
repo: mosdef-hub/mbuild
---

**Bug summary**

I was trying to create a polymer using the polymer builder, and ran into some buggy behavior. Essentially, I have a single bead that I want to act as the monomer, and it already has oriented ports. I have to use the replace=False argument, but then the add_monomer() method is trying to add ports that are already there. However, this method works if I had the monomer directly to the polymer class. So I wanted to make sure these methods are consistent and allow the user to do what they want either way.


**Code to reproduce the behavior**

Please include a code snippet that can be used to reproduce this bug.

```python
import mbuild as mb
class _CH3(mb.Compound):
    def __init__(self):
        super().__init__()
        self.name = "_CH3"
        
        """Create a particle name _CH3 and add it to self."""
        _ch3 = mb.Compound()
        self.add(_ch3)
        
        
        """Create a port attached to the _CH3 particles, label as 'up'.
        Use the separation value of the _CH2's ports as above.
        """
        port_up = mb.Port(anchor=_ch3, orientation=[0, 0, 1], separation=0.07)
        self.add(port_up, label="up")


class _CH2(mb.Compound):
    def __init__(self):
        super().__init__()
        self.name = "_CH2"
        """Create a partilce name _CH2 and add it to self."""
        _ch2 = mb.Compound()
        self.add(_ch2)
        
        
        """Create a port attached to the _CH2 particles, label as 'up'."""
        port_up = mb.Port(anchor=_ch2, orientation=[0, 0, 1], separation=0.07)
        self.add(port_up, "up")
        
        
        """Create a port attached to the _CH2 particles, label as 'down',
        with same separation but opposite orientation as 'up port'
        """
        port_down = mb.Port(anchor=_ch2, orientation=[0, 0, -1], separation=0.07)
        self.add(port_down, "down")


_ch2 = _CH2()
_ch3 = _CH3()
polymer_works = Polymer(monomers=[_CH2()]
polymer_works.build(n=5) 

polymer_broken = Polymer()
polymer_broken.add_monomer(CH2(), replace=False, indices=[0,0], orientation=[[0,0,1], [0,0,-1]], separation=2.5)
polymer_broken.build(n=5)
```

Output
```
---------------------------------------------------------------------------
MBuildError                               Traceback (most recent call last)
Input In [60], in <cell line: 8>()
      6 polymer = Polymer()
      7 monomer = _CH2()
----> 8 polymer.add_monomer(monomer, replace=False, indices=[0,0], orientation=[[0,0,1], [0,0,-1]], separation=2.5)
     10 """Build the just-created object with length 5"""
     11 # Enter your code here

File ~/miniconda3/envs/fomms-workshop/lib/python3.9/site-packages/mbuild/lib/recipes/polymer.py:279, in Polymer.add_monomer(self, compound, indices, separation, orientation, replace)
    276 comp = clone(compound)
    278 for idx, label, orientation in zip(indices, port_labels, orientation):
--> 279     _add_port(comp, label, idx, separation, orientation, replace)
    280 if replace:
    281     remove_atom1 = comp[indices[0]]

File ~/miniconda3/envs/fomms-workshop/lib/python3.9/site-packages/mbuild/lib/recipes/polymer.py:387, in _add_port(compound, label, idx, separation, orientation, replace)
    380     anchor = compound[idx]
    382 port = Port(
    383     anchor=anchor,
    384     orientation=orientation,
    385     separation=separation / 2,
    386 )
--> 387 compound.add(port, label=label)
    388 return separation

File ~/miniconda3/envs/fomms-workshop/lib/python3.9/site-packages/mbuild/compound.py:732, in Compound.add(self, new_child, label, containment, replace, inherit_periodicity, inherit_box, reset_rigid_ids)
    729     label = label_pattern.format(count)
    731 if not replace and label in self.labels:
--> 732     raise MBuildError(f'Label "{label}" already exists in {self}.')
    733 else:
    734     self.labels[label] = new_child

MBuildError: Label "up" already exists in <_CH2 1 particles, 0 bonds, non-periodic, id: 6307720976>.
```


I think there needs to be a way to use add_monomer that works equivalently to when the polymer class is initialized.

**Software versions**
python=3.8
mbuild=0.15.0
