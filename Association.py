class Doctor:
    def __init__(self, name: str):
        self.name = name

    def treat(self, patient):
        print(f"Dr. {self.name} is treating {patient.name}.")


class Patient:
    def __init__(self, name: str):
        self.name = name



doctor = Doctor("Smith")
patient = Patient("Alice")


doctor.treat(patient) 
