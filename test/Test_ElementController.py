from datetime import datetime
import unittest

from controller.ElementController import ElementController
from controller.FileController import FileController
from model.HomeworkElement import HomeworkElement
from model.Progress import Progress

class ElementControllerTests(unittest.TestCase):
    reader: FileController = FileController("test/TESTDATA.csv")
    controller: ElementController = ElementController(reader.read_data())
    element: HomeworkElement = HomeworkElement(
        datetime(2022, 9, 19), "Hello", "World", Progress.STARTED
    )

    def test_ElementController_add(self):
        self.controller = ElementController(self.reader.read_data())
        self.assertEqual(len(self.controller.data), 3)
        self.controller.add(self.element)
        self.assertEqual(len(self.controller.data), 4)
    
    def test_ElementController_is_valid_value(self):
        self.assertTrue(
            self.controller._is_valid_value("date", self.element.date)
        )
        self.assertTrue(
            self.controller._is_valid_value("progress", self.element.progress)
        )
        self.assertTrue(
            self.controller._is_valid_value("course", self.element.course)
        )
        self.assertTrue(
            self.controller._is_valid_value("info", self.element.info)
        )
    
    def test_ElementController_edit(self):
        self.assertEqual(self.controller.data[1].course, "Course Two")
        self.controller.edit(1, "course", "Test Value")
        self.assertEqual(self.controller.data[1].course, "Test Value")

        self.assertEqual(self.controller.data[1].date, datetime(2020, 3, 19, 5, 45))
        self.controller.edit(1, "date", datetime(2022, 4, 20))
        self.assertEqual(self.controller.data[1].date, datetime(2022, 4, 20))
    
    def test_ElementController_remove(self):
        self.controller = ElementController(self.reader.read_data())
        self.assertEqual(len(self.controller.data), 3)
        self.controller.remove(2)
        self.assertEqual(len(self.controller.data), 2)

    def test_ElementController_find(self):
        self.controller = ElementController(self.reader.read_data())
        result = self.controller.find("info", "No info")
        self.assertEqual(len(result), 1)
        result = self.controller.find("date", datetime(2022, 4, 20))
        self.assertEqual(len(result), 0)
    
    def test_ElementController_sort_by_date(self):
        self.controller = ElementController(self.reader.read_data())
        self.assertEqual(self.controller.data[2].course, "Course Three")
        self.controller.sort("date")
        self.assertEqual(self.controller.data[0].course, "Course Three")