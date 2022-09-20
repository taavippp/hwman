import unittest

from controller.ConfigController import ConfigController
from controller.FileController import FileController

class ConfigControllerTests(unittest.TestCase):
    reader: FileController = FileController("test/TESTCONFIG.json")
    config: ConfigController = ConfigController(reader.read_config())

    def test_is_valid_var(self):
        self.assertTrue(self.config._is_valid_var("default_file", "test"))
        self.assertFalse(self.config._is_valid_var("default_file", 123))
        self.assertFalse(self.config._is_valid_var("reminders", list()))
        self.assertFalse(self.config._is_valid_var("test", True))

    def test_set_config(self):
        self.config.set("default_file", "test.json")
        self.assertEqual(self.config.config["default_file"], "test.json")
        self.config.set("reminders", False)
        self.assertFalse(self.config.config["reminders"])
        self.config.set("display_time_24", 123)
        self.assertEqual(self.config.config["display_time_24"], True, "Should not have set to 123.")