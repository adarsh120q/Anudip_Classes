import json

with open("/home/adarshsingh/Anudip_Classes/Labs/Lab7/Invalid_Inputs_JSON/data.json", mode= "r") as file:
    data = json.load(file)

    for book in data:
        if type(book['Product ID']) is not int:
            print(f"Invalid Product ID: {book['Product ID']}")
        if type(book['Name']) is not str:
            print(f"Invalid Name: {book['Name']}")
        if type(book['Price']) is not float and type(book['Price']) is not int:
            print(f"Invalid Price: {book['Price']}")