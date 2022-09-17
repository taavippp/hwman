from model.Enums import Day, Progress
from model.HomeworkElement import HomeworkElement
from dataclasses import dataclass

@dataclass
class ElementController:
    """Class for managing and manipulating HomeworkElements at runtime."""
    data: list[HomeworkElement]

    def add(self, element: HomeworkElement) -> None:
        self.data.append(element)
    
    def edit(self, index: int, param: str, value: Day | str | Progress) -> None:
        if not (self._is_valid_value(param, value)):
            raise TypeError("Invalid parameter(s) given.")
        vars(self.data[index])[param] = value
    
    def remove(self, index: int) -> None:
        self.data.pop(index)
    
    def find(self, param: str, value: Day | str | Progress) -> list[HomeworkElement]:
        if not (self._is_valid_value(param, value)):
            raise TypeError("Invalid parameter(s) given.")
        return list(filter(
            lambda element: (vars(element)[param] == value), self.data
        ))

    def _is_valid_value(self, param: str, value: Day | str | Progress) -> bool:
        if not (
        (param == "day" and isinstance(value, Day)) or
        (param == "progress" and isinstance(value, Progress)) or
        (isinstance(value, str))
        ):
            return False
        return True