
from abc import ABC,abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.task import Task

class TaskObserver(ABC):
    
    @abstractmethod
    def update(self, task: 'Task', change_type: str):
        pass