def div(a, b):
    return (f"Division of {a} by {b} is: {a/b}")

num1, num2 = map(float, input("Enter two space seperated numbers to perform division: ").split())
print(div(num1, num2))