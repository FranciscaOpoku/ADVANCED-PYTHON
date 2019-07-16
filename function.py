class Person:
    def __init__(self):
        self.age = 20
    def get_age(self):
        return self.age
francisca = Person()
print("francisca is ",francisca.get_age(), "years old")