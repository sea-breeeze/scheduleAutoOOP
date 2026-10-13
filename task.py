class Task:
    def __init__(self, name, duration, rotating):
        self.name = name
        self.duration = duration
        self.rotating = rotating
        
    def is_rotating(self):
        return self.rotating