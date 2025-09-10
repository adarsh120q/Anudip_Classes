# Nested dictionary
students={
    "S1":{"name":"Komal","age":20,"email":"komal@abc.org"},
    "S2":{"name":"Nisha","age":21,"email":"nisha@abc.org"},
    "S3":{"name":"Ravi","age":19,"email":"ravi@abc.org"},
}
# json architecture

print(students["S2"]["age"])
#looping through the nested dictionary
for key,value in students.items():
  print(key,"=>",value["name"],"-",value["age"],"-",value["email"])
  # update age in s3
students["S3"]["age"]=23
students["S1"]["course"]="Java"
students["S3"].update({"course":"WEPP"})
students["S3"].pop("course")
del students["S1"]["course"]
print(students)
# add course as Java for Komal only using update method