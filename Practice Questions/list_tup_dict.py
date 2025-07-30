def classification(my_list):
    result = {}
    for key, value in my_list:
        if key not in result:
            result[key] = []
        result[key].append(value)

    for key, value in result.items():
        print (f"{key} : {value}")  


list1 = [('fruit', 'apple'), ('fruit', 'banana'), ('color', 'red')]

choice = 1
print("Want to add element to the dictionary or view the dictionary?")
print("Enter 1 to add elements\nEnter 2 to view the dictionary")

ch = int(input("\nEnter choice here: "))

if ch == 1:
    while True:
        key = input("Enter category name: ")
        value = input("Enter the value: ")
        list1.append((key, value))  

        choice = int(input("Enter 0 to stop, or any other number to continue: "))
        if choice == 0:
            break

    print("\nUpdated grouped dictionary:")
    classification(list1)

elif ch == 2:
    print("\nGrouped dictionary:")
    classification(list1)

else:
    print("Invalid input!")
