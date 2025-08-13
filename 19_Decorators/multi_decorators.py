def dec_1(func):
    def wrapper(): 
        print("Before call 1")
        func() 
        print("After call 1")
    return wrapper
def dec_2(func):
    def wrapper(): 
        print("Before call 2")
        func() 
        print("After call 2")
    return wrapper

def dec_3(func):
    def wrapper(): 
        print("Before call 3") 
        func() 
        print("After call 3")
    return wrapper

@dec_1
@dec_2
@dec_3
def my_func():
    print("Hello, Demo of multiple decorator calling")
my_func()