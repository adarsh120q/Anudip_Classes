n = 18
for i in range(1,n+1):
    for j in range(i):
        print("*",end=' ')
    for j in range(n-i-1,-1,-1):
        print(" ",end=' ')
    for j in range(n-i-1,0,-1):
        print(" ",end=' ')
    if i==n:
        for j in range(i-1):
            print("*",end=' ')
    else:
        for j in range(i):
            print("*",end=' ')
    print()

for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=' ')
    for j in range(n-i-1,-1,-1):
        print(" ",end=' ')
    for j in range(n-i-1,0,-1):
        print(" ",end=' ')
    if i==n:
        for j in range(i-1):
            print("*",end=' ')
    else:
        for j in range(i):
            print("*",end=' ')
    print()