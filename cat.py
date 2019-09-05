class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)


gus = Cat("Gus", 9)
print(gus.description())