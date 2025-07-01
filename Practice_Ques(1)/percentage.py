marks = list(map(int, input("Enter marks of student in Five subjects: ").split()))[:5]
total_marks = sum(marks)

st_percent = total_marks/5

if st_percent >=0 and st_percent <40:
    print("Fail")
elif st_percent >=40 and st_percent < 50:
    print("Third Division")
elif st_percent >=50 and st_percent <60:
    print("Second Division")
elif st_percent >=60 and st_percent <= 100:
    print("First Division")
else:
    print("Invalid input!")