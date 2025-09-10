import csv

with open("/home/adarshsingh/Anudip_Classes/Labs/Lab7/Age > 30_CSV/new_people.csv", "w") as file:
    csv_writer = csv.writer(file)

    with open("/home/adarshsingh/Anudip_Classes/Labs/Lab7/Age > 30_CSV/people.csv", "r") as file2:
        csv_reader = csv.reader(file2)
        header = next(csv_reader)
        csv_writer.writerow(header)

        for row in csv_reader:
            if int(row[1]) > 30:
                csv_writer.writerow(row)

    print("File updated succesfully")    