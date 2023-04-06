---
tags: ,enhancement,wontfix
title: "in systemParameters merge outcome columns (e.g. \"merger\") into one OUTCOME column"
html_url: "https://github.com/TeamCOMPAS/COMPAS/issues/57"
user: FloorBroekgaarden
repo: TeamCOMPAS/COMPAS
---

In `constants.h` we define what gets printed in the systemParameters.csv output file: 

In `const ANY_PROPERTY_VECTOR BSE_SYSTEM_PARAMETERS_REC = ` 
the following variables are printed: 

`    BINARY_PROPERTY::UNBOUND,
    BINARY_PROPERTY::STELLAR_MERGER,
    BINARY_PROPERTY::STELLAR_MERGER_AT_BIRTH,
`

make this into one variable: `OUTCOME` which can have the options/outcomes: 
unbound, stellar_merger, stellar_merger_at_birth, DCO, 

and thus contains a quick look-up table for all outcomes of the systemParameters. 
