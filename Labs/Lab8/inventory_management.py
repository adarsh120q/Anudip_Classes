in_stock = {"laptop", "mouse", "keyboard", "monitor"}
out_of_stock = {"printer", "webcam"}
choice = 1
print("==========ONLINE STORE INVENTORY==========")
while choice != 0:
    print("\nEnter your choice according to desired operation:")
    print("1 - To add items in stock")
    print("2 - To add items in out of stock category")
    print("3 - Check availability of item")
    print("4 - Check which products are available for sale")
    print("0 - To close operation")
    choice = int(input("Enter your choice here: "))
    if choice == 1:
        items = input("\nEnter the names of the items you want to add: ").split()
        in_stock = in_stock.union(items)
        out_of_stock = out_of_stock.difference(items)
        print("New items added successfully!")
        for index,item in enumerate(in_stock,1):
            print(f"{index}: {item}")

        print("Do you want to continue the operation or exit the program?")
        print("Enter 1 to continue-")
        print("Enter 0 to Exit-")
        choice = int(input("Enter your choice here: "))
        if choice == 0:
            break
        elif choice != 1:
            print("Invalid input!")

    elif choice == 2:
        items = input("\nEnter the name of items which gone out of stock: ").split()
        out_of_stock = out_of_stock.union(items)
        in_stock = in_stock.difference(items)
        print("Inventory updated successfully!")
        print(f"In Stock items:")
        for index,item in enumerate(in_stock,1):
            print(f"{index}: {item}")
        print(f"Out of stock items:")
        for index,item in enumerate(out_of_stock,1):
            print(f"{index}: {item}")

        print("Do you want to continue the operation or exit the program?")
        print("Enter 1 to continue-")
        print("Enter 0 to Exit-")
        choice = int(input("Enter your choice here: "))
        if choice == 0:
            break
        elif choice != 1:
            print("Invalid input!")

    elif choice == 3:
        item = input("\nEnter item name here: ")
        if item in in_stock:
            print(f"Item {item} is in stock")
        else:
            print(f"Item {item} is out of stock\n")

        print("\nDo you want to continue the operation or exit the program?")
        print("Enter 1 to continue-")
        print("Enter 0 to Exit-")
        choice = int(input("Enter your choice here: "))
        if choice == 0:
            break
        elif choice != 1:
            print("Invalid input!")

    elif choice == 4:
        print(f"\nItems available for sale are:")
        for index,item in enumerate(in_stock,1):
            print(f"{index}: {item}")

        print("Do you want to continue the operation of exit the program?")
        print("Enter 1 to continue-")
        print("Enter 0 to Exit-")
        choice = int(input("Enter your choice here: "))
        if choice == 0:
            break
        elif choice != 1:
            print("Invalid input!")

    elif choice == 0:
        break
    else:
        print("\nInvalid input!")
        break


print("\nInventry operation closed!")

