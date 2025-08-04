
num1, num2 = map(int, input("Enter two space seperated numbers: ").split())

if num1>num2:
    while True:
        if num1%num2 == 0:
            print("HCF is: ",num2)
            break
        else:
            x = num2
            num2 = num1%num2
            num1 = x

else:
    while True:
        if num2%num1 == 0:
            print("HCF is: ",num1)
            break
        else:
            x = num1
            num1 = num2%num1
            num2 = x