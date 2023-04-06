---
tags: ,GUI,enhancement
title: "Filebrowser improvements"
html_url: "https://github.com/LiberTEM/LiberTEM/issues/83"
user: sk1p
repo: LiberTEM/LiberTEM
---

- [x] recent files / recent directories (could also remember the dataset parameters)
- [x] better convey status: disable file browser UI while loading directory listing (important for high latency situations)
- [x] Separate "Up" icon, not just the ".." directory since that is unfamiliar to Windows users.
- [ ] "Back" and "Forward" icon
- [x] Configurable shortcuts to common directories with user data
- [x] Input window for path to type or copy&paste the path
- [x] Display general metadata -- size, creation date, update date, owner, ...
- [ ] Display specific metadata, for example from known HDF5 dialects or sidecars
- [ ] Use the available screen space efficiently. Right now it uses only part of the screen.
- [x] Windows drives list

Edit: Removed obsolete HDFS