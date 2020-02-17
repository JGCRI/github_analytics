import os
import requests

import github_analytics.utils as u
import github_analytics.database as db


class Clones:
    """Download and update the `clones` table in the target database.

    :param organization:    GitHub organization name
    :param repository:      GitHub repository name
    :param username:        GitHub user name
    :param token:           GitHub Personal access token
    :param target_db:       Full path with file name and extension to the target SQLite3 database

    USAGE:
    ```
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

    See the GitHub Developer Traffic REST API v3:  https://developer.github.com/v3/repos/traffic/

    """

    GITHUB_API = 'https://api.github.com'

    def __init__(self, organization, repository, username, token, target_db):

        # full path with filename and extension to the target SQLite3 database
        self.target_db = target_db

        self.repository = repository

        # construct URL to get the clones traffic data from a specific repository
        url = os.path.join(Clones.GITHUB_API, 'repos', organization, self.repository, 'traffic', 'clones')

        # create a datetime string for the current datetime
        self.download_dt = u.get_download_datetime()

        # get timestamped data about each clone
        self.response = requests.get(url, auth=(username, token)).json()['clones']

        # SQL for inserting a row into the SQLite3 database
        self.insert_sql = "INSERT INTO clones(date_time, uniques, totals, download_dt, repo_name) VALUES(?,?,?,?,?)"

        # SQL for updating a row in the SQLite3 database
        self.update_sql = """UPDATE clones
                                SET uniques = ?,
                                    totals = ?,
                                    download_dt = ?
                                WHERE repo_name = ? 
                                    AND date_time = ?"""

        # SQL for returning the unique and total records for a target date_time
        self.select_sql = """SELECT uniques, totals 
                    FROM clones
                    WHERE repo_name = '{}' AND date_time = '{}';"""

    def sql_to_dict(self, conn, date_time):
        """Get records in current table as a dictionary."""

        cur = conn.cursor()
        cur.execute(self.select_sql.format(self.repository, date_time))

        values = cur.fetchall()

        # return empty dictionary if there are no values for a datetime present
        if len(values) == 0:
            return {}

        else:
            return {'unique': values[0][0], 'count': values[0][1]}

    def archive(self):
        """Either insert or update the data currently in the `clones` table of the target SQLite3 database."""

        # create a database connection
        conn = db.create_connection(self.target_db)

        with conn:

            # for each record in clones Google API response
            for record in self.response:

                date_time = u.convert_google_time(record['timestamp'])
                n_count = record['count']
                n_unique = record['uniques']

                # get data currently in `clones` table
                table_data = self.sql_to_dict(conn, date_time)

                # if no data was present for the current date_time, add the new entry
                if bool(table_data) is False:
                    db.insert_row(conn, self.insert_sql, (date_time, n_unique, n_count, self.download_dt, self.repository))

                # if the date_time is in the database, update to new vals if different
                else:
                    db.update_row(conn, self.update_sql, (n_unique, n_count, self.download_dt, self.repository, date_time))

            conn.commit()
