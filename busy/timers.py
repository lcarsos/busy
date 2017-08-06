"""A Timer is a unit of work in Busy"""

from datetime import datetime


def create_timer(start_time, duration, tasks=[]):
    """Create a completed timer entry"""
    pass


def start_timer(start_time=datetime.now(), tasks=[]):
    """Create a new active timer"""
    pass


class Timer:
    """
    A timer keeps track of time. It knows when it was started, and when the
    timer is expired, it will know how long it went for. It also knows what
    tasks it logs time for.
    """

    def __init__(self, id):
        self.id = id

    # Timer information
    def started_on(self):
        pass

    def duration(self):
        pass

    def tasks(self):
        pass

    def is_complete(self):
        """Check if a timer has been completed"""
        pass

    # Timer actions
    def complete(self):
        pass
