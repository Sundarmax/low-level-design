
from .task_observer import TaskObserver
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.task import Task

class ActivityLogger(TaskObserver):

    def update(self, task: 'Task', change_type : str):
        print(f"LOGGER: Task '{task.get_title()}' was updated. Change: {change_type}")

class EmailNotifer(TaskObserver):
    pass

