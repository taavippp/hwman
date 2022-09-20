from dataclasses import dataclass
from datetime import datetime

from model.HomeworkElement import HomeworkElement
from model.Progress import Progress

@dataclass
class ElementController:
    """Class for managing and manipulating HomeworkElements at runtime."""
    data: list[HomeworkElement]

    def get_all(self) -> list[HomeworkElement]:
        return self.data

    def add(self, element: HomeworkElement) -> None:
        self.data.append(element)
    
    def edit(self, index: int, param: str, value: datetime | str | Progress) -> None:
        if not (self._is_valid_value(param, value)):
            raise TypeError("Invalid parameter(s) given.")
        vars(self.data[index])[param] = value
    
    def remove(self, index: int) -> None:
        self.data.pop(index)
    
    def find(self, param: str, value: datetime | str | Progress) -> list[HomeworkElement]:
        if not (self._is_valid_value(param, value)):
            raise TypeError("Invalid parameter(s) given.")
        return list(filter(
            lambda element: (vars(element)[param] == value), self.data
        ))
    
    def sort(self, param: str) -> None:
        self.data.sort(key = lambda element: (vars(element)[param]))
        
    def _is_valid_value(self, param: str, value: datetime | str | Progress) -> bool:
        if not (
        (param == "date" and isinstance(value, datetime)) or
        (param == "progress" and isinstance(value, Progress)) or
        (isinstance(value, str))
        ):
            return False
        return True