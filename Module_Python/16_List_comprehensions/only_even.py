data = [[10, 15, 20], [25, 30], [35, 40, 45]]
all_even = [item for rows in data for item in rows if item%2 == 0]
print(all_even)

new_even = [[item for item in rows if item %2 == 0] for rows in data]
print(new_even)