import datetime
class person:
    def __init__(self,name, birth):
        self.speak ="hello"
        self.walk ="walking away"
        self.name=name
        self.birth=birth
        
    def get_speak(self):
        return self.speak

    def get_walk(self):
        return self.walk

    def get_name(self):
        return self.name

    def get_birth(self):
        return self.birth

nam =input("enter your name ")
bir =input("enter a date in YYYY-MM-DD format ")
year, month, day = map(int, bir.split('-'))
bir = datetime.date(year, month, day)

Francisca = person(nam, bir)

print(Francisca.get_speak())
print("I am ", Francisca.get_name())
print("I was born on ", Francisca.get_birth())
print ("I am ", Francisca.get_walk())