from worker import worker

worker = worker("UpdateTest", ['Mon', 'Tue', 'Wed'])

print (worker.name)
print (worker.availability)

print("Is worker available on Mon?", worker.is_available('Mon'))
print("Is worker available on Thu?", worker.is_available('Thu'))