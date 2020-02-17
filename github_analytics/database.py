import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file

    :param db_file:       database file
    :return:              connection object or None

    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

    except Error as e:
        raise e

    return conn


def insert_row(conn, sql, data_tuple):
    """Insert row into database using tuple and advance row.

    :param conn:            Database connection object
    :param sql:             SQL string containing insert statement
    :param data_tuple:      Tuple with data matching input SQL requirements

    :return:                Last row id

    """

    cur = conn.cursor()
    cur.execute(sql, data_tuple)

    return cur.lastrowid


def update_row(conn, sql, data_tuple):
    """Update row in database using tuple and commit.

    :param conn:            Database connection object
    :param sql:             SQL string containing insert statement
    :param data_tuple:      Tuple with data matching input SQL requirements

    """

    cur = conn.cursor()
    cur.execute(sql, data_tuple)
    conn.commit()
