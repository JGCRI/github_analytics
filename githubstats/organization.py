import os
import requests


class Organization:
    """Download and process GitHub metadata for an organization.

    :param organization:    GitHub organization name
    :param username:        GitHub user name
    :param token:           GitHub Personal access token

    USAGE:
    ```
    organization = 'JGCRI'
    token = '<your token here>'
    uname = '<your user name here>'

    # instantiate Organization
    org = Organization(organization, uname, token)

    # list all repositories in an organization
    org.list_repos_in_org()
    ```

    """

    GITHUB_API = 'https://api.github.com'

    # number of records to return for a page, this is set high because we want to make sure we get all repositories
    PAGE_LIMIT = 1000

    def __init__(self, organization, username, token):

        self.org = organization
        self.username = username
        self.token = token

    def list_repos_in_org(self):
        """Generate a list of all repository names for an organization.

        See:  https://developer.github.com/v3/repos/#list-organization-repositories

        """

        # construct URL to get the clones traffic data from a specific repository
        url = os.path.join(Organization.GITHUB_API, 'orgs', self.org, 'repos?per_page={}'.format(Organization.PAGE_LIMIT))

        # conduct get to GitHub API
        response = requests.get(url, auth=(self.username, self.token))

        return [i['name'] for i in response.json()]
