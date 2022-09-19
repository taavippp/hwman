#incomplete and honestly not sure if even correct
from dataclasses import dataclass

@dataclass(init = False)
class ConfigController:
    config: dict[str, object] = dict()

    valid_vars: set = {
        "default_file",
        "display_time_24",
        "reminders",
    }

    def __init__(self, config_dict: dict[str, object]) -> None:
        for var in config_dict:
            if (self._is_valid_var(var)):
                value = config_dict[var]

    def _is_valid_var(self, var) -> bool:
        return var in self.valid_vars