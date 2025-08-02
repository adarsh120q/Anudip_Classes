import csv

winners = [
    ['Name', 'Event', 'Position'],
    ['John', 'Coding challenge', '1st'],
    ['Jane Smith', 'Art comp.', '2nd'],
    ['Sam', 'Music contest', '1st'],
]

with open('winners.csv', mode = 'w', newline = '') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(winners)
print("Data saved successfully")