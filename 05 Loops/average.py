nums = list(map(float, input("Enter five numbers:").split()))[:5]

x = len(nums)-1
sum = 0
while x>=0:
    if nums[x] == 0:
        print("You have entered Zero!")
    else:
        sum = sum + nums[x]
        x-=1

