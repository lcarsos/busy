"""Execute busy"""

import os
import os.path as op
import logging

from busy.args import parser
from busy.database import get_database


def main(args):
    """Get set up and run the prorgram"""
    busy_args = parser.parse_args(args)
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(busy_args)

    busy_dir = op.expanduser('~/.busy')

    if not op.exists(busy_dir):
        logging.info('making busy directory')
        os.mkdir(busy_dir)

    conn = get_database(op.join(busy_dir, 'database.db'))
    print('done')
    conn.close()
