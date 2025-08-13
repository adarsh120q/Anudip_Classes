
def my_decorator_n(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result=func(*args, **kwargs)
        print("After call")
    return wrapper
@my_decorator_n
def add_numbers(a,b):
    return a+b
result=add_numbers (10,20)

