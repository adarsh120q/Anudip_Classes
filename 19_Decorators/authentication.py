import time

def log_time(func):
    def wrapper():
        current_time = time.time()
        print(f"Current time is: {current_time}")
        func()
    return wrapper

def authorise(user_role):
    def my_decorator(func):
        def wrapper():
            if user_role == 'admin':
                print("Access granted")
                func()
            else:
                print("Access denied!")
                return None

        return wrapper
    return my_decorator

user_role = input("Enter your role here: ")

@authorise(user_role.lower())
@log_time
def my_func():
    print("Here the function works")

my_func()