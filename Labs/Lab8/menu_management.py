regular_menu = {"Pizza", "Burger", "Salad", "Pasta"}
weekend_menu = {"Steak", "Salmon", "Pasta", "Wine"}

all_dishes = regular_menu.union(weekend_menu)
print("List of regular items and weekend items both:")
for index,items in enumerate(all_dishes,1):
    print(f"{index}. {items}")

weekend_dishes = weekend_menu.difference(regular_menu)
print("\nList of items available only on weekends:")
for index,items in enumerate(weekend_dishes,1):
    print(f"{index}. {items}")

regular_menu.add("Dessert")
weekend_menu.add("Dessert")

print("\nLatest Regular dishes after adding 'Dessert':")
for index,items in enumerate(regular_menu,1):
    print(f"{index}. {items}")

print("\nLatest Weekends menu after adding 'Dessert':")
for index,items in enumerate(weekend_menu,1):
    print(f"{index}. {items}")

regular_menu.remove("Burger")
print("\nUpdated Regular menu after removing 'Burger':")
for index,items in enumerate(regular_menu,1):
    print(f"{index}. {items}")