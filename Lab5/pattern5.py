n = 5  
for i in range(n):
    print(" " * (n - i - 1) * 2, end='')
    num = 1  
    for j in range(i + 1):
        print(f"{num:<4}", end='') 
        num = num * (i - j) // (j + 1)
    print()  
