from sys import argv, exit
import csv

new = []
if len(argv) < 3:
    exit("Too few command-line arguments")
elif len(argv) > 3:
    exit("Too many command-line arguments")
elif ".csv" not in argv[1]:
    exit("Not a CSV file")

try:
    with open(argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(", ")
            new.append({"first": first, "last": last, "house": row["house"]})

except FileNotFoundError:
    exit("File does not exist")

with open(argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in new:
        writer.writerow(row)
