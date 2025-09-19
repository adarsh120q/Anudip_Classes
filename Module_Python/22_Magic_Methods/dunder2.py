class Sum:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num*other.num

x = Sum(5)
y = Sum(5)
print((x+y)*5)