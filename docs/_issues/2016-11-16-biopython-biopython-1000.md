---
tags: From-Redmine
title: "Deprecate record.database_letters, record.query_letters"
html_url: "https://github.com/biopython/biopython/issues/1000"
user: vincentdavis
repo: biopython/biopython
---

From redmine [XML Blast parser: miscellaneous bug fixes and cleanup](https://redmine.open-bio.org/issues/2176)
Most of the cleanup, bug fixes were done. The last comment was:

> We could perhaps deprecate record.database_letters immediately, and at a later point, record.query_letters

There is a [TODO](https://github.com/biopython/biopython/blob/589bc075ace24cb29bcd69c9789963df7febeb4d/Bio/Blast/NCBIXML.py#L188) in the code regarding this.


@peterjc last comment

> I've updated CVS as per comment 12 to also use record.query_length, and comment 13 to also use record.database_length.
> 
> Before:
> 
> from Bio.Blast import NCBIXML
> for record in NCBIXML.parse(open("xbt007.xml")) :
> 
> ... print record.query_id
> ... print record.query_letters, record.query_length
> ... print record.num_letters_in_database, record.database_letters, record.database_length
> ... 
> gi|585505|sp|Q08386|MOPB_RHOCA
> 270 None
> 13958303 None None
> gi|129628|sp|P07175.1|PARA_AGRTU
> 222 None
> 13958303 None None
> 
> Now, with Bio/Blast/NCBIXML.py CVS revision 1.20 or 1.21,
> 
> from Bio.Blast import NCBIXML
> for record in NCBIXML.parse(open("xbt007.xml")) :
> 
> ... print record.query_id
> ... print record.query_letters, record.query_length
> ... print record.num_letters_in_database, record.database_letters, record.database_length
> ... 
> gi|585505|sp|Q08386|MOPB_RHOCA
> 270 270
> 13958303 None 13958303
> gi|129628|sp|P07175.1|PARA_AGRTU
> 222 222
> 13958303 None 13958303
> 
> We could perhaps deprecate record.database_letters immediately, and at a later point, record.query_letters