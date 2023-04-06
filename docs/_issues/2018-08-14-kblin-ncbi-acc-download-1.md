---
tags: ,enhancement,help-wanted
title: "Better user-facing messages on invalid IDs"
html_url: "https://github.com/kblin/ncbi-acc-download/issues/1"
user: areejalsheikh
repo: kblin/ncbi-acc-download
---

Hi,

Thanks for this awesome tool. Could you please help with the following error?

I just tried to run the command in the README

ncbi-acc-download AB_12345 

but I got the error:

    raise DownloadError("Download failed with return code: {}".format(r.status_code))
ncbi_acc_download.core.DownloadError: Download failed with return code: 400

No problems showing the help message ncbi-acc-download -h.

Thanks,
Areej