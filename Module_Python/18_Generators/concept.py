'''
A generator function is defined like a regular function but uses the yield keyword to
return values one at a time. Each time yield is called, the function’s state is saved, and
it can be resumed later.
'''
def gen():
  yield 1
  yield 2
  yield 3

for i in gen():
  print(i**2)


print("\nNew Generator same as range")
'''
● yield Statement: The yield statement pauses the function, saving its state for the
    next iteration. When the generator’s __next__() method is called, the function
    resumes execution immediately after the yield statement.
● Generator Object: When you call a generator function (e.g., count_up_to(5)), it
    doesn’t execute the function body immediately. Instead, it returns a generator
    object that can be iterated over.
'''
def new_range(max):
  counter=0
  while counter<max:
    yield counter
    counter+=1

for i in new_range(5):
  print(i)