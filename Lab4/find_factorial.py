num = int(input("Enter the number: "))
factorial = 1
while num>0:
    factorial = factorial*num
    num-=1

print("Factorial of the number is: ",factorial)