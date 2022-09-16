from dataclasses import dataclass
from model.Enums import Day, Progress

@dataclass
class HomeworkElement:
    day: Day
    course: str
    info: str
    progress: Progress

    def day_to_string(self) -> str:
        return self.day.name.title()
    
    def progress_to_string(self) -> str:
        return self.progress.name.title()

    def to_list(self) -> list:
        return list([
            self.day.value,
            self.course,
            self.info,
            self.progress.value
        ])

#    def to_csv(self) -> str:
#        return "{},{},{},{}".format(
#            self.day.value,
#            self.course,
#            self.info,
#            self.progress.value,
#        )