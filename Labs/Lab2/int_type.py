check = lambda a: "Positive" if a>0 else("Negative" if a<0 else "Zero")

num = float(input("Enter the number: "))

print(check(num))