---
tags: ,help-wanted,needs-triage,tbug
title: "Unfriendly error message in CLI: \"invalid Zip archive: Could not find central directory end\""
html_url: "https://github.com/nextstrain/nextclade/issues/974"
user: sacundim
repo: nextstrain/nextclade
---

This happened in an execution of a pretty standard Nextstrain ncov dataset build that didn't change since the last time it succeeded. I don't know if the job had a network connectivity problem at this time or if the archive was bad at the source, but it seems fair to say that the error message could be friendlier (e.g. "The Nextclade dataset file %s is corrupted").

```
python3 scripts/sanitize_sequences.py \
             --sequences results/puerto-rico_all-time/puerto-rico_all-time_subsampled_sequences.fasta.xz \
             --strip-prefixes hCoV-19/ SARS-CoV-2/ \
             --output /dev/stdout 2> logs/sanitize_sequences_before_nextclade_puerto-rico_all-time.txt \
             \| nextclade run \
             --jobs 8 \
             --input-dataset data/sars-cov-2-nextclade-defaults.zip \
             --output-tsv results/puerto-rico_all-time/nextclade_qc.tsv \
             --output-fasta results/puerto-rico_all-time/aligned.fasta \
             --output-translations results/puerto-rico_all-time/translations/aligned.gene.{gene}.fasta \
             --output-insertions results/puerto-rico_all-time/insertions.tsv 2>&1 \| tee logs/align_puerto-rico_all-time.txt
--
 
Error:
0: [91minvalid Zip archive: Could not find central directory end[0m
Location:
[35mpackages_rs/nextclade-cli/src/dataset/dataset_download.rs[0m:[35m76[0m
Backtrace omitted. Run with RUST_BACKTRACE=1 environment variable to display it.
Run with RUST_BACKTRACE=full to include source snippets.
[Sun Aug 28 10:45:10 2022]
Error in rule build_align:
jobid: 24
```

(The "Sun Aug 28 10:45:10 2022" timestamp is UTC)