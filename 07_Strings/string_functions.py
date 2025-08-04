my_string="  Hello Python Programming      "
print(my_string.lower())
print(my_string.upper())

#Remove spaces from left and right both
print(my_string.strip())

# removes spaces from left
print(my_string.lstrip())

# Removes spaces from right
print(my_string.rstrip())
print(len(my_string))

# Replaces 'Python' with 'Java'
print(my_string.replace('Python','Java'))

# delimiter or seperator
my_data="Learning Python For Fun and Earn"
# Splits the string into list cinsidering spaces' ' as seperator
print(my_data.split())
#sep ->seperator : sep=None

my_data2="Learning@Java for@web@development"
data=my_data2.split(sep='@',maxsplit=-1)
print(data)
sentence=" ".join(data)
print(sentence)
print(type(sentence))
# The above operation joins the data in a single string

for i in range(1,6):
    print("  "*(5-i),end="")
    print(" * ".join("1" for j in range(1,i+1)))
 # str(1) for j in range(1,i+1)
 # string for loop
 #list comprehension syntax
 # expression for item in iterable
 
my_data3="Python Programming is easy to learn and Python is versatile"
print(my_data3.find("Python",4, len(my_data3)))
print(my_data3.count("Python"))
print(my_data3.startswith("Python"))
print(my_data3.endswith("Python"))
word="Python123"
print(word.isalpha())
print(word.isdigit())
print(word.isalnum())

value = 42
formatted_str = "Value: %05d" % value
print(formatted_str)