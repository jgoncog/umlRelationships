class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_name(self):
        return self.name

    def get_age(self):
        return self.__age


class Teacher(Person):
    def teach(self):
        print(f"{self.get_name()} is teaching")


# Testing the inherited features
teacher = Teacher("Mona", 30)

print(f"Name: {teacher.get_name()}")
print(f"Age: {teacher.get_age()} (note this age is privately accessed)")
teacher.teach()