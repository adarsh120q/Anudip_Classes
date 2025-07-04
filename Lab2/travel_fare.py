dist = float(input("Enter the travelled distance in Kilometer: "))

if dist > 0:
    if dist <= 50:
        print(f"Total fare is: Rupees {dist*8}")
    elif dist <= 100:
        print(f"Total fare is: Rupees {((dist-50)*10)+(50*8)}")
    else:
        print(f"Total fare is: Rupees {((dist-100)*12)+(50*10)+(50*8)}")
else:
    print("Invalid input!")