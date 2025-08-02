basic_pay = int(input("Enter employee's basic salary: "))

if basic_pay > 0 and basic_pay <1500:
    total_pay = basic_pay + (basic_pay*0.1) + (basic_pay*0.9)
    print(f"Total gross salary of the employee is {total_pay} Rupees.")
elif basic_pay >=1500:
    total_pay = basic_pay + 500 + (basic_pay*0.98)
    print(f"Total gross salary of the employee is {total_pay} Rupees.")
else:
    print("Invalid input!")