try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1/num2

except ZeroDivisionError :
    print("Exception encountered!")
    print("Division by zero not possible.")

except Exception as e:
    print(e)
    print("Invalid input error, enter valid input")

else:
    print("Result:",result)