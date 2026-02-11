from .task_state import TaskState
from enums.task_status import TaskStatus
from entities.task import Task
from .todo_state import TodoState


class DoneState(TaskState):

    def start_progress(self, task : 'Task'):
        print("Cannot start a completed task. reopen it first")

    def complete_task(self, task : 'Task'):
        print("Task is already done")

    def reopen_task(self, task : 'Task'):
        task.set_state(TodoState())

    def get_status(self) -> TaskStatus:
        return TaskStatus.DONE
