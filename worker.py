class Worker:
    def __init__(self, name, availability):
        self.name = name
        self.availability = availability

    def is_available(self, day):
        return day in self.availability