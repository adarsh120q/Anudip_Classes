def checkValidity(age):
    if age>=18:
        print("Eligible for voting")
    else:
        raise ValueError("Ineligible for voting")
        #raising an exception explicitly (manually)
try:
    age=int(input("Enter age to check validity: "))
    checkValidity(age)
except ValueError as ve:
    print(ve)
    print("Invalid Input By User")
except IndentationError:
    print("Indentation Error")
finally:
    print("End of Program")