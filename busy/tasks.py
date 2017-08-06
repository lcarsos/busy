"""A Task is a unit of organization in Busy"""

def create_task():
    pass


class Task:
    """
    A Task keeps track of a thing that has to get done. "Things" are very
    complex, Busy calls them tasks. Some Tasks cannot be started until other
    Tasks are completed, that task is "waiting on" those other tasks, some
    would call it "blocked". Some Tasks cannot be completed until other tasks
    are completed, those are children tasks. They come up when you put
    something on your todo list and realize there are several steps to getting
    that "one" task done, and you need/want to track that.
    """
    def __init__(self, id):
        self._id = id

    def created(self):
        pass

    def started(self):
        pass

    def completed(self):
        pass

    def name(self):
        pass

    def description(self):
        pass

    def tags(self):
        pass

    def expected_time(self):
        pass

    def remaining_time(self):
        pass

    def story_points(self):
        pass

    def is_complete(self):
        pass

    # Tasks related to this Task
    def waiting_on(self):
        pass

    def blocking(self):
        pass

    def parents(self):
        pass

    def children(self):
        pass

    # Work done for this task
    def timers(self):
        """Timers directly related to this task"""
        pass

    def all_timers(self):
        """Include timers on children"""
        pass
