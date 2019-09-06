class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age

    # Acts as a getter
    @property 
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age cannot be negative")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"


        

jane = Human("Jane", "Goodall", 50)
jane.age = 55
print(jane.age)
print(jane.full_name)

