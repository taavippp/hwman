import sys
from ElementController import ElementController

class InputController:
    """Class that handles user input."""
    keywords: dict[str, function] = {
        "add": ElementController.add,
        "edit": ElementController.edit,
        "delete": ElementController.remove,
        "remove": ElementController.remove, # same as 'delete'
        "list": ElementController.get_data,
        "show": ElementController.get_data, # same as 'list'
#       "settings",
#       "config", #same as 'settings'
#       "set",
#       "help",
        "exit": sys.exit,
    }

    def handle_input(self, input: str) -> list[function, list]:
        if (len(input) == 0):
            return
        input_data = input.split()
        func = self.keywords[input_data[0]]
        input_data.pop(0)
        return [func, input_data]