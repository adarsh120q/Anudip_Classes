file = "/home/adarshsingh/Anudip_Classes/12 Exceptional Handling/myfile.txt"
try:
    file=open("/home/adarshsingh/Anudip_Classes/12 Exceptional Handling/myfile.txt","r")
    data=file.read()

except FileNotFoundError:
    print('File Not Found')
else:
    print(data)
finally:
    print("Closing file")
    file.close()

