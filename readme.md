# GitHub Repo Email Scraper

### Description:
  Scrape emails of contributors who work on identified open source projects (helpful in automating sourcing for talent acquisition teams)

### Usage:
* Update the `username`and `key` variables at the top of [scraper.py](https://github.com/aharshbe/github_repo_email_scraper/blob/main/scraper.py) to include your username (handle) and personal [GitHub access token](https://github.com/settings/tokens). To create a new token click "Personal access tokens" then click "Generate new token"
* Update the `search` variable with the repo you'd like to search, follow the format org/repo
* `python3 scraper.py`

### Requirements:
* python3
* requests module
* a GitHub personal access token

### Assumptions/Considerations:
* This will only obtain emails of contributors to repos who sign their commits with an email (it is worth mentioning almost every developer does this for various reasons)
* You must have access to a GitHub account in order to create your access token (you can query GitHub's API without it but you will almost immediately be rate limited)
* This tool works best when you pair it with thoughtful searches through GitHub repos that you identify as valuable in your sourcing, i.e., search open source repos that use a programming language or framework that is useful to your organization, etc
* This currently only obtains the top 30 contributors of any given repo (may update this to paginate in the future). 30 good leads is a start though 😁

#### Author:
* me (aharshbe)
