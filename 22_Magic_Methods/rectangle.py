class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def __eq__(self,other):
        return (self.l*self.b == other.l*other.b)

    def __lt__(self,other):
        return (self.l*self.b < other.l*other.b)

    def __le__(self,other):
        return (self.l*self.b <= other.l*other.b)

    def __gt__(self,other):
        return (self.l*self.b > other.l*other.b)

    def __ge__(self,other):
        return (self.l*self.b >= other.l*other.b)


a1 = Rectangle(3,4)
a2 = Rectangle(9,6)

print(a1==a2)
print(a1<a2)
print(a1<=a2)
print(a1>a2)
print(a1>=a2)