# Create a Empty Dictionary
item_prices = {}
# Get user input for a new item and its price to add
new_item = input("Enter the new item you want to add to the dictionary: ")
new_price = float(input("Enter the price for the new item: "))
# Use update() to add the new item and its price to the dictionary
item_prices.update({new_item: new_price})
print(f"Added {new_item} to the dictionary with a price of ${new_price:.2f}")
print("The available items are")
print(item_prices)# Get user input for the item to remove
item_to_remove = input("Enter the item you want to remove from the dictionary: ")
# Use pop() to remove the item and get its price
if item_to_remove in item_prices:
  price = item_prices.pop(item_to_remove)
  print(f"The price of {item_to_remove} is ${price:.2f} removed successfully")
else:
  print(f"{item_to_remove} not found in the dictionary.")
# Print the updated dictionary after popping the item
  print("Updated Dictionary:")
  print(item_prices)
# Print the updated dictionary after adding the new item
  print("Updated Dictionary:")
  print(item_prices)