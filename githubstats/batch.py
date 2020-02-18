from githubstats.clones import Clones
from githubstats.views import Views
from githubstats.organization import Organization


class Batch:
    """Batch update all tables in a target database for all repositories in an organization.

    :param organization:    GitHub organization name
    :param username:        GitHub user name
    :param token:           GitHub Personal access token
    :param target_db:       Full path with file name and extension to the target SQLite3 database

    USAGE:
    ```
    from githubstats import Batch

    organization = 'JGCRI'
    token = '<your token here>'
    username = '<your user name here>'
    target_db = '<your SQLite3 database here>'

    # instantiate Clones
    batch = Batch(organization, username, token, target_db)

    # update all tables in the target database for all repositories in an organization
    batch.update_for_all_repos()
    ```

    """

    def __init__(self, organization, username, token, target_db):

        # get a list of all repositories in the target organization
        self.repo_list = Organization(organization, username, token).list_repos_in_org()

        self.organization = organization
        self.username = username
        self.token = token
        self.target_db = target_db

    def update_for_all_repos(self):
        """Update all tables in the target database for all repositories in the organization."""

        for repository in self.repo_list:

            print("Processing repository:  {}".format(repository))

            # instantiate Clones
            clones = Clones(self.organization, repository, self.username, self.token, self.target_db)

            # archive clone data
            clones.archive()

            # instantiate Views
            views = Views(self.organization, repository, self.username, self.token, self.target_db)

            # archive data
            views.archive()
