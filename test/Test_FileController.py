from model.Enums import Progress
from controller.FileController import FileController
import unittest

class FileControllerTests(unittest.TestCase):
    controller: FileController = FileController("test/TEST.csv")
    names: tuple = ("Course One", "Science")

    def test_FileController_read_len(self):
        data = self.controller.read_data()
        self.assertEqual(len(data), 3)
    
    def test_FileController_read_values(self):
        data = self.controller.read_data()
        self.assertTrue(data[0].course in self.names)
        self.assertEqual(data[1].progress, Progress.NONE)
        self.assertEqual(data[2].info, "No info again")
    
    def test_FileController_write_values(self):
        def set_data():
            return self.controller.read_data()
        data = set_data()
        new_value = self.names[1] if (data[0].course == self.names[0]) else self.names[0]
        data[0].course = new_value
        self.controller.write_data(data)
        data = set_data()
        self.assertEqual(data[0].course, new_value)