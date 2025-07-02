a = input("Enter the character: ")

if (ord(a)>=20 and ord(a)<48) or (ord(a)>57 and ord(a)<65) or (ord(a)>90 and ord(a)<97) or (ord(a)>122 and ord(a)<127):
    print("It is a SYMBOL!")
elif (ord(a)>47 and ord(a)<58):
    print("It is a NUMBER!")
elif (ord(a)>64 and ord(a)<91):
    print("It is an UPPERCASE ALPHABET!")
elif (ord(a)>60 and ord(a)<123):
    print("It is a LOWERCASE ALPHABET!")
else:
    print("Invalid input!")