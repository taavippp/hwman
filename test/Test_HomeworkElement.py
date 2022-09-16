from model.Enums import Day, Progress
from model.HomeworkElement import HomeworkElement
import unittest

class HomeworkElementTests(unittest.TestCase):
    element: HomeworkElement = HomeworkElement(Day.MONDAY, "Thing", "Information", Progress.NONE)

    def test_day_is_DayEnum_Monday(self):
        self.assertEqual(self.element.day, Day.MONDAY)

    def test_day_to_string_is_Monday(self):
        self.assertEqual(self.element.day_to_string(), "Monday")
    
    def test_progress_is_ProgressEnum_None(self):
        self.assertEqual(self.element.progress, Progress.NONE)
    
    def test_progress_to_string_is_None(self):
        self.assertEqual(self.element.progress_to_string(), "None")
    
    def test_element_to_list(self):
        self.assertEqual(
            self.element.to_list(),
            list([
                1,
                "Thing",
                "Information",
                0
            ])
        )

class EnumsTests(unittest.TestCase):
    day: Day = Day(5)
    progress: Progress = Progress(2)

    def test_day_value(self):
        self.assertEqual(self.day.value, 5)
    
    def test_day_name(self):
        self.assertEqual(self.day.name, "FRIDAY")
    
    def test_progress_value(self):
        self.assertEqual(self.progress.value, 2)
    
    def test_progress_name(self):
        self.assertEqual(self.progress.name, "DONE")

#from terminal:
#py -m unittest test.Test_HomeworkElement
if __name__ == "__main__":
    unittest.main()