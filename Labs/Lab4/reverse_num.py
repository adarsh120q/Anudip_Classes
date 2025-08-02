num = int(input("Enter the number: "))
list_num = list(str(num))
new_num = []

while list_num:
    x = list_num.pop()
    new_num.append(x)

result = ''.join(new_num)
print("Reversed number:", result)
