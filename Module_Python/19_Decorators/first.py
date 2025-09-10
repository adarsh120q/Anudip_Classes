def decorator_my(func):
  def wrapper():
    print("Starting of program")
    func()
    print("Ending of program")

  return wrapper

@decorator_my
def say_hello():
  print("hello")

say_hello()