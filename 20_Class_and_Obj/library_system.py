class LibraryMember:
    fine_per_day = 5

    def __init__(self, name, books_borrowed):
        self.name = name
        self.books_borrowed = books_borrowed

    def borrow_book(self, count):
        self.books_borrowed += count

    @classmethod
    def change_fine_rate(cls, new_rate):
        cls.fine_per_day = new_rate

    def calculate_fine(self, days_overdue):
        # Check if the instance has its own fine_per_day attribute
        if 'fine_per_day' in self.__dict__:
            return self.fine_per_day * days_overdue
        else:
            return LibraryMember.fine_per_day * days_overdue


m1 = LibraryMember("Aman", 2)
m2 = LibraryMember("Jatin", 0)

m1.borrow_book(1)
m2.borrow_book(2)
# aman : 3 jatin : 2
LibraryMember.change_fine_rate(10)

m2.fine_per_day = 15
# m1->aman=10
# m2->jatin=15
print(m1.name, m1.calculate_fine(3))  # Uses class fine rate → 10 × 3 = 30 as m1 not having its own instance property as fine_per_day
print(m2.name, m2.calculate_fine(3))  # Uses instance fine rate → 15 × 3 = 45 as m2 having its own instance property as fine_per_day
