[![Build Status](https://travis-ci.org/JGCRI/githubstats.svg?branch=master)](https://travis-ci.org/JGCRI/githubstats)

# githubstats
Mine and archive GitHub repositories for insight analytics

## Get started with `githubstats`

## Build your archival database
After installing `githubstats` you can build the necessary SQLite3 database by running in a Python prompt:

```python
from githubstats import BuildDatabase

BuildDatabase("<path to your desired new database with a .db extension>")
```

## Mine and archive clone related insights data from GitHub for a repository

```python
from githubstats import Clones

organization = 'JGCRI'
repository = 'gcam-core'
token = '<your token here>'
uname = '<your user name here>'
target_db = '<your SQLite3 database here>'

# instantiate Clones
clones = Clones(organization, repository, uname, token, target_db)

# archive data
clones.archive()
```

## Mine and archive view related insights data from GitHub for a repository

```python
from githubstats import Views

organization = 'JGCRI'
repository = 'gcam-core'
token = '<your token here>'
uname = '<your user name here>'
target_db = '<your SQLite3 database here>'

# instantiate Views
views = Views(organization, repository, uname, token, target_db)

# archive data
views.archive()
```

## Update data for all repositories in an organization

```python
from githubstats import Batch

organization = 'JGCRI'
token = '<your token here>'
username = '<your user name here>'
target_db = '<your SQLite3 database here>'

# instantiate Batch
batch = Batch(organization, username, token, target_db)

# update all tables in the target database for all repositories in an organization
batch.update_for_all_repos()
```
