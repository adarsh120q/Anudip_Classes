quantity = int(input("Enter the number of items bought: "))
price = int(input("Enter the price per item: "))

if quantity >= 0 and price >= 0:
    total_cost = quantity*price

    if total_cost>=5000:
        print(f"Total expense is {total_cost-(total_cost*0.1)} Rupees.")
    else:
        print(f"Total expense is {total_cost} Rupees.")

else:
    print("Invalid input!")