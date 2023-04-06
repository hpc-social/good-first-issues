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
REPOS_FILE = os.environ.get("REPOS_FILE", ".github/repos.txt")
ISSUE_LABEL = os.environ.get("ISSUE_LABEL", "good first issue")

if not REPOS_FILE:
    sys.exit(f"{REPOS_FILE} must be defined.")

if not os.path.exists(REPOS_FILE):
    sys.exit(f"{REPOS_FILE} does not exist.")


def read_file(filename):
    with open(filename, "r") as filey:
        lines = filey.readlines()
    return lines


# Assume that repos without good first issues we won't check again
EMPTY_REPOS = os.environ.get("EMPTY_REPOS", ".github/empty.txt")
empty = set()

if os.path.exists(EMPTY_REPOS):
    empty = read_file(EMPTY_REPOS)
    empty = set([x.strip() for x in empty if x.strip()])

token = os.environ.get("GITHUB_TOKEN")
if not token:
    sys.exit("Please export GITHUB_TOKEN")

# Read in the repos file
lines = read_file(REPOS_FILE)

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
response = requests.get("https://rseng.github.io/web/api/data.json")
if response.status_code != 200:
    sys.exit(f"Issue getting RSEpdeia data: {res.reason}")
listing = response.json()

# Find repos with good first issue label
for repo in listing:

    url = repo["url"]

    # Only GitHub supported, and skip those we've added
    # We can do a cleanup later if the action has too many
    if "gitlab" in url or url in repos or url in empty:
        print(f"Skipping {url}")
        continue

    uid = "/".join(url.split("/")[-2:])

    # This will return the first
    response = requests.get(api_base.format(repo=uid), headers=headers, params=data)
    if response.status_code in [301, 302, 404]:
        print(f"Repository {url} is moved.")
        continue

    elif response.status_code != 200:
        print("Error with response %s: %s" % (response.status_code, response.reason))
        time.sleep(60)
        continue

    issues = response.json()
    if not issues:
        print(f"Repository {url} has no issues.")
        empty.add(url)
        continue
    print(f"Found repository with good first issues {uid}")
    repos.add(url)


# Save repository!
with open(REPOS_FILE, "w") as fd:
    fd.write("\n".join(list(repos)))

# Save repository!
with open(EMPTY_REPOS, "w") as fd:
    fd.write("\n".join(list(empty)))
