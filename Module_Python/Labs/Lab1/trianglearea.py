side1,side2,side3 = map(int, input("Enter sides of the triangle: ").split())
s = (side1 + side2 + side3)/2  
area = abs(s*(s-side1)*(s-side2)*(s-side3))**0.5
print(f"Area of the triangle is: {int(area)}")