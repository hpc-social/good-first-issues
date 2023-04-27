---
tags: help-wanted
title: "How can I disable filename abbreviations in the results of tab-autocompletion?"
html_url: "https://github.com/ipython/ipython/issues/12105"
user: cxrodgers
repo: ipython/ipython
---

Note 1: This is not the same tab-completion bug for which many issues have already been opened (the one where a massive number of objects from the global namespace are displayed). This issue specifically has to do with unwanted abbreviation of filename paths. I haven't yet found any other reports of this issue.

Note 2: I also posted this to stackoverflow but am posting again here since I didn't receive a response there yet.
https://stackoverflow.com/questions/59548675/how-can-i-disable-filename-abbreviations-in-the-results-of-tab-autocompletion-in

Issue begins now:
When I use tab-autocompletion to complete file paths in ipython, the results are not very useful because it abbreviates each path to just the first and last characters, separated by an ellipsis.

This is the result from pressing tab when there are 5 matches, each about 60 characters long.
```
In [2]: ls /home/jack/mnt/nas2_home/misc/201912
/h…s/ /h…a/ /h…n/ /h…o/ /h…o/
```

These are the desired results, obtained with a previous version (see below):
```
In [2]: ls /home/jack/mnt/nas2_home/misc/201912
/home/jack/mnt/nas2_home/misc/20191207_PoseTF_new_sessions/ 
/home/jack/mnt/nas2_home/misc/20191209_adrian_data/         
/home/jack/mnt/nas2_home/misc/20191217_PoseTF_curation/     
/home/jack/mnt/nas2_home/misc/20191230_PoseTF_fullvideo/    
/home/jack/mnt/nas2_home/misc/20191231_PoseTF_fullvideo/
```
I used 'readlinelike' autocompletions, but the results are the same using the 'column' or 'multicolumn' options for c.TerminalInteractiveShell.display_completions. I renamed my entire .ipython directory and created a new profile with all the default settings, so I don't think it is any weird setting that I have.

Here are the installed versions of some relevant modules:

```
ipython                   7.11.1           py37h39e3cac_0  
jedi                      0.16.0                   py37_0  
prompt_toolkit            3.0.3                      py_0  
python                    3.7.6                h0371630_2  
```
If I downgrade to ipython=5.8.0 and prompt_toolkit=1.0.15, I get the desired behavior. So this is a good workaround for now, but I'd like to be able to stay up to date, or at least understand how to configure this behavior.

thanks!
