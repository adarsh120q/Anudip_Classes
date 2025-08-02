import json

with open("CSV and Json/myjson.json", mode= "r") as file:
    data = json.load(file)
    
    for book in data['books']:
        print(f"Title: {book['title']}-----Author: {book['author']}-----Available: {book['available']}")
