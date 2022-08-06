from sys import argv, exit
from tabulate import tabulate
import csv

table = []

if len(argv) < 2:
    exit("Too few command-line arguments")
elif len(argv) > 2:
    exit("Too many command-line arguments")
elif ".csv" not in argv[1]:
    exit("Not a CSV file")

try:
    with open(argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            table.append(row)

except FileNotFoundError:
    exit("File does not exist")

print(tabulate(table, headers="keys", tablefmt="grid"))
