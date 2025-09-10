#Dictionary
# Option 1 : Using {}
my_dict={"name":"Komal","age":20,"course":"Python","roll_no":20}
print(my_dict)

# Option 2 : Using dict()
employee=dict(name="Komal",age=20,course="Python",roll_no=20)
print(employee)

# accessing the values
print(employee["name"])# value on the basis of key
print(employee.get("name"))# value on the basis of key
print(employee.get("surname","Not Found"))# if the key is not present
# add or update
employee["name"]="Nisha"
print(employee)
employee["surname"]="Jaiswal"
print(employee)
employee.update({"name":"Komal","surname":"Jaiswal"})
print(employee)
# remove
# del employee["age"]
# print(employee)
# employee.pop("course")
# print(employee)
# employee.popitem()
# employee.clear()
# print(employee)

print(employee.keys())
print(employee.values())
print(employee.items())# creates list of tuples

for key in employee:
  print(key," : ",employee[key])

for key,value in employee.items():
  print(key,value)