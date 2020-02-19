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

## Generate a CSV file for the number of unique clones for each repository in the target database

```python
from githubstats import Reports

# instantiate reports class
rpt = Reports("<full path with file name and extension to your SQLite3 database>")

# generate a CSV file containing the number of unique clones for each repository in the database
df = rpt.unique_clones_by_repository('clones', output_csv="<full path with file name and extension to your output CSV file>")
```
