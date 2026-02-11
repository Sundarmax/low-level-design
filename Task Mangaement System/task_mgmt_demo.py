
from task_management_system import TaskManagementSystem
from enums.task_priority import TaskPriority
from strategies.sort_by_priority import SortByPriority
task_mgmt_system =  TaskManagementSystem()

from datetime import date

user1 = task_mgmt_system.create_user("Sundar max", "max@gmail.com")
 
print(user1.name,user1.id)

task1 = task_mgmt_system.create_task(
    "Cloud cost control","Calculate the monthly billing",date.today(), TaskPriority.LOW, user1.id
)
print(task1.get_id(),task1.get_title(),task1.get_due_date(),task1.get_status())
task1.start_progress()
print(task1.get_id(),task1.get_title(),task1.get_due_date(),task1.get_status())
task1.complete_task()
print(task1.get_id(),task1.get_title(),task1.get_due_date(),task1.get_status())

task2 = task_mgmt_system.create_task(
    "k8s cost control","Calculate the monthly billing",date.today(), TaskPriority.HIGH, user1.id
)

task3 = task_mgmt_system.create_task(
    "VM cost control","Calculate the monthly billing",date.today(), TaskPriority.MEDIUM, user1.id
)

sort_tasks = task_mgmt_system.sort_task(SortByPriority())
sorted_task = [ [tsk.get_id(),tsk.get_priority()] for tsk in sort_tasks]
print(sorted_task)