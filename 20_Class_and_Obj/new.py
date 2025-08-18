class Car:
    wheels = 4
    def __init__(self, brand): 
        self.brand = brand

c1 = Car("Toyota")
c2 = Car("Honda")
c1.wheels = 6
Car.wheels = 8
print(c1.brand, c1.wheels)
print(c2.brand, c2.wheels)
print(Car.wheels)
c3=Car("Hyundai")
print(c3.brand, c3.wheels)