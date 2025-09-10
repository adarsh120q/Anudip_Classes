n = 5
for i in range(1,n+1):
    print(" "*(n-i),end='')
    for j in range(1,i+1):
        if i!=n:
            if j==1:
                print(j,end=' ')
            elif j==i:
                print(j,end=' ')
            else:
                print(" ",end=' ')
        
        else:
            print(j,end=' ')

    print()