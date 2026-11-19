class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age


person = Person("Lina", 20)

print("Name:", person.name)
print("Age:", person.get_age())

# Reflection:
# Using get_age() protects private data and allows
# controlled access to the age attribute.