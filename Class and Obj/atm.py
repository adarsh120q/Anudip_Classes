class As_Bank:
    def __init__(self,balance=50000):
        self.balance = balance

    def withdraw(self,amt):
        if self.balance>= amt:
            self.balance-=amt
            return f"\nTransaction Successful!\nYour remaining balance is: {self.balance}\n"
        else:
            return "\nInsufficient balance!"

    def deposit(self,amt):
        self.balance+=amt
        return f"\nTransaction Successful!\nYour current balance is: {self.balance}\n"

    def left_bal(self): 
            return f"\nYour current balance is: {self.balance}\n"

print("Welcome to AS Bank!\n")
trans = As_Bank()
while True:
    print("Enter 1 to Withdraw          ","Enter 2 to Deposit")
    print("Enter 3 to View Balance      ","Enter 0 to exit the Transaction")
    choice = int(input("Enter choice number here (0-3): "))
    if choice == 1:
        amt = int(input("Enter the amount you want to withdraw:"))
        print(trans.withdraw(amt))
        choice = int (input("Enter '1' to Continue or enter '0' to Exit the transaction: "))
        if choice == 0:
            break
        elif choice == 1:
            continue
        else:
            print("\nInvalid Input!\n")
    elif choice == 2:
        amt = int(input("Enter the amount you want to deposit:"))
        print(trans.deposit(amt))
        choice = int (input("Enter '1' to Continue or enter '0' to Exit the transaction: "))
        if choice == 0:
            break
        elif choice == 1:
            continue
        else:
            print("\nInvalid Input!\n")
    elif choice == 3:
        print(trans.left_bal())
        choice = int (input("Enter '1' to Continue or enter '0' to Exit the transaction: "))
        if choice == 0:
            break
        elif choice == 1:
            continue
        else:
            print("\nInvalid Input!\n")
    elif choice == 0:
        break
    else:
        print("\nInvalid input!\n")

print("\nThank You, for using AS Bank!")