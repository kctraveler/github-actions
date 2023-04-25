# Overview
Project 4 for Software Quality and Testing course. Use GitHub actions for Continuous Integration and reporting test coverage as a status badge.

## About the code
- Implementation of a simple stack data structure and related unit test to provide a sample project for using GitHub actions and CI.
- We are using the built in python unittest package as well as PyTest for the initial testing framework
- Github Status Badges act as funcionality to show the Repositories workflow Status. Whether a paticular workflow is passing, failing or the statistics of the workflow.

- The code coverage badge shows the percentage of the source code that is covered by the test suite in "test_stack.py". High code coverage means that most of the code is executed during testing, meaning that it will possess a low chance of containing undetected bugs or issues:<br />
[![Coverage Status](https://coveralls.io/repos/github/kctraveler/github-actions/badge.svg)](https://coveralls.io/github/kctraveler/github-actions)

  [![Linux Build](https://github.com/kctraveler/github-actions/actions/workflows/python-app.yml/badge.svg)](https://github.com/kctraveler/github-actions/actions/workflows/python-app.yml)
  
- The codefactor badge highlights the CodeFactor tool that allows for the automation of the repository's code quality to facilitate better quality software. It does this by automatically reviewing/tracking every commit and pull request; providing actionable feedback and fixes for issues:<br /> 
  [![CodeFactor](https://www.codefactor.io/repository/github/kctraveler/github-actions/badge)](https://www.codefactor.io/repository/github/kctraveler/github-actions)

- The maintainability badge shows the capability of the master code to be changed, reused or repurposed without damaging the strucutre of the codebase. This also includes keeping any dependencies of the master code branch stable:<br />
 [![Maintainability](https://api.codeclimate.com/v1/badges/bb0ae3e1e2bf2f756edc/maintainability)](https://codeclimate.com/github/kctraveler/github-actions/maintainability)

- The commit activity badge shows the number of commits pushed to the current repo based on a specific time period. At the moment, 28 commits per month:<br />
 ![Commit Activity](https://img.shields.io/github/commit-activity/m/kctraveler/github-actions)

- The code size badge shows the total data size of the current repository:<br />
 ![Code Size](https://img.shields.io/github/languages/code-size/kctraveler/github-actions)


