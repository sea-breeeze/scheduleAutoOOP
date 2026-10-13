class Scheduler:
    """A class to manage the scheduling of tasks."""

    def __init__(self, workers, tasks):
        self.workers = workers
        self.tasks = tasks    

    def get_available_workers_for_day(self, day):
        available_workers = []

        for worker in self.workers:
            if worker.is_available(day):
                available_workers.append(worker)

        return available_workers

    def initialize_worker_minutes(self, available_workers):
        worker_minutes = {}

        for worker in available_workers:
            worker_minutes[worker.name] = 0

        return worker_minutes

    def assign_tasks(self, available_workers, worker_minutes, last_task_worker):
        assignments = []

        if not available_workers:
            return assignments

        sorted_tasks = sorted(
            self.tasks,
            key=lambda task: task.duration,
            reverse=True
        )

        for task in sorted_tasks:

            eligible_workers = available_workers

            if task.is_rotating():
                previous_worker = last_task_worker.get(task.name)

                other_workers = [
                    worker for worker in available_workers
                    if worker.name != previous_worker
                ]

                if other_workers:
                    eligible_workers = other_workers

            selected_worker = min(
                eligible_workers,
                key=lambda worker: worker_minutes[worker.name]
            )

            assignments.append({
                "task": task.name,
                "worker": selected_worker.name,
                "duration": task.duration
            })

            worker_minutes[selected_worker.name] += task.duration

            if task.is_rotating():
                last_task_worker[task.name] = selected_worker.name

        return assignments

    def generate_weekly_schedule(self):
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        weekly_schedule = {}
        last_task_worker = {}

        for day in days:

            available_workers = self.get_available_workers_for_day(day)

            worker_minutes = self.initialize_worker_minutes(
                available_workers
            )

            assignments = self.assign_tasks(
                available_workers,
                worker_minutes,
                last_task_worker
            )

            weekly_schedule[day] = assignments

        return weekly_schedule