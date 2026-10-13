from worker import worker
from task import Task
from scheduler import Scheduler

workers = [
    worker("Juan", ["Mon", "Tue"]),
    worker("John", ["Tue", "Wed"]),
    worker("Alex", ["Mon", "Wed"])
]

tasks = [
    Task("Clean Kitchen", 30, True),
    Task("Take Out Trash", 10, False)
]

scheduler = Scheduler(workers, tasks)

available = scheduler.get_available_workers_for_day("Mon")

for worker in available:
    print(worker.name)

worker_minutes = scheduler.initialize_worker_minutes(available)

print(worker_minutes)

last_task_worker = {}

monday_minutes = scheduler.initialize_worker_minutes(
    scheduler.get_available_workers_for_day("Mon")
)

monday = scheduler.assign_tasks(
    scheduler.get_available_workers_for_day("Mon"),
    monday_minutes,
    last_task_worker
)

print("Monday:", monday)
print("History:", last_task_worker)

tuesday_minutes = scheduler.initialize_worker_minutes(
    scheduler.get_available_workers_for_day("Tue")
)

tuesday = scheduler.assign_tasks(
    scheduler.get_available_workers_for_day("Tue"),
    tuesday_minutes,
    last_task_worker
)

print("Tuesday:", tuesday)
print("History:", last_task_worker)

weekly_schedule = scheduler.generate_weekly_schedule()

for day, assignments in weekly_schedule.items():
    print(f"\n{day}:")

    for assignment in assignments:
        print(
            f"  {assignment['task']} -> "
            f"{assignment['worker']} "
            f"({assignment['duration']} min)"
        )