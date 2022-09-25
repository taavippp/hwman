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
        self.conf_file = FileController("user/CONFIG.json")
        if (testing):
            self.conf_file = FileController("test/TESTCONFIG.json")
        
        self.config = ConfigController(self.conf_file.read_config())
        self.load(
            self.config.get("file")
        )
        if (self.config.get("reminders")):
            date_opened = datetime.strptime(
                self.config.get("date_opened"),
                "%d-%m-%Y"
            ).date()
            today = date.today()

            if (date_opened < today):
                self.set(
                    "date_opened",
                    date.strftime(date.today(), "%d-%m-%Y")
                )
                self.conf_file.write_config(self.config.get_all())
                self.reminder()
    
    def string_to_datetime(self, value: str) -> datetime:
        date: datetime
        try:
            date = datetime.strptime(value, "%d.%m.%Y %H:%M")
        except ValueError:
            try:
                date = datetime.strptime(value, "%d.%m.%Y")
            except ValueError:
                print("Invalid value [red]{}[/red]".format(
                    value
                ))
                date = datetime.now()
        return date
    
    def parse_value(self, param: str, value: str | int) -> datetime | str | Progress:
        match param:
            case "date":
                return self.string_to_datetime(value)
            case "progress":
                return Progress(int(value))
            case _:
                return value

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
        self.conf_file.write_config(
            self.config.get_all()
        )
        print(
            "Saved files [blue]{}[/blue] and [blue]{}[/blue]".format(
                self.data_file.path,
                self.conf_file.path
            )
        )

    def info(self) -> None:
        """Displays information about the program."""
        table = RichTable(
            "File",
            "Elements",
            "Test mode"
        )
        table.add_row(
            self.data_file.path,
            str(len(self.data.get_all())),
            str(self.testing).lower()
        )
        print(
            table
        )
    
    def add(self, datestr: str, course: str, info: str, progress: int) -> None:
        """Adds new element to the list."""
        date: datetime = self.string_to_datetime(datestr)

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
    def edit(self, index: int, param: str, value: str | int):
        """Edits an existing element in the list."""
        parsed_value = self.parse_value(param, value)
        
        self.data.edit(index - 1, param, parsed_value)
        print(
            "Changed parameter [blue]'{}'[/blue] at index {} to [blue]'{}'[/blue]".format(
                param, index, parsed_value
            )
        )

    def delete(self, index: int):
        """Deletes an element in the list."""
        self.data.remove(index - 1)
        print(
            "Removed element at index {}".format(
                index
            )
        )

#---#---#---#---#---#---#---#---#---#
    
    def print_data(self, data: list[HomeworkElement], message: str):
        if (len(data) == 0):
            print(
                "No elements to show."
            )
            return
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

    def find(self, param: str, value: str | int):
        """Shows elements with the given parameters."""
        parsed_value = self.parse_value(param, value)
        result = self.data.find(param, parsed_value)
        self.print_data(
            result,
            "[bold green]Found {} element(s):[/bold green]"
        )
    
    def list(self):
        """Shows all of the elements."""
        self.print_data(
            self.data.get_all(),
            "[bold green]List has {} element(s):[/bold green]"
        )
    
    def settings(self):
        """Shows all the configurations."""
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
            "[bold green]Settings:[/bold green]",
            table
        )
    
    def set(self, var: str, value: str | bool):
        """Changes a value in the configurations."""
        self.config.set(var, value)
        print(
            "Set variable [blue]{}[/blue] to [blue]{}[/blue]".format(
                var, value
            )
        )
    
    def sort(self, param: str):
        """Sorts the list by given parameter."""
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
            "[bold green]List of [red]imminent[/red] homework:[/bold green]"
        )