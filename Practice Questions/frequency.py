my_list = [1,2,3,5,4,6,1,2,8,6,4,8,7,2,3,0,1]
unique_nums = list(set(my_list))

for i in range(len(unique_nums)):
    print(f"{i+1}. Number- {unique_nums[i]}: {my_list.count(unique_nums[i])} times")