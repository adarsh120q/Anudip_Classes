import json # Import the JSON module to work with JSON files
#Data to be written to the JSON file
inventory = {
"books": [
{"title": "Learning Python", "author": "Mark Lutz", "available": True},
{"title": "Django for Beginners", "author": "William S. Vincent", "available": False},
{"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "available": True}
]
}
#Writing to the JSON file
with open('tech_books_inventory.json', mode='w') as file: # Open the file in write mode ('w')
    json.dump(inventory, file, indent=4) # Write the JSON data to the file with indentation for readability
print("Data saved successfully")