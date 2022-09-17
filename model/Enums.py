from enum import Enum

class Day(Enum):
    """Enum that represents different days of the week."""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class Progress(Enum):
    """Enum that represents different states of completion."""
    NONE = 0
    STARTED = 1
    DONE = 2