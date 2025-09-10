cost_price = int(input("Enter cost price: "))
sell_price = int(input("Enter selling price: "))

if cost_price >= 0 and sell_price >= 0:
    if cost_price > sell_price:
        print("Loss!")
    elif sell_price > cost_price:
        print("Profit!")
    else:
        print("Same!")

else:
    print("Invalid input!")