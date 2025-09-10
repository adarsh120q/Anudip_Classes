list1 = list(map(int, input("Enter space seperated integers: ").split()))
list2 = list(map(int, input("Enter space seperated integers: ").split()))

list3 = list(set(list1).intersection(set(list2)))
print(list3)