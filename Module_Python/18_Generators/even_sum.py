def sum_of_even(numbers):
  sum=0
  for i in numbers:
    if i%2==0:
        yield i
        sum+=i

  return sum

numbers = [10, 15, 22, 33, 40, 55, 60]
gen=sum_of_even(numbers)

try:
    while True :
        print(next(gen))
except StopIteration as e:
    print("Sum of all even numbers:",e.value)