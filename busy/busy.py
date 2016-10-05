"""Execute busy"""

import os
import os.path as op

from busy.database import get_database


def main(args):
    """Get set up and run the prorgram"""
    busy_dir = op.expanduser('~/.busy')

    if not op.exists(busy_dir):
        os.mkdir(busy_dir)

    conn = get_database(op.join(busy_dir, 'database.db'))
    print('done')
    conn.close()
