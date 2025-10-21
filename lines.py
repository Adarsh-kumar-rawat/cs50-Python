import sys
import os

# Must have exactly one command-line argument
if len(sys.argv) != 2:
    sys.exit(1)

filename = sys.argv[1]

# File must exist and end with .py
if not filename.endswith(".py") or not os.path.isfile(filename):
    sys.exit(1)

loc = 0
with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            loc += 1

print(loc)
