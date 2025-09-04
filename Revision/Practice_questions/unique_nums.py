nums = [1,2,3,4,1,2,5]
my_list = {x for x in nums if nums.count(x) > 1}
print(my_list)