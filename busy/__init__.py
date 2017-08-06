"""Declaring busy as a package"""

import sys

numversion = (0, 0, 1)
version = ".".join([str(num) for num in numversion])
db_schema_version = 1


# pylint: disable=missing-docstring
def run_busy():
    from busy.busy import main
    main(sys.argv[1:])
