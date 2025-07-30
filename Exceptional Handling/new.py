try:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))

    print(f"The result is: {n1/n2}")
# except:
#     print("You have entered unprecidented input!")

# except Exception as e:
#     print("Error by user", e)
#     print("Error by zero is not alowed")

except ZeroDivisionError :
    print("Division by Zero is not possible!")

except Exception as e:
    print(f"{e}- It is not possible, enter valid input.")