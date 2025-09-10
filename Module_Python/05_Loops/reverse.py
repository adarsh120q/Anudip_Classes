num = int(input("Enter the number: "))

x = 0

while num>0:
    x = x*10+(num%10)
    num = num//10

print("Reversed number is:",x)