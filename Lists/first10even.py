my_list = [3,56,947,5,6,1,3,6,4,9,8,98,65,5,252,4,6,465,654]
my_list2 = []
i = 0
while len(my_list2)<10:
    if my_list[i]%2==0:
        my_list2.append(my_list[i])
    i+=1

print(my_list2)