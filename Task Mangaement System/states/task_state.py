from abc import ABC, abstractmethod

from enums.task_status import TaskStatus
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.task import Task
    
class TaskState(ABC):

    @abstractmethod
    def start_progress(self, task: 'Task'):
        pass

    @abstractmethod
    def complete_task(self, task: 'Task'):
        pass

    @abstractmethod
    def reopen_task(self, task: 'Task'):
        pass
    
    @abstractmethod
    def get_status(self) -> TaskStatus:
        pass 