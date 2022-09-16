from model.Enums import Day, Progress
from model.HomeworkElement import HomeworkElement
from unittest import TestCase
import unittest

class MondayHomeworkElementTest(TestCase):
    element: HomeworkElement = HomeworkElement(Day.MONDAY, "", "", Progress.NONE)

    def day_is_DayEnum_Monday(self):
        self.assertEqual(self.element.day, Day.MONDAY, "Should be Day.MONDAY")

    def day_to_string_is_Monday(self):
        self.assertEqual(self.element.day_to_string(), "Monday", "Should be 'Monday'")

if __name__ == "__main__":
    unittest.main()