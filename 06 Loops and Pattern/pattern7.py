n = 5
for i in range(n,0,-1):
    for j in range(n-i,0,-1):
        print(" ",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    for l in range(2,i+1):
        print(l,end=" ")
    print()

for i in range(2,n+1):
    for j in range(n-i,0,-1):
        print(" ",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    for l in range(2,i+1):
        print(l,end=" ")
    print()