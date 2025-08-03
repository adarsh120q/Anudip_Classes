import csv

with open("/home/adarshsingh/Anudip_Classes/Practice Questions/incorrect_file.csv", "r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    for row in csv_reader:
        phone = 0
        if row[1].isdigit():
            phone = int(row[1])
        
        count = 0
        while phone!=0:
            count+=1
            phone = phone//10

        if not row[0].isalpha() or count != 10 or row[2].count("@")!=1 or "." not in row[2] or row[2].find("@")>row[2].rfind("."):
            print(f"Name-{row[0]}, Phone-{row[1]}, Email-{row[2]} : Invalid Record")

        else:
            print(f"Name-{row[0]}, Phone-{row[1]}, Email-{row[2]} : Valid Record")