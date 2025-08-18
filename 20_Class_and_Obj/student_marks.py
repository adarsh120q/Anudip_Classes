class Student():
    def __init__(self, name):
        self.name = name
        self.marks_dict = {}

    def add_mark(self, subject, mark):
        self.marks_dict[subject]=mark

    def average(self):
        avg = (sum(self.marks_dict.values()))//len(self.marks_dict)
        return avg

    def grade(self):
        avg = self.average()
        if avg>=90 and avg<=100:
            return "A"

        elif avg>=75:
            return "B"

        elif avg >=50:
            return "C"
        elif avg<50 and avg>=0:
            return "E"

    def details(self):
        print(f"Name of student: {self.name}")
        print(f"Marks of {self.name}- ")
        for subject, marks in self.marks_dict.items():
            print(f"    {subject} - {marks}")

        print(f"Average of marks: {self.average()}")
        print(f"Grade: {self.grade()}")


my_st = Student("Adarsh")
my_st.add_mark("Maths",90)
my_st.add_mark("Cs", 87)
my_st.details()