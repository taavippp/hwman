import unittest

from controller.TerminalController import TerminalController

#should i even try here? technically most of the code is tested
class TerminalControllerTests(unittest.TestCase):
    terminal: TerminalController = TerminalController(True)