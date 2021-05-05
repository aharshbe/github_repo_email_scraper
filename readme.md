# GitHub Repo Email Scraper

### Description:
  Scrape emails of contributors who work on identified open source projects (helpful in automating sourcing for talent acquisition teams)

### Usage:
* Update the `username`and `key` variable at the top of [scraper.py](https://github.com/aharshbe/github_repo_email_scraper/blob/main/scraper.py) to include your username (handel) and personal [GitHub access token](https://github.com/settings/tokens). To create a new token click "Personal access tokens" then click "Generate new token"
* Update the `search` variable with the repo you'd like to search, follow the format org/repo
* `python3 scraper.py`

### Requirements:
* python3
* requests module
* a GitHub personal access token

#### Author:
* me (aharshbe)
