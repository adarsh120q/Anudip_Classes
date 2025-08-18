class Laptop :
    os="Windows"
    def __init__(self, brand, price):
        self.brand=brand
        self.price=price

    @classmethod
    def change_os(cls, new_os):
        cls.os=new_os


l1=Laptop ("HP", 67000)
l2=Laptop ("Dell", 58000)
print(l1.brand, l1. price, l1.os)
print(l2.brand, l2.price, l2.os)
l1.series="Pavilion"
Laptop.change_os("Mac")
print(l1.brand, l1. price, l1.os)
print(l2.brand, l2.price, l2.os)
print(l1.__dict__)
print(l2.__dict__)
print(l1.series)
# print(l2.series)