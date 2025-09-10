class Person:
    def greet(self):
        print("Hello to OOP ")
        self.show()
    def show(self):
        print("Good Afternoon")

#self is object of class itself which will be used within a class Python automatically passes it when you create the object of a class ...
# per Person()# object creation
# #object/instance=calls the constructor: ClassName()
##_init(): constructor function
#per.greet("Pooja")
per=Person()
per.greet()
