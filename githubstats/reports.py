import pandas as pd

import githubstats.database as db


class Reports:
    """Generate reports from the database.

    :param target_db:       Full path with file name and extension to your SQLite3 database

    USAGE
    ```
    from githubstats import Reports

    # instantiate reports class
    rpt = Reports("<full path with file name and extension to your SQLite3 database>")

    # generate a CSV file containing the number of unique clones for each repository in the database
    df = rpt.unique_clones_by_repository('clones', output_csv="<full path with file name and extension to your output CSV file>")

    """

    def __init__(self, target_db):

        self.target_db = target_db

    def unique_clones_by_repository(self, table, output_csv=None):
        """Create an output data frame containing the total number of unique clones
         for all repositories in the database.  Output as CSV as an option.

         :param table:          target name of the table
         :param output_csv:     Full path to file name with extension for the output CSV; None by default.

         """

        sql = """SELECT 
                        DATE(date_time) as date, uniques, repo_name 
                    FROM {};""".format(table)

        # create database connection
        conn = db.create_connection(self.target_db)

        df = db.query_to_dataframe(sql, conn)

        # convert date field from string to datetime object
        df['date'] = pd.to_datetime(df['date'])

        grp = df.groupby('repo_name')
        min_date_dict = grp.min()['date'].to_dict()
        max_date_dict = grp.max()['date'].to_dict()
        sum_dict = grp.sum()['uniques'].to_dict()

        df['min_date'] = df['repo_name'].map(min_date_dict)
        df['max_date'] = df['repo_name'].map(max_date_dict)
        df['uniques'] = df['repo_name'].map(sum_dict)

        df.drop(columns=['date'], inplace=True)

        df = df.groupby('repo_name').min()

        df.reset_index(inplace=True)
        df.columns = ['repository', 'unique_{}'.format(table), 'min_date', 'max_date']

        if output_csv is not None:
            df.to_csv(output_csv, index=False)

        return df
