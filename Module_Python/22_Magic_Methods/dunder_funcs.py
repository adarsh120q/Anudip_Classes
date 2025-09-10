class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' wiht {self.pages} pages."

    def __len__(self): # Dunder funtion
        return self.pages

    def __add__(self,other):
        return self.pages+other.pages

    def __repr__(self):
        return f"Book({self.title},{self.pages})"

book1 = Book("Python Basics", 200)
book2 = Book("Core Java", 250)

print(book1)
print(book2)
print(len(book2)) # The len function here is using the '__len__' method in the class.

print(book1+book2) # This operation would have been shown error without '__add__' function in the above class.

print(book1==book2)
print(repr(book1))# default repr prints the memory address of the object.
