import csv
import json

with open("/home/adarshsingh/Anudip_Classes/Lab7/JSON file to CSV/data.csv", "w") as file:
    csv_writer = csv.writer(file)

    with open("/home/adarshsingh/Anudip_Classes/Lab7/JSON file to CSV/product.json", "r") as file2:
        data = json.load(file2)
        csv_writer.writerow(data[0].keys())

        for items in data:
            csv_writer.writerow(items.values())