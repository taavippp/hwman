from datetime import date, datetime
import unittest

from controller.FileController import FileController
from model.Progress import Progress

class FileControllerTests(unittest.TestCase):
    data_control: FileController = FileController("test/TESTDATA.csv")
    names: tuple = ("Course One", "Science")

    config_control: FileController = FileController("test/TESTCONFIG.json")

    def get_data(self):
        return self.data_control.read_data()

    def test_FileController_read_data_len(self):
        data = self.get_data()
        self.assertEqual(len(data), 3)
    
    def test_FileController_read_data(self):
        data = self.get_data()
        self.assertTrue(data[0].course in self.names)
        self.assertEqual(data[1].progress, Progress.NONE)
        self.assertEqual(data[2].info, "No info again")
    
    def test_FileController_write_data(self):
        data = self.get_data()
        new_value = self.names[1] if (data[0].course == self.names[0]) else self.names[0]
        data[0].course = new_value
        self.data_control.write_data(data)
        data = self.get_data()
        self.assertEqual(data[0].course, new_value)

    def test_FileController_read_config(self):
        config = self.config_control.read_config()
        keys = list(config.keys())
        print(keys)
        self.assertTrue("file" in keys)
        self.assertTrue("date_opened" in keys)
        self.assertTrue("reminders" in keys)
        self.assertEqual(config["file"], "test/TESTDATA.csv")
        self.assertEqual(config["date_opened"], date.today().strftime("%d-%m-%Y"))
        self.assertEqual(config["reminders"], True)
    
    def test_FileController_write_config(self):
        config = self.config_control.read_config()
        config["file"] = "MICHAEL.json"
        self.config_control.write_config(config)
        
        config = self.config_control.read_config()
        self.assertEqual(config["file"], "MICHAEL.json")
        config["file"] = "test/TESTDATA.csv"
        self.config_control.write_config(config)