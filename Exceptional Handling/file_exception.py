file = myfile.txt
try:
    file=open("myfile.txt","r")
    data-file.read()

except FileNotFoundError:
    print('File Not Found')
else:
    print(data)
finally:
    print("Closing file")
    file.close()

