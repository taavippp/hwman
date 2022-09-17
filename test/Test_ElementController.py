import unittest
from controller.ElementController import ElementController
from controller.FileController import FileController
from model.Enums import Day, Progress
from model.HomeworkElement import HomeworkElement

class ElementControllerTests(unittest.TestCase):
    reader: FileController = FileController("test/TEST.csv")
    controller: ElementController = ElementController(reader.read_data())
    element: HomeworkElement = HomeworkElement(
        Day.SATURDAY, "Hello", "World", Progress.STARTED
    )

    def test_ElementController_add(self):
        self.controller = ElementController(self.reader.read_data())
        self.assertEqual(len(self.controller.data), 3)
        self.controller.add(self.element)
        self.assertEqual(len(self.controller.data), 4)
    
    def test_ElementController_is_valid_value(self):
        self.assertTrue(
            self.controller._is_valid_value("day", self.element.day)
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
        self.assertEqual(self.controller.data[1].day, Day.WEDNESDAY)
        self.controller.edit(1, "day", Day.MONDAY)
        self.assertEqual(self.controller.data[1].day, Day.MONDAY)
    
    def test_ElementController_remove(self):
        self.controller = ElementController(self.reader.read_data())
        self.assertEqual(len(self.controller.data), 3)
        self.controller.remove(2)
        self.assertEqual(len(self.controller.data), 2)

    def test_ElementController_find(self):
        self.controller = ElementController(self.reader.read_data())
        result = self.controller.find("info", "No info")
        self.assertEqual(len(result), 1)
        result = self.controller.find("day", Day.THURSDAY)
        self.assertEqual(len(result), 0)