from .task_state import TaskState
from enums.task_status import TaskStatus

from .in_progress_state import InprogressState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.task import Task


class TodoState(TaskState):

    def start_progress(self, task : 'Task'):
        task.set_state(InprogressState())

    def complete_task(self, task : 'Task'):
        print("Cannot complete the task that is not in progress")

    def reopen_task(self, task : 'Task'):
        print("Task is already in TO-DO state")

    def get_status(self):
        return TaskStatus.TODO
