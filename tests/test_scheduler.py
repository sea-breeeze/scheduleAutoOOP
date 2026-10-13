
from worker import Worker
from task import Task
from scheduler import Scheduler


# TEST 1: Worker availability
def test_worker_availability():
    workers = [
        Worker("Juan", ["Mon", "Tue"]),
        Worker("Alex", ["Wed"])
    ]

    scheduler = Scheduler(workers, [])

    available = scheduler.get_available_workers_for_day("Mon")

    assert len(available) == 1
    assert available[0].name == "Juan"


# TEST 2: Workload balancing
def test_workload_balancing():
    workers = [
        Worker("Juan", ["Mon"]),
        Worker("Alex", ["Mon"])
    ]

    tasks = [
        Task("Clean Kitchen", 30, False),
        Task("Take Out Trash", 10, False)
    ]

    scheduler = Scheduler(workers, tasks)

    available = scheduler.get_available_workers_for_day("Mon")
    worker_minutes = scheduler.initialize_worker_minutes(available)

    assignments = scheduler.assign_tasks(
        available, worker_minutes, {}
    )

    assert assignments[0]["worker"] == "Juan"
    assert assignments[1]["worker"] == "Alex"
    assert worker_minutes["Juan"] == 30
    assert worker_minutes["Alex"] == 10


# TEST 3: Task rotation
def test_task_rotation():
    workers = [
        Worker("Juan", ["Mon", "Tue"]),
        Worker("Alex", ["Mon", "Tue"])
    ]

    tasks = [Task("Clean Kitchen", 30, True)]

    scheduler = Scheduler(workers, tasks)
    weekly_schedule = scheduler.generate_weekly_schedule()

    monday_worker = weekly_schedule["Mon"][0]["worker"]
    tuesday_worker = weekly_schedule["Tue"][0]["worker"]

    assert monday_worker == "Juan"
    assert tuesday_worker == "Alex"
    assert monday_worker != tuesday_worker


# TEST 4: No available workers
def test_no_available_workers():
    workers = [Worker("Juan", ["Mon"])]
    tasks = [Task("Clean Kitchen", 30, False)]

    scheduler = Scheduler(workers, tasks)
    weekly_schedule = scheduler.generate_weekly_schedule()

    assert weekly_schedule["Tue"] == []


# TEST 5: No workers at all
def test_no_workers():
    scheduler = Scheduler(
        [],
        [Task("Clean Kitchen", 30, True)]
    )

    weekly_schedule = scheduler.generate_weekly_schedule()

    assert all(
        assignments == []
        for assignments in weekly_schedule.values()
    )


# TEST 6: No tasks
def test_no_tasks():
    workers = [Worker("Juan", ["Mon", "Tue"])]

    scheduler = Scheduler(workers, [])
    weekly_schedule = scheduler.generate_weekly_schedule()

    assert all(
        assignments == []
        for assignments in weekly_schedule.values()
    )


# TEST 7: Tasks sorted by longest duration
def test_longest_task_first():
    workers = [Worker("Juan", ["Mon"])]

    tasks = [
        Task("Short Task", 10, False),
        Task("Long Task", 60, False),
        Task("Medium Task", 30, False)
    ]

    scheduler = Scheduler(workers, tasks)
    weekly_schedule = scheduler.generate_weekly_schedule()

    monday = weekly_schedule["Mon"]

    assert monday[0]["task"] == "Long Task"
    assert monday[1]["task"] == "Medium Task"
    assert monday[2]["task"] == "Short Task"


# TEST 8: Rotating task with only one worker
def test_rotation_single_worker():
    workers = [Worker("Juan", ["Mon", "Tue"])]
    tasks = [Task("Clean Kitchen", 30, True)]

    scheduler = Scheduler(workers, tasks)
    weekly_schedule = scheduler.generate_weekly_schedule()

    assert weekly_schedule["Mon"][0]["worker"] == "Juan"
    assert weekly_schedule["Tue"][0]["worker"] == "Juan"


# TEST 9: Nonrotating tasks can repeat workers
def test_nonrotating_task():
    workers = [
        Worker("Juan", ["Mon", "Tue"]),
        Worker("Alex", ["Mon", "Tue"])
    ]

    tasks = [Task("Take Out Trash", 10, False)]

    scheduler = Scheduler(workers, tasks)
    weekly_schedule = scheduler.generate_weekly_schedule()

    assert weekly_schedule["Mon"][0]["worker"] == "Juan"
    assert weekly_schedule["Tue"][0]["worker"] == "Juan"


# TEST 10: Weekly schedule contains seven days
def test_seven_day_schedule():
    scheduler = Scheduler([], [])

    weekly_schedule = scheduler.generate_weekly_schedule()

    expected_days = [
        "Mon", "Tue", "Wed", "Thu",
        "Fri", "Sat", "Sun"
    ]

    assert list(weekly_schedule.keys()) == expected_days
