class ConfigController:
    config: dict[str, object] = dict()

    valid_vars: dict = {
        "file": str,
        "display_time_24": bool,
        "reminders": bool,
    }

    def set(self, var: str, value: str | bool) -> None:
        if not (self._is_valid_var(var, value)):
            return
        self.config[var] = value
    
    def get_all(self) -> dict[str, str | bool]:
        return self.config

    def __init__(self, param_dict: dict[str, object]) -> None:
        for var in param_dict:
            self.set(var, param_dict[var])

    def _is_valid_var(self, var, value) -> bool:
        if not (var in self.valid_vars.keys()):
            return False
        if not (self.valid_vars[var] == type(value)):
            return False
        return True