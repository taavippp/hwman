from model.Enums import Progress
from controller.DataManager import DataManager
import unittest

class DataManagerTests(unittest.TestCase):
    manager: DataManager = DataManager("test/TEST.csv")
    names: tuple = ("Course One", "Science")

    def test_DataManager_read_len(self):
        data = self.manager.read_data()
        self.assertEqual(len(data), 3)
    
    def test_DataManager_read_values(self):
        data = self.manager.read_data()
        self.assertTrue(data[0].course in self.names)
        self.assertEqual(data[1].progress, Progress.NONE)
        self.assertEqual(data[2].info, "No info again")
    
    def test_DataManager_write_values(self):
        def set_data():
            return self.manager.read_data()
        data = set_data()
        new_value = self.names[1] if (data[0].course == self.names[0]) else self.names[0]
        data[0].course = new_value
        self.manager.write_data(data)
        data = set_data()
        self.assertEqual(data[0].course, new_value)