import csv

with open("/home/adarshsingh/Anudip_Classes/Lab7/Missing Data in CSV/missing_data.csv", "r+") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        for i in range(3):
            if row[i] == '':
                row[i] = "Unknown"

        print(f"Name-{row[0]}, Age-{row[1]}, City-{row[2]}")
