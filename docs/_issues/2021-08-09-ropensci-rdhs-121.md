---
tags: 
title: "User submitted query response on how to start interacting with DHS surveys - A demo"
html_url: "https://github.com/ropensci/rdhs/issues/121"
user: OJWatson
repo: ropensci/rdhs
---

<!-- IF THIS INVOLVES AUTHENTICATION: DO NOT SHARE YOUR USERNAME/PASSWORD, OR API KEYS/TOKENS IN THIS ISSUE - MOST LIKELY THE MAINTAINER WILL HAVE THEIR OWN EQUIVALENT KEY -->

<!-- If this issue relates to usage of the package, whether a question, bug or similar, along with your query, please paste your devtools::session_info() or sessionInfo() into the code block below, AND include a reproducible example (consider using a "reprex" https://cran.rstudio.com/web/packages/reprex/) If not, delete all this and proceed :) -->

A user provided question via email, which is being posted here for use for other individuals:

> I'm not familiar with the DHS surveys. I'm working to reproduce a methodology to calculate the wealth index from 43 DHS
surveys using 11 attributes from the household? (Rooms per person, Electricity, Floors, Water, Toilet, Phone, Radio, Tv, Car, Motorbike, Fridge). How do I select them from the surveys? 

The following is a documented answer which I hope helps show how to go about this task:

```r
library(rdhs)

# Step 0 create your config - see documentation online for how to do this correctly 
# rdhs::set_rdhs_config(...)

# Step 1 Using the API to identify surveys of interst
# first find the surveys for the countries of interest, e.g. DRC and Cote d'Ivoire  since 2010 
survs <- rdhs::dhs_surveys(countryIds = c("CD", "CI"), surveyYearStart = 2010)

# now find the actual datasets for these surveys and download the flat file format
datasets <- rdhs::dhs_datasets(surveyIds = survs$SurveyId, fileFormat = "FL")
dataset_names <- datasets$FileName[datasets$FileType == "Household Recode"]

# Now actually get these datasets by downloading them  
d <- rdhs::get_datasets(dataset_names)

# with these downloaded search for what questions are of interest
qus <- rdhs:::search_variable_labels(
  dataset_names, 
  search_terms = "Rooms|Electricity|Floors|Water|Toilet|Phone|Radio|Tv|Car|Motorbike|Fridge"
)

# from this select the specific ids that are of interest, e.g. the first 9
variables <- qus$variable[1:9]

# now search for these
vars <- rdhs:::search_variables(dataset_names, variables)

# use these to extract what you need
extract <- rdhs::extract_dhs(vars)

# and bind them together to create one dataset
# n.b. here we concatenate hv201 as it has non matching labels between the surveys
# this is flagged as a warning if you run this without the labels argument
final_df <- rdhs::rbind_labelled(extract, labels = list("hv201" = "concatenate"))
```
