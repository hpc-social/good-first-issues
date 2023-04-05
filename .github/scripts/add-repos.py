#!/bin/bash

import json
import os
import requests
import sys
import time

here = os.path.dirname(os.path.abspath(__file__))
print("Present working directory is %s" % here)
api_base = "https://api.github.com/repos/{repo}/issues"

# GitHub Workflow - we get variables from environment
REPOS_FILE = os.environ.get("REPOS_FILE", '.github/repos.txt')
ISSUE_LABEL = os.environ.get("ISSUE_LABEL", "good first issue")
if not REPOS_FILE:
    sys.exit(f"{REPOS_FILE} must be defined.")

if not os.path.exists(REPOS_FILE):
    sys.exit(f"{REPOS_FILE} does not exist.")

token = os.environ.get("GITHUB_TOKEN")
if not token:
    sys.exit("Please export GITHUB_TOKEN")

# Read in the repos file
with open(REPOS_FILE, "r") as filey:
    lines = filey.readlines()

# Must authenticate
headers = {"Authorization": f"token {token}"}
data = {"state": "open", "labels": ISSUE_LABEL}

# Print metadata for user
print("Issue label: [%s]" % ISSUE_LABEL)

# For this set of repos, too many for special tags!
repos = set()
for line in lines:

    # Extra tags are optional, separated by comma
    extra_tags = ""
    try:
        repo, extra_tags = line.strip().split(" ")
    except ValueError:
        repo = line.strip()
    repos.add(repo)

# Get current repos from rsepedia
response = requests.get('https://rseng.github.io/web/api/data.json')
if response.status_code != 200:
    sys.exit(f'Issue getting RSEpdeia data: {res.reason}')
listing = response.json()

# Find repos with good first issue label
for repo in listing:

    # Only GitHub supported, and skip those we've added
    # We can do a cleanup later if the action has too many
    if "gitlab" in repo['url'] or repo['url'] in repos:
        continue

    uid = "/".join(repo['url'].split("/")[-2:])
    url = api_base.format(repo=uid)

    # This will return the first
    response = requests.get(url, headers=headers, params=data)
    if response.status_code in [301, 302, 404]:
        continue

    elif response.status_code != 200:
        print("Error with response %s: %s" % (response.status_code, response.reason))
        time.sleep(60)
        continue 
               
    issues = response.json()
    if not issues:
        continue
    print(f'Found repository with good first issues {uid}')
    repos.add(f"https://github.com/{uid}")


# Save repository!
with open(REPOS_FILE, "w") as fd:
    fd.write("\n".join(list(repos)))
