my_list = list(map(int, input("Enter the numbers: ").split()))

l = len(my_list)-1

for i in range(l-1):
    for j in range(i+1, l):
        if my_list[i]>my_list[j]:
            temp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = temp
        else:
            continue

print("The second highest number is:", my_list[l-1])