from model.HomeworkElement import HomeworkElement
from model.Enums import Day, Progress
from dataclasses import dataclass
import csv

@dataclass
class DataManager:
    path: str

    def read_data(self) -> list[HomeworkElement]:
        data: list[HomeworkElement] = list()
        with open(self.path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(HomeworkElement(
                    Day(int(row["Day"])),
                    str(row["Course"]),
                    str(row["Info"]),
                    Progress(int(row["Progress"])),
                ))
        return data

    def write_data(self, data: list[HomeworkElement]) -> None:
        with open(self.path, "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Day",
                "Course",
                "Info",
                "Progress",
            ])
            for element in data:
                writer.writerow(element.to_list())