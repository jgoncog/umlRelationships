class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age


class Student(Person):
    def study(self):
        print(f"{self.name} is studying")


# Create a Student object
student1 = Student("Lina", 20)

# Test inherited features
print("Name:", student1.name)
print("Age:", student1.get_age())

# Call the Student method
student1.study()