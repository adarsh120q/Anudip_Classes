n = 7
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end=' ')
    for k in range(65+n-1,63+i,-1):
        print(chr(k),end=' ')
    for l in range(65+i,65+n ):
        print(chr(l),end=' ')
    print()

for i in range(n-1,0,-1):
    for j in range(i-1):
        print(" ",end=' ')
    for k in range(65+n-1,63+i,-1):
        print(chr(k),end=' ')
    for l in range(65+i,65+n ):
        print(chr(l),end=' ')
    print()
