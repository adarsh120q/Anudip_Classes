import csv

with open('winners.csv', mode = 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        print(f"Name-{row[0]}, Event-{row[1]}, Position-`{row[2]}")