calls = int(input("Enter total number of calls: "))

if calls >=0 and calls <= 100:
    print(f"Monthly telephone bill is {200} Rupees.")
elif calls >=0 and calls <= 150:
    print(f"Monthly telephone bill is {200 + (calls*0.6)} Rupees.")
elif calls >= 0 and calls <= 200:
    print(f"Monthly telephone bill is {200 + (calls*0.5)} Rupees.")
elif calls >= 0:
    print(f"Monthly telephone bill is {200 + (calls*0.4)} Rupees.")
else:
    print("Invalid input!")