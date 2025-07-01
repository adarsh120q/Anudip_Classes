angle1,angle2,angle3 = map(int, input("Enter angles of triangle: ").split())
if angle1 + angle2 + angle3 ==180:
    print("Valid Triangle!")
else:
    print("Invalid inputs!")