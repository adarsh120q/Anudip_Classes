items = {}
item_names = ["Apple", "Mango", "Bread"]
quant_price = [
    {"Quantity": 46, "Price": 20}, 
    {"Quantity": 34, "Price": 10}, 
    {"Quantity": 54, "Price": 35}
]

for name, details in zip(item_names, quant_price):
    items[name] = details

print("Welcome to AS Mart!")
while True:
    print("\nEnter '1' to Display Inventory-")
    print("Enter '2' to Add/Update product-")
    print("Enter '3' to Sell Product-")
    print("Enter '0' to Exit-\n")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nHere is the inventory-")
        for item, details in items.items():
            print(f"{item} - Quantity: {details['Quantity']}, Price: ₹{details['Price']}")

        print("\nDo you want to Continue or Exit?")
        choice = int(input("Enter '1' to Continue, '0' to Exit: "))
        if choice  == 1:
            continue
        elif choice == 0:
            break
        else:
            print("Invalid input!\n")

    elif choice == 2:
        print("Do you want to Add 'New' item or 'Update' the existing one?")
        print("   Enter '1' to add new item-\n   Emter '2' to update the item-\n   Enter '0' for Main menu-")
        choice2 = int(input("Enter the choice: "))
        while choice2 != 1 and choice2 != 2 and choice2 != 0:
            print("\nInvalid input!")
            choice2 = int(input("Enter valid option number- '1'/'2'/'0' : "))

        if choice2 == 1:
            new_item = input("Enter the new item name: ")
            while new_item in item_names:
                print("ERROR! You have entered the existing item name.")
                new_item = input("Enter the NEW name: ")

            item_names.append(new_item)
            quantity = int(input(f"Enter the quantity of {new_item}: "))
            price = int(input(f"Enter the price of {new_item}: "))
            quant_price.append({"Quantity": quantity, "Price": price})

            for name, details in zip(item_names, quant_price):
                items[name] = details

            print("\nNew Item added successfully!")

            print("\nDo you want to Continue or Exit?")
            choice = int(input("Enter '1' to Continue, '0' to Exit: "))
            if choice  == 1:
                continue
            elif choice == 0:
                break
            else:
                print("Invalid input!\n")

        elif choice2 == 2:
            item_name = input("\nEnter the name of item: ")
            while item_name not in items:
                print(f"'{item_name}' no such item is in the inventory!")
                item_name = input("Enter valid name: ")

            quantity = int(input(f"Enter the quantity of {item_name}: "))
            price = int(input(f"Enter the price of {item_name}: "))   
            items[item_name]['Quantity'] = quantity
            items[item_name]['Price'] = price

            print("\nInventory updated successfully!")

            print("\nDo you want to Continue or Exit?")
            choice = int(input("Enter '1' to Continue, '0' to Exit: "))
            if choice  == 1:
                continue
            elif choice == 0:
                break
            else:
                print("Invalid input!\n")

    elif choice == 3:
        item_name = input("\nEnter name of item to sell: ")
        while item_name not in items:
            print(f"'{item_name}' no such item is in the inventory!")
            item_name = input("Enter valid name: ")

        quantity = int(input(f"Enter quantity of {item_name} to sell: "))
        while quantity > items[item_name]['Quantity'] or quantity < 1:
            if quantity > items[item_name]['Quantity']:
                print("Insufficient Quantity!")
                quantity = int(input(f"Enter smaller quantity of {item_name} to sell: "))
            else:
                print("Invalid Input!")
                quantity = int(input(f"Enter bigger quantity of {item_name} to sell: "))
            
        price = items[item_name]['Price']*quantity
        print(f"SOLD! The price of {quantity} {item_name} is ₹{price}")

        items[item_name]['Quantity']-= quantity

        print("\nDo you want to Continue or Exit?")
        choice = int(input("Enter '1' to Continue, '0' to Exit: "))
        if choice  == 1:
            continue
        elif choice == 0:
            break
        else:
            print("Invalid input!")

    elif choice == 0:
        break

    else:
        print("Invalid input!\nPlease choose the appropriate option.")

    
print("\nThank you for visiting AS Mart!")

