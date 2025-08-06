def next_step(choice):
    print("Do you want to continue or exit:")
    print("Enter 1 to continue same process-")
    print("Enter 2 go to main menu-")
    print("Enter 0 to exit the program-")
    choice = int(input("Enter your choice here: "))
    while choice != 1:
        if choice == 1:
            x = 0

in_stock = {"laptop", "mouse", "keyboard", "monitor"}
out_of_stock = {"printer", "webcam"}
choice = 1
while choice != 0:
    print("Enter your choice according to desired operation:")
    print("1 - To add items in stock")
    print("2 - To add items in out of stock category")
    print("3 - Check availability of item")
    print("4 - Check which products are available for sale")
    print("0 - To close operation")
    choice = int(input("Enter your choice here: "))
    if choice == 1:
        items = input()
        in_stock = in_stock.union(items)
        out_of_stock = out_of_stock.difference(items)
        print("New items added successfully!")
        print(in_stock, end = '\n')
    
    elif choice == 2:
        items = input()
        out_of_stock = out_of_stock.union(items)
        in_stock = in_stock.difference(items)
        print("Item discarded from stock!")
        print(f"In Stock items = {in_stock}")
        print(f"Out of stock items = {out_of_stock}\n")

    elif choice == 3:
        item = input("Enter item name here: ")
        if item in in_stock:
            print(f"Item {item} is in stock")
        else:
            print(f"Item {item} is out of stock\n")

    elif choice == 4:
        print(f"Items available for sale = {in_stock}\n")

    elif choice == 0:
        print("Inventry operation closed!")

    else:
        print("Invalid input!")
        break



