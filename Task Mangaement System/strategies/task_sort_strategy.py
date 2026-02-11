from abc import ABC,abstractmethod
from entities.task import Task

class TaskSortStrategy(ABC):
    
    @abstractmethod
    def sort(self, tasks : list[Task]):
        pass