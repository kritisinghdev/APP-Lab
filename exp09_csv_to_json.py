"""Experiment 9: Read a CSV file, convert the data to JSON and write it
to a .json file  -- CO-3"""

import csv
import json
import os

CSV_FILE = "students.csv"
JSON_FILE = "students.json"

# Create a sample CSV if one does not exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "marks"])
        writer.writerows([[1, "Asha", 85], [2, "Ravi", 72], [3, "Meera", 91]])

# Read CSV: each row becomes a dictionary
with open(CSV_FILE, "r", newline="") as f:
    rows = list(csv.DictReader(f))

# Write the list of dictionaries as JSON
with open(JSON_FILE, "w") as f:
    json.dump(rows, f, indent=4)

print(f"Converted {len(rows)} rows from '{CSV_FILE}' to '{JSON_FILE}'")
print(json.dumps(rows, indent=4))
