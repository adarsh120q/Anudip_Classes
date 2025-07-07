num = int(input("Enter the number: "))
num_list = list(str(num))
x = len(num_list) - 1
i = 0
while i<=x:
    if num_list[i] != num_list[x]:
        print("Not a Palindrome!")
        break
    else:
        x-=1
        i+=1
if i == len(num_list)-1:
    print("It is a palindrome!")