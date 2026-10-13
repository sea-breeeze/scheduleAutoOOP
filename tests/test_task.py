from task import Task

task1 = Task("Clean Kitchen", 30, True)
task2 = Task("Take Out Trash", 10, False)

print(task1.name)
print(task1.duration)
print(task1.is_rotating())

print(task2.name)
print(task2.duration)
print(task2.is_rotating())