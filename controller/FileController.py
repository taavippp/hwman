from dataclasses import dataclass
from datetime import datetime
import csv

from model.HomeworkElement import HomeworkElement
from model.Progress import Progress

@dataclass
class FileController:
    """Class for reading and writing .csv files related to the program."""
    path: str

    def read_data(self) -> list[HomeworkElement]:
        data: list[HomeworkElement] = list()
        with open(self.path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(HomeworkElement(
                    datetime.strptime(
                        row["Date"],
                        "%d-%m-%Y %H:%M"
                    ),
                    str(row["Course"]),
                    str(row["Info"]),
                    Progress(int(row["Progress"])),
                ))
        return data

    def write_data(self, data: list[HomeworkElement]) -> None:
        with open(self.path, "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Date",
                "Course",
                "Info",
                "Progress",
            ])
            for element in data:
                writer.writerow(element.to_list())
    
    def read_config(self) -> dict[str, ConfigElement]:
        config = dict()
        with open(self.path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                config[row["Variable"]] = row["Value"]
        return config
    
    def write_config(self, config: dict[str, object]) -> None:
        with open(self.path, "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Variable",
                "Value",
            ])
            for variable in config:
                writer.writerow([
                    variable, config[variable]
                ])