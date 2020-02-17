import sqlite3
from sqlite3 import Error

import github_analytics.database as db


class BuildDatabase:
    """Build an initial database and its schema.

    :param db_file:         Full path with file name and extension to a SQLite database with the.db extension.

    """

    def __init__(self, target_db):

        # create new db and connection
        self.conn = db.create_connection(target_db)

        # build clones table
        self.create_clones_table()

        self.conn.close()

    def create_table(self, sql):
        """Create new table in database.

        :param sql:         Create table SQL

        """
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def create_clones_table(self):
        """Create table for clones data information."""

        sql = """CREATE TABLE clones(
                    date_time TEXT NOT NULL,
                    uniques INT NOT NULL,
                    totals INT NOT NULL,
                    download_dt TEXT NOT NULL,
                    repo_name TEXT NOT NULL);"""

        self.create_table(sql)


if __name__ == '__main__':

    BuildDatabase('/Users/d3y010/Desktop/test.db')