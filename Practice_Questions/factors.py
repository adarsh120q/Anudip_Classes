def factors(num):
    fact_list = []
    for i in range(1, (num//2)+1):
        if num%i == 0:
            fact_list.append(i)
        
    for i in fact_list:
        print(i, end = ' ')


num = int(input("Enter the number: "))
factors(num)
