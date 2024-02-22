#!/bin/bash

import json
import os
import requests
import sys
import time
import shlex
import subprocess

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(here))
print("Present working directory is %s" % here)
api_base = "https://api.github.com/repos/{repo}/issues"
api_topic_base = "https://api.github.com/repos/{repo}/topics"

# GitHub Workflow - we get variables from environment
REPOS_FILE = os.path.join(root, ".github", "repos.txt")
ISSUE_LABEL = os.environ.get("ISSUE_LABEL", "good first issue")
COLLECTION_FOLDER = os.environ.get("COLLECTION_FOLDER", "_issues")
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

# Documentation base is located at docs
# This is expected to be run in a GitHub action
docs_dir = os.path.join(root, "docs")
output_dir = os.path.join(docs_dir, COLLECTION_FOLDER)

# Print metadata for user
print("Issue label: [%s]" % ISSUE_LABEL)
print("Collection output folder: [%s]" % output_dir)

if not os.path.exists(output_dir):
    os.mkdir(output_dir)


def check_response(response):
    """
    Ensure a response is 200 (successful)
    """
    if response.status_code != 200:
        print(
            "Issue with %s, response %s: %s, sleeping"
            % (response.url, response.status_code, response.reason)
        )
        time.sleep(60)
        return False
    return True


def get_repository_topics(repo):
    """
    Use the repository topics URL to get a list of topic tags
    """
    url = api_topic_base.format(repo=repo)
    response = requests.get(url, headers=headers, params=data)
    if not check_response(response):
        return []
    return response.json().get("names") or []


def unique(listing):
    """
    Ensure a list is unique.
    """
    return list(set(listing))


def run_command(cmd, stream=False):
    """
    use subprocess to send a command to the terminal.

    Parameters
    ==========
    cmd: the command to send
    """
    if not isinstance(cmd, list):
        cmd = shlex.split(cmd)

    stdout = subprocess.PIPE if not stream else None
    output = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=stdout)

    t = output.communicate()[0], output.returncode
    output = {"message": t[0], "return_code": t[1]}

    if isinstance(output["message"], bytes):
        output["message"] = output["message"].decode("utf-8")

    return output


def generate_markdown(line):
    """
    Generate markdown for a repo / tags
    """
    # Extra tags are optional, separated by comma
    extra_tags = ""
    try:
        repo, extra_tags = line.strip().split(" ")
    except ValueError:
        repo = line.strip()

    extra_tags = extra_tags.split(",")
    repo = "/".join(repo.split("/")[-2:])
    topics = get_repository_topics(repo)
    url = api_base.format(repo=repo)

    print("Looking up issues for %s" % repo)

    # This will return the first
    response = requests.get(url, headers=headers, params=data)
    if not check_response(response):
        return None, None

    issues = response.json()

    # For each issue, write a markdown file
    for issue in issues:
        date = issue["created_at"].split("T")[0]
        basename = "%s-%s-%s.md" % (date, repo.replace("/", "-"), issue["number"])
        filename = os.path.join(output_dir, basename)
        # Add front matter for Jekyll
        content = "---\n"

        # Add labels as tags
        tags = unique([x["name"] for x in issue["labels"]] + topics)
        if ISSUE_LABEL in tags:
            tags.remove(ISSUE_LABEL)

        if extra_tags:
            tags = unique(tags + extra_tags)
        if tags:
            tags = [x.replace(":", "").replace(" ", "-") for x in tags]
            tags = [x for x in tags if x]
            tags.sort()
            if tags:
                print("Adding tags %s" % ",".join(tags))
                tags = [f'"{tag}"' for tag in tags]
                content += "tags: [%s]\n" % (",".join(tags))

        # Don't include body!

        # Title must have quotes escaped
        content += "title: %s\n" % json.dumps(issue["title"])
        content += 'html_url: "%s"\n' % issue["html_url"]
        content += 'user: "%s"\n' % (issue["user"]["login"])
        content += 'repo: "%s"\n' % repo
        content += "---\n\n"

        # Try building
        try:
            print(content)
        except:
            print(
                f'Skipping issue {issue["number"]} of {repo}, cannot parse illegal characters.'
            )
            continue
        yield filename, content


# Load repos
for line in lines:
    # Try writing and building each, do not keep ones that don't build
    for filename, content in generate_markdown(line):
        if not filename or not content:
            continue
        with open(filename, "w") as filey:
            filey.writelines(content)

        # This isn't perfect, but it ensures we do not add content that won't build
        os.chdir(docs_dir)
        p = run_command(["bundle", "exec", "jekyll", "build"])
        if p["return_code"] != 0:
            print(f"Issue with building {filename}, removing")
            os.remove(filename)
        os.chdir(here)

count = os.listdir(output_dir)
print(f"Found {count} total issues.")
