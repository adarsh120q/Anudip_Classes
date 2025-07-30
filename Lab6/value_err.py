try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Exception encountered")
    print("Enter the value in integer only")
else:
    print(f"You have entered {num}")