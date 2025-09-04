def is_prime(num):
    count_prime = [i for i in range(1,int(num**0.5)+1) if num%i==0]
    if len(count_prime)!=2:
        return "Not Prime"
    else:
        return "Prime"

prime_nums = [i for i in range(1,50) if is_prime(i)=="Prime"]
print(prime_nums)