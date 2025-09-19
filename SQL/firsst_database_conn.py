import mysql.connector

# Connect to MySQL / MariaDB
connobj = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12041204',
    database='studentmanagement'
)

# Creating cursor object
curobj = connobj.cursor()

# Taking user input
stdid = input("Enter student id: ")
stdname = input("Enter student name: ")
age = int(input("Enter age (in years): "))

# Insert query using %s placeholders
sqlquery = "INSERT INTO student (id, name, age) VALUES (%s, %s, %s)"
values = (stdid, stdname, age)

# Execute and commit
curobj.execute(sqlquery, values)
connobj.commit()

print("Data inserted successfully!")

# Close connection
curobj.close()
connobj.close()
