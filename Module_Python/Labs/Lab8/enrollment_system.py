course_a = {"Alice", "Bob", "Charlie"}
course_b = {"Charlie", "David", "Eva"}

print("==========STUDENT ENROLLMENT SYSTEM==========")
choice = 1
while choice != 0:
    print("\nEnter 1 to see common students in both courses-")
    print("Enter 2 to see all students in both couses-")
    print("Enter 3 to see students only in Course A and not in B-")
    print("Enter 4 to see the students enrolled in only one course-")
    print("Enter 0 to exit the program-")
    choice = int(input("Enter you choice here: "))

    if choice == 1:
        students = course_a.intersection(course_b)
        print("\nStudents enrolled in both the courses are:")
        for index,stds in enumerate(students,1):
            print(f"{index}. {stds}")
        
    elif choice == 2:
        students = course_a.union(course_b)
        print("\nTotal students in either courses are:")
        for index,stds in enumerate(students,1):
            print(f"{index}. {stds}")

    elif choice == 3:
        students = course_a.difference(course_b)
        print("\nStudents in Course A but not in B:")
        for index,stds in enumerate(students,1):
            print(f"{index}. {stds}")

    elif choice == 4:
        students = (course_a.union(course_b)).difference(course_a.intersection(course_b))
        print("\nStudents enrolled in only one course:")
        for index,stds in enumerate(students,1):
            print(f"{index}. {stds}")
        
    elif choice == 0:
        break

    else:
        print("\nInvalid input!")

print("\nProgram ended!")