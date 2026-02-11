from .task_sort_strategy import TaskSortStrategy
from enums.task_priority import TaskPriority

class SortByPriority(TaskSortStrategy):

    def sort(self, tasks):
        priority_order = {
            TaskPriority.CRITICAL : 4,
            TaskPriority.HIGH : 3,
            TaskPriority.MEDIUM : 2,
            TaskPriority.LOW : 1
        }
        tasks.sort(key=lambda task: priority_order.get(task.get_priority(),0), reverse=True)
        return tasks


