percent = float(input("Enter the percentage: "))
if percent >= 85 and percent <= 100:
    sub_choice = int(input("Please select your choice of course- \n 1) BCA         2) BCom(H) \nEnter '1' or '2' according to the course selection: "))
    
    if sub_choice == 1:
        cs_marks = float(input("Enter marks of CS: "))
        if cs_marks >= 90 and cs_marks <=100:
            print("Eligible for Admission!")
        else:
            print("Not eligible!")      
    elif sub_choice == 2:
        math_marks = float(input("Enter marks of Maths: "))
        if math_marks >= 95 and math_marks <=100:
            print("ELigible for admission")
        else:
            print("Not eligible!")

    else:
        print("Enter valid number (only '1' or '2')!")
else:
    print("Not Applicable!")