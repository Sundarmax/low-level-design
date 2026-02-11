import threading
from entities.user import User
from entities.task import Task
from enums.task_priority import TaskPriority
from datetime import date
from observers.activity_logger import ActivityLogger
from strategies.task_sort_strategy import TaskSortStrategy

class TaskManagementSystem:
    # _instance= None
    # _lock = threading.Lock()

    def __init__(self):
        self._users = {}
        self._tasks = {}

    def create_user(self, name:str, email:str) -> User:
        user = User(name,email)
        self._users[user.id] = user
        return user

    def create_task(self, title: str, desc: str, due_date: date, priority : TaskPriority,
                    created_by_user_id : str ) -> Task:
        created_by = self._users.get(created_by_user_id)
        if created_by is None:
            raise ValueError("User not found")
        
        task = Task.TaskBuilder(title) \
        .description(desc) \
        .due_date(due_date) \
        .priority(priority).created_by(created_by).build()

        task.add_observer(ActivityLogger())
        self._tasks[task.get_id()] = task
        return task
    

    def sort_task(self, sorting_strategy : TaskSortStrategy) -> list[Task]:
        tsks = []
        for tsk in self._tasks.values():
            tsks.append(tsk)
        return sorting_strategy.sort(tsks)