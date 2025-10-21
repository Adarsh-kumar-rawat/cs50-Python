import csv
import sys


if len(sys.argv) != 3:
    sys.exit("Usage: python scourgify.py input.csv output.csv")

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        output_rows = []
        for row in reader:
            name, house = row
            last, first = name.split(", ")  # split "Last, First"
            output_rows.append([first, last, house])

except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")

with open(output_file, "w", newline="", encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["first", "last", "house"])  # new header
    writer.writerows(output_rows)
