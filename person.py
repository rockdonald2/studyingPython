class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print("The person's name is " + self.name)

class Student(Person):
    def __init(self, name, age, school):
        # or you can use the super().__init__ function to, its means the same thing
        Person.__init__(self, name, age)
        self.school = school


p1 = Person("Zsolt", 19)
p1.printName()
del p1
