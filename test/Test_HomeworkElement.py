from datetime import datetime, timedelta
import unittest

from model.HomeworkElement import HomeworkElement
from model.Progress import Progress

#py -m unittest test.Test_HomeworkElement
class HomeworkElementTests(unittest.TestCase):
    element: HomeworkElement = HomeworkElement(
        #May 3, 2022
        datetime(2022, 5, 3, 0, 0),
        "Thing",
        "Information",
        Progress.NONE
    )
    day: timedelta = timedelta(1)

    def weekday_to_str(self, weekday: int) -> str:
        return HomeworkElement.Weekday(weekday).name.title()

    def test_date_to_weekday(self):
        self.assertEqual(self.element.date_to_weekday(), "Tuesday")

    def test_date_to_string(self):
        self.assertEqual(self.element.date_to_string(), "[black]03.05.2022 00:00[/black]")
        new_date = datetime.now() + (self.day * 5)
        self.element.date = new_date
        self.assertEqual(
            self.element.date_to_string(),
            self.weekday_to_str(new_date.isoweekday())
        )
        new_date = datetime.now() + (self.day * 1)
        self.element.date = new_date
        self.assertEqual(
            self.element.date_to_string(),
            "[bold red]{}[/bold red]".format(
                self.weekday_to_str(new_date.isoweekday())
            )
        )
        self.element.date = datetime(2022, 5, 3)

    def test_date_to_csv(self):
        self.assertEqual(self.element.date_to_csv(), "03-05-2022 00:00")
    
    def test_progress_enum(self):
        self.assertEqual(self.element.progress, Progress.NONE)
    
    def test_progress_to_string(self):
        self.assertEqual(self.element.progress_to_string(), "None")
    
    def test_element_to_list(self):
        self.assertEqual(
            self.element.to_list(),
            [
                "03-05-2022 00:00",
                "Thing",
                "Information",
                0
            ]
        )