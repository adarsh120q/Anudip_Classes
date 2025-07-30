file = None
try:
  file=open("Lab6/myfile.txt","r")
  data=file.read()
except FileNotFoundError:
  print('File Not Found')
else :
  print(data)
finally :
  if file is not None:
    print("Closing file")
    file.close() 
