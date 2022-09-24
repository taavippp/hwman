from rich.table import Table as RichTable
from datetime import date, datetime
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
            self.config.get("file")
        )
        if (self.config.get("reminders")):
            if (datetime.strptime(
                self.config.get("date_opened"),
                "%d-%m-%Y"
            ) <= datetime.now()):
                self.reminder()
        self.set(
            "date_opened",
            date.strftime(date.today(), "%d-%m-%Y")
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
        print(
            "Saved file: [blue]{}[/blue]".format(
                self.data_file.path
            )
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
    
    # The list of entries would start at 1.    
    def edit(self, index: int, param: str, value: datetime | str | Progress):
        self.data.edit(index - 1, param, value)
        print(
            "Changed parameter [blue]'{}'[/blue] at index {} to [blue]'{}'[/blue]".format(
                param, index, value       
            )
        )

    def delete(self, index: int):
        self.data.remove(index - 1)
        print(
            "Removed element at index {}".format(
                index
            )
        )
    
    def print_data(self, data: list[HomeworkElement], message: str):
        table = RichTable(
            "ID",
            "Date",
            "Course",
            "Info",
            "Progress"
        )
        for index, element in enumerate(data):
            table.add_row(
                "{}.".format(index + 1),
                element.date_to_string(),
                element.course,
                element.info,
                element.progress_to_string()
            )
        print(
            message.format(
                len(data)
            ),
            table
        )

    def find(self, param: str, value: datetime | str | Progress):
        result = self.data.find(param, value)
        self.print_data(
            result,
            "[bold yellow]Found {} element(s):[/bold yellow]"
        )
    
    
    def list(self):
        self.print_data(
            self.data.get_all(),
            "[bold yellow]List has {} element(s):[/bold yellow]"
        )
    
    def settings(self):
        table = RichTable(
            "Variable",
            "Value"
        )
        settings = self.config.get_all()
        for key in settings:
            table.add_row(
                key,
                str(settings[key])
            )
        print(
            "[bold yellow]Settings:[/bold yellow]",
            table
        )
    
    def set(self, var: str, value: str | bool):
        self.config.set(var, value)
        print(
            "Set variable [blue]{}[/blue] to [blue]{}[/blue]".format(
                var, value
            )
        )
    
    def sort(self, param: str):
        self.data.sort(param)
        print("Sorted elements by [blue]{}[/blue].".format(
            param
        ))
    
    def reminder(self):
        result = filter(
            lambda element: (
                0 >= element.now_and_date_diff_in_days() > -3
            ),
            self.data.get_all()
        )
        self.print_data(
            list(result),
            "[bold yellow]List of [red]imminent[/red] homework:[/bold yellow]"
        )

test = TerminalController(True)