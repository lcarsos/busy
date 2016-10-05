"""
Simple function to ensure that the database exists, and then return the Sqlite
connection
"""

import logging
import os.path as op
import sqlite3

from busy import db_schema_version

log = logging.getLogger(__name__)


def get_database(location):
    """Run some pre-checks then make a connection to the database"""
    ensure_database_exists(location)
    conn = sqlite3.connect(location)

    c = conn.cursor()
    c.execute('SELECT version FROM schema_version LIMIT 1')
    ver = tuple(c.fetchone())[0]
    if ver != db_schema_version:
        log.warning('Your busy database is out of date')

    return conn


def ensure_database_exists(location):
    """
    Make sure the database file exists. If it doesn't create it and make sure
    it is on the latest schema.
    """
    if op.exists(location):
        return
    conn = sqlite3.connect(location)
    try:
        script = op.join(op.dirname(op.abspath(op.dirname(__file__))), 'sql/busy.sql')
        script_text = []
        with open(script, 'r') as f:
            script_text = f.read()
        conn.executescript(script_text)
    finally:
        conn.close()
