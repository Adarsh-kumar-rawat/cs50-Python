import sys
import os
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit("Usage: python pizza.py <file.csv>")

filename = sys.argv[1]

# Check that file ends with .csv
if not filename.lower().endswith(".csv"):
    sys.exit("Error: file must have a .csv extension")

if not os.path.isfile(filename):
    sys.exit(f"Error: file '{filename}' does not exist")

# Read the CSV file
table = []
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        table.append(row)
print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
