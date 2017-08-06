"""Separate the CLI args from being built in main"""

import argparse

from busy import version
from busy.commands import build_with_command

search_parameters = argparse.ArgumentParser(add_help=False)
search_parameters.add_argument('name', help="Name a task, if it exists and isn't complete, start logging to it")
search_parameters.add_argument('-t',
                               '--tag',
                               action='append',
                               help="Limit task name matching to only tasks with this tag")

parser = argparse.ArgumentParser(
    description='For people serious about todo lists')
parser.add_argument('-V',
                    '--version',
                    action='version',
                    version='%(prog)s v{}'.format(version))

subparsers = parser.add_subparsers()

busy_blank = subparsers.add_parser('',
                                   help='Start logging work, and later you can associate with a task')

busywith = subparsers.add_parser('with',
                                 parents=[search_parameters],
                                 help='Start logging work on a named task')
busywith.set_defaults(func=build_with_command)

busyon = subparsers.add_parser('on', help='Show what tasks are active right now')

busystop = subparsers.add_parser('stop',
                                 parents=[search_parameters],
                                 help='Stop working on an active task')
