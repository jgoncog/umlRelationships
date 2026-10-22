from abc import ABC, abstractmethod

# Interface (Contract)
class Drivable(ABC):
    @abstractmethod
    def drive(self):
        pass

# Realization (Implementation)
class Car(Drivable):
    def drive(self):
        print("Car is driving!")

# Usage
my_car = Car()
my_car.drive()  # Output: Car is driving!
