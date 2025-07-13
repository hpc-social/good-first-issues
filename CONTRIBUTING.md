# Contributing to Good First Issues

Thank you for your interest in contributing to the **Good First Issues** project! Whether you're a beginner or an experienced contributor, this repository is a great place to start. We welcome contributions of all kinds, and we appreciate your help in improving this project.

## Table of Contents

- [About](#about)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Submitting Code](#submitting-code)
  - [Documentation](#documentation)
  - [New Features](#new-features)
- [Getting Started](#getting-started)
  - [Cloning the Repository](#cloning-the-repository)
- [Project Workflow](#project-workflow)
  - [How to Add Repositories](#how-to-add-repositories)
  - [How to Add Good First Issues](#how-to-add-good-first-issues)
- [Community](#community)
- [Code of Conduct](#code-of-conduct)

## About

This repository is part of the **Good First Issues** initiative, designed to help new contributors find open source projects to get started with. If you have a project or community that offers "Good First Issues," simply add your repository to `.github/repos.txt` and any issue labeled with **Good First Issue** will automatically appear in the list.

We use automation with GitHub Actions to manage repositories and issues, making it easy for maintainers to add their projects to the initiative and for new contributors to find beginner-friendly issues.

## How to Contribute

We welcome contributions in various forms. Here are some ways you can contribute:

### Reporting Bugs

If you find a bug or encounter an issue while using this project, please report it by creating a GitHub issue. Be sure to include:

- A clear description of the problem.
- Steps to reproduce the issue.
- Any relevant logs or error messages.

### Submitting Code

If you're interested in fixing bugs, adding features, or improving the code, feel free to fork the repository and submit a pull request (PR). When submitting code, please:

- Ensure your code follows our style guide.
- Test your changes thoroughly before submitting.
- Provide a clear description of what your PR is addressing.

### Documentation

Documentation contributions are always welcome! If you notice areas where the documentation can be improved, feel free to suggest changes or submit a PR. This can include:

- Fixing typos or grammar mistakes.
- Improving explanations or examples.
- Adding new sections or clarifications.

### New Features

If you have an idea for a new feature or enhancement, please open an issue first to discuss it. Once the feature is approved, you can submit a PR with your implementation.

## Getting Started

To get started with development, you’ll first need to clone the repository to your local machine. You can do this using Git:

```bash
git clone https://github.com/hpc-social/good-first-issues.git
cd good-first-issues
```
## Getting Started

### Cloning the Repository

This repository includes two main automation scripts:

 - add-repos.py: Adds repositories to .github/repos.txt.
 - generate-first-issues.py: Generates and updates issues labeled "Good First Issue" based on the repositories listed.

To run the scripts locally:

```bash
python .github/scripts/add-repos.py
python .github/scripts/generate-first-issues.py
```

## Project Workflow

### How to Add Repositories

If you want to add your repository to the "Good First Issues" list, simply follow these steps:

- Open the .github/repos.txt file.
- Add your repository’s full name (e.g., username/repository-name).
- Commit and push your changes.
Once your repository is added, the action will automatically start pulling "Good First Issues" from your repository.

### How to Add Good First Issues

To have an issue marked as a "Good First Issue" in your repository, follow these steps:

- Label the issue with Good First Issue.
- Ensure the issue is beginner-friendly and has clear instructions.
- Submit the PR with the necessary modifications if required.

## Community

We encourage a friendly and respectful environment. Join us in our efforts to make open source more inclusive and welcoming. If you have any questions or need assistance, feel free to ask in the issues section.

### Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please take the time to read it and contribute in a respectful manner.