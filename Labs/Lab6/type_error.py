try:
    val1 = input("Enter any value: ")
    val2 = input("Enter any value: ")
    result = val1/val2

except TypeError:
    print(f"The Division of strings is not possible.")

except Exception as e:
    print(e)
    print("Invalid input error, enter valid input")

else:
    print("Result:", result)