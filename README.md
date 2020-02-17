# github_analytics
Mine and archive GitHub repositories for insight analytics

## Get started with `github_analytics`

## Build your archival database
After installing `github_analytics` you can build the necessary SQLite3 database by running in a Python prompt:

```python
from github_analytics import BuildDatabase

BuildDatabase("<path to your desired new database with a .db extension>")
```

## Mine and archive clone related insights data from GitHub for a repository

```python
from github_analytics import Clones

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

