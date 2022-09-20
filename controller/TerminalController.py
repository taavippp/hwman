from datetime import datetime
from rich import print

from controller.ElementController import ElementController
from controller.ConfigController import ConfigController
from controller.FileController import FileController
from model.HomeworkElement import HomeworkElement
from model.Progress import Progress

class TerminalController:
    """Class that handles everything related to the terminal."""

    testing: bool
    data_file: FileController
    conf_file: FileController
    config: ConfigController
    data: ElementController

    def __init__(self, testing: bool = False) -> None:
        self.testing = testing
        self.conf_file = FileController("CONFIG.json")
        if (testing):
            self.conf_file = FileController("test/TESTCONFIG.json")
        
        self.config = ConfigController(self.conf_file.read_config())
        self.load(
            self.config.get_all()["file"]
        )

    def load(self, path) -> None:
        """Loads a new file and its elements."""
        self.data_file = FileController(
            path
        )
        self.data = ElementController(
            self.data_file.read_data()
        )
        print(
            "Loaded file: [blue]{}[/blue]".format(path)
        )

    def save(self) -> None:
        """Saves all elements to the loaded file."""
        self.data_file.write_data(
            self.data.get_all()
        )

    def info(self) -> None:
        """Displays information about the program."""
        print(
            "File: [blue]{}[/blue]".format(
                self.data_file.path
            ),
            "Elements: [blue]{}[/blue]".format(
                len(self.data.get_all())
            ),
            "Test mode: [blue]{}[/blue]".format(
                str(self.testing).lower()
            )
        )
    
    def add(self, datestr: str, course: str, info: str, progress: int) -> None:
        """Adds new element to the list."""
        date: datetime
        try:
            date = datetime.strptime(datestr, "%d.%m.%Y %H:%M")
        except:
            date = datetime.strptime(datestr, "%d.%m.%Y")

        element = HomeworkElement(
            date,
            course,
            info,
            Progress(progress)
        )
        self.data.add(
            element
        )
        print(
            "Added new homework: [blue]{}[/blue]".format(course)
        )