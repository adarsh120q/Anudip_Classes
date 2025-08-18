items = {}
st_names = ["Adarsh", "Manu", "Bob"]
st_marks = [
    {"Maths": 46}, 
    {"Science": 34}, 
    {"Computer": 54}
]

for name, details in zip(st_names, st_marks):
    items[name] = details

for name,details in items.items():
    for item, value in details.items():
        print(f"{name}: {item} - {value}")
