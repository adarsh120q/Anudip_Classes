print("What type of toys do you want?")
print("(1) Battery Based Toys\n(2) Key-Based Toys\n(3) Electrical Charging Based Toys")
choice = int(input("Type number '1' or '2' or '3' to choose: "))

if choice == 1:
    amt = float(input("Enter the amount: "))
    if amt>=0:
        if amt > 1000:
            print(f"Total amount to be paid: Rupees {amt-(amt*0.1)}")
        else:
            print(f"Total amount to be paid: Rupees {amt}")
    else:
        print("Invalid input!")

elif choice == 2:
    amt = float(input("Enter the amount: "))
    if amt>=0:
        if amt > 100:
            print(f"Total amount to be paid: Rupees {amt-(amt*0.05)}")
        else:
            print(f"Total amount to be paid: Rupees {amt}")
    else:
        print("Invalid input!")

elif choice == 3:
    amt = float(input("Enter the amount: "))
    if amt>=0:
        if amt > 500:
            print(f"Total amount to be paid: Rupees {amt-(amt*0.1)}")
        else:
            print(f"Total amount to be paid: Rupees {amt}")
    else:
        print("Invalid input!")

else:
    print("Invalid input!")