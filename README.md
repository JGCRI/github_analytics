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

