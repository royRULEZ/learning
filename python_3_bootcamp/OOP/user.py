class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"


user1 = User("Joe", "Smith", 45)
user2 = User("Blanca", "Lopez", 41)

print(user1.initials())
print(user2.first)
print(user2.likes("Chips"))
