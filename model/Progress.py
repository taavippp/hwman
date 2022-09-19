from enum import Enum

class Progress(Enum):
    """Enum that represents different states of completion."""
    NONE = 0
    STARTED = 1
    DONE = 2