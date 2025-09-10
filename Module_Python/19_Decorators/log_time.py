import time

def lof_time(func):
    def wrapper():
        past_time = time.time()
        func()
        current_time = time.time()
        print(f"Difference of time is: {current_time-past_time}")

    return wrapper

@lof_time
def my_func():
    print("Here the function works")

my_func()