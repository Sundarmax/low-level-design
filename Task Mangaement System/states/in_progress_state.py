from .task_state import TaskState
from enums.task_status import TaskStatus
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.task import Task

class InprogressState(TaskState):

    def start_progress(self, task : 'Task'):
        print("Task is already in progress.")

    def complete_task(self, task : 'Task'):
        from .done_state import DoneState
        task.set_state(DoneState())

    def reopen_task(self, task : 'Task'):
        from .todo_state import TodoState
        task.set_state(TodoState())

    def get_status(self) -> TaskStatus:
        return TaskStatus.IN_PROGRESS
