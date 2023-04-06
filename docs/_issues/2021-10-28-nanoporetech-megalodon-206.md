---
tags: documentation
title: "Updating \"file formats\" docs for additional clarity?"
html_url: "https://github.com/nanoporetech/megalodon/issues/206"
user: lyijin
repo: nanoporetech/megalodon
---

Hi there,

Thanks for writing such an excellent piece of software. The pace of development has definitely outstripped the updates in documentation--and as a newbie to ONT analysis, I was hoping that I could point out some of the pain points and help improve docs for others in my shoes.

The doc that I depended the most on was https://nanoporetech.github.io/megalodon/file_formats.html.

**Linking to updated SAMtags file**
I understand that the Mm and Ml tag was under heavy development, and only codified recently. Could you link users to the updated SAM standards https://samtools.github.io/hts-specs/SAMtags.pdf instead of the issue at hts-specs? There were hundreds of messages in the issue, was really confusing. Thankfully Google read my mind and produced the SAMtags pdf when I searched for it, saving me heaps of trouble.

**Mentioning new IGV can visualise probabilistic methylation**
Thanks to @fidibidi and @marcus1487 raising a request in https://github.com/igvteam/igv/issues/991, IGV can now view probabilistic methylation, and it works really well.

One non-obvious thing that I encountered was that IGV, by default, treats positions with > 20% methylation confidence as methylation; however, megalodon defaults to declaring positions with > 80% methylation confidence as methylated.
To change this threshold in IGV, go to View > Preferences > Alignments, scroll all the way down, Coverage Track Options > Base modification probability threshold, "0.8". This was mentioned in one of the later messages in the issue mentioned above; not my being a genius.

**Mentioning default thresholds**
I've noticed a bunch of issues here that sought clarity on what megalodon's thresholds are in defining a "methylated position" vs. "unmethylated position", e.g. #185. From my poking around (or rather, I think it was because I read #192), I've discovered that megalodon defaults can be checked with `megalodon --help-full`, and grepping for `--mod-aggregate-method` and `--mod-binary-threshold`.

**Clarifying how the bedMethyl file can be compared to BAM file**
I am aware that the bedMethyl file (`modified_bases.5mC.bed`) stores the per-position methylation %. I am interested in also looking at per-read methylation, and I think I should be looking at the BAM file (`mod_mappings.bam`) to parse this information.

However, in #96, @marcus1487 mentioned that "Note that the coverage listed in the bedmethyl file will be slightly lower than the raw coverage since reads which do not produce high confidence predictions (modified/canonical) are not included in the reported lines of the bedmethyl output. "

From my testing in IGV and `samtools depth` on the BAM file, it has indeed more reads at a specific position than what was reported in the BED file. I'd like to filter the BAM file in a way that makes it produce identical coverages as the BED file. What I'm unsure of are the explicit quality filters used to drop "low-confidence" reads. Using #192 to base my guesses, are reads dropped if the read contains methylation confidence scores between 20% and 80%? i.e. using SAMtags Ml:B:C lingo, if the read contains **any** value between 51 <= x <= 204, it gets dropped?

```shell
$ samtools view mod_mappings.bam | cut -f 14 | head -2
Ml:B:C,253,250,253,253,252,34,254,252,254,245,250,249,250,253,251,249,243,250,251,235,243,242,10,220,16,111
Ml:B:C,253,254,215,19,248,232,233,17,90,118,254
```

Retain former, discard latter?


Thanks for your time!