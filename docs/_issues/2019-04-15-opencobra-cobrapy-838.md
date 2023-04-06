---
tags: ,needs-information
title: "Inconsistency in finding blocked reactions"
html_url: "https://github.com/opencobra/cobrapy/issues/838"
user: hvdinh16
repo: opencobra/cobrapy
---

For the function cobra.flux_analysis.find_blocked_reactions:

If the function is implemented by the scripts below, the number of blocked reactions will be miscalculated, only specific for GLPK solver and not for Gurobi or CPLEX:
import cobra
model = cobra.io.read_sbml_model('./iRhtoC.xml')
model.solver = 'glpk'
result = cobra.flux_analysis.find_blocked_reactions(model, reaction_list=model.reactions,
            open_exchanges=True, zero_cutoff=1e-6)

If the function is implemented by the second method below, the number of blocked reactions is correct for GLPK solver:
from cobra.flux_analysis import find_blocked_reactions
from cobra.io import read_sbml_model
config = cobra.Configuration()
config.solver = 'glpk'
model = read_sbml_model('iRhtoC.xml')
result = find_blocked_reactions(model, open_exchanges=True, zero_cutoff=model.tolerance)

Scripts and model are attached below:
[blocked_reactions.ipynb.tar.gz](https://github.com/opencobra/cobrapy/files/3082063/blocked_reactions.ipynb.tar.gz)
[iRhtoC.xml.zip](https://github.com/opencobra/cobrapy/files/3082067/iRhtoC.xml.zip)

This issue propagates to memote, reported in https://github.com/opencobra/memote/issues/639