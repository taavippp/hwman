from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from model.Progress import Progress

@dataclass
class HomeworkElement:
    """Class that stores the information related to a single course's homework."""
    date: datetime
    course: str
    info: str
    progress: Progress

    class Weekday(Enum):
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 3
        THURSDAY = 4
        FRIDAY = 5
        SATURDAY = 6
        SUNDAY = 7

    def _format_date(self, chars: tuple) -> str:
        return self.date.strftime(
            "%d{0}%m{0}%Y %H{1}%M".format(chars[0], chars[1])
        )

    def date_to_weekday(self) -> str:
        return self.Weekday(
            self.date.isoweekday()
        ).name.title()

    def date_to_csv(self) -> str:
        return self._format_date(("-", ":"))

    def date_to_string(self) -> str:
        return self._format_date((".", ":"))

    def progress_to_string(self) -> str:
        return self.progress.name.title()

    def to_list(self) -> list:
        return list([
            self.date_to_csv(),
            self.course,
            self.info,
            self.progress.value
        ])