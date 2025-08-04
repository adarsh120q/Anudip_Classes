n = 3
for i in range(1,n+1):
    for j in range(n-i,0,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        if k==1:
            print("1",end=" ")
        else:
            print("*",end=" ")
    for l in range(i-1,0,-1):
        if l==1:
            print("1",end=" ")
        else:
            print("*",end=" ")
    print()

for i in range(n-1,0,-1):
    for j in range(n-i,0,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        if k==1:
            print("1",end=" ")
        else:
            print("*",end=" ")
    for l in range(i-1,0,-1):
        if l==1:
            print("1",end=" ")
        else:
            print("*",end=" ")
    print()