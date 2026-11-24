"""Experiment 8: Read an input file, count lines, extract the first two lines
and write them to a new file  -- CO-3"""

import os

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

# Create a sample input file if one does not exist
if not os.path.exists(INPUT_FILE):
    with open(INPUT_FILE, "w") as f:
        f.write("Python is easy to learn.\n"
                "File handling is useful.\n"
                "This is the third line.\n"
                "And this is the fourth line.\n")

# Read the file
with open(INPUT_FILE, "r") as f:
    lines = f.readlines()

# Count lines
print("Total number of lines:", len(lines))

# Extract the first two lines
first_two = lines[:2]
print("First two lines:")
for line in first_two:
    print("  ", line.strip())

# Write to a new file
with open(OUTPUT_FILE, "w") as f:
    f.writelines(first_two)

print(f"Extracted data written to '{OUTPUT_FILE}'")
