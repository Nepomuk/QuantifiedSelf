#!/usr/bin/env python
"""
Access the wordcount database. Possible actions: init, insert.
"""

import sqlite3 as sql
import os
import time
import argparse


def create_db(args):
    """Create an empty DB that will hold the wordcount entries."""
    database_name = args.database

    # check if the database already exists and if overwriting is disabled
    if os.path.isfile(database_name) and not args.overwrite_db:
        print "W: Database {0} already exists.".format(database_name)
        return

    # (re)create the database from scratch
    db_connection = sql.connect(database_name)
    with db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("DROP TABLE IF EXISTS wordcount")
        db_cursor.execute("CREATE TABLE wordcount (\
                time        INT PRIMARY KEY, \
                wc_count    INT, \
                perl_count  INT, \
                tex_count   INT \
            )")
        print "Database {0} created.".format(database_name)


def insert_into(args):
    """Insert data into the database."""
    db_connection = sql.connect(args.database)
    with db_connection:
        db_cursor = db_connection.cursor()
        if len(args.ac) == 3:
            input_values = [int(time.time()), args.ac[0], args.ac[1], args.ac[2]]
            db_cursor.execute("INSERT INTO wordcount VALUES (?,?,?,?)", input_values)


def parse():
    """Parse the program arguments."""
    parser = argparse.ArgumentParser(
        description='Access the database containing the wordcount entries.'
    )
    parser.add_argument(
        'command',
        choices=['init', 'insert'],
        help='Selects the command to execute.'
    )
    parser.add_argument(
        '-ac',
        nargs=3, type=int,
        metavar='N',
        help='[insert] The counts from all three methods in this order: \
            wc_count, perl_count, tex_count.'
    )
    parser.add_argument(
        '-db', '--database',
        default="wordcount.db",
        help='Path to the local SQlite3 database file.'
    )
    parser.add_argument(
        '--overwrite-db',
        action='store_true',
        help='[init] Overwrite the database if the file already exists.'
    )

    return parser.parse_args()


if __name__ == "__main__":
    ARGS = parse()

    if ARGS.command == 'init':
        create_db(ARGS)
    elif ARGS.command == 'insert':
        if ARGS.ac == None or len(ARGS.ac) != 3:
            print "ERROR: Too few arguments!"
            print "Insert command needs three numbers as arguments of -ac (wc_count, pearl_count, tex_count)."
        else:
            insert_into(ARGS)
