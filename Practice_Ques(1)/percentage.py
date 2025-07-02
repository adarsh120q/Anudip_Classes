marks = list(map(int, input("Enter marks of student in Five subjects: ").split()))[:5]

for n in marks:
    if n < 0 or n > 100:
        print("Invalid input!")
        break
else:
    total_marks = sum(marks)

    st_percent = total_marks/5

    if st_percent <40:
        print("Fail")
    elif st_percent < 50:
        print("Third Division")
    elif st_percent <60:
        print("Second Division")
    else:
        print("First Division")