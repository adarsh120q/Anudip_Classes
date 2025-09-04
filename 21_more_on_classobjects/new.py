class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        self.salary = salary

class Student(Person):
    def __init__(self, name, roll_no):
        Person.__init__(self, name)
        self.roll_no = roll_no

class ResearchScholar(Employee, Student):
    def __init__(self, name, roll_no, salary, field):
        Employee.__init__(self, name, salary)
        Student.__init__(self, name, roll_no)
        self.field = field


    def show_details(self):
        print(
            f"Research Scholar: {self.name}, "
            f"Roll No: {self.roll_no}, "
            f"Salary: {self.salary}, "
            f"Field: {self.field}"
        )


# ---- Test ----
rs = ResearchScholar("Komal", 101, 20000, "Artificial Intelligence")
rs.show_details()
print(ResearchScholar.mro())
