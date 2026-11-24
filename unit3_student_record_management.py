"""Unit 3 - Question 1: Student Record Management System

Requirements covered:
  * Read student records from students.csv using the csv module
  * Use the 'with' statement while opening the file
  * Accept the filename using argparse (--file)
  * Display all student records
  * Search for a student using Roll Number

Usage:
  python unit3_student_record_management.py --file students.csv
  python unit3_student_record_management.py --file students.csv --roll 102
"""

import argparse
import csv
import os


def create_sample_file(filename):
    """Create a sample CSV file if the file does not exist."""
    rows = [
        ["Roll", "Name", "Department", "Marks"],
        [101, "Asha", "Computer", 85],
        [102, "Ravi", "IT", 72],
        [103, "Meera", "Computer", 91],
        [104, "Kiran", "Electronics", 66],
    ]
    with open(filename, "w", newline="") as f:
        csv.writer(f).writerows(rows)
    print(f"(Sample file '{filename}' created)\n")


def read_students(filename):
    """Read all records from the CSV file and return a list of dictionaries."""
    with open(filename, "r", newline="") as f:     # 'with' closes the file automatically
        return list(csv.DictReader(f))


def display_all(students):
    print(f"{'Roll':<8}{'Name':<15}{'Department':<15}{'Marks':<6}")
    print("-" * 44)
    for s in students:
        print(f"{s['Roll']:<8}{s['Name']:<15}{s['Department']:<15}{s['Marks']:<6}")
    print(f"\nTotal students: {len(students)}")


def search_by_roll(students, roll):
    for s in students:
        if s["Roll"] == str(roll):
            return s
    return None


def main():
    parser = argparse.ArgumentParser(description="Student Record Management System")
    parser.add_argument("--file", default="students.csv",
                        help="CSV file containing student records")
    parser.add_argument("--roll", help="Roll number to search for")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        create_sample_file(args.file)

    students = read_students(args.file)

    print("===== ALL STUDENT RECORDS =====")
    display_all(students)

    # If --roll was not given on the command line, ask the user
    roll = args.roll or input("\nEnter Roll Number to search (Enter to skip): ").strip()
    if roll:
        student = search_by_roll(students, roll)
        print("\n===== SEARCH RESULT =====")
        if student:
            for key, value in student.items():
                print(f"{key:<12}: {value}")
        else:
            print(f"No student found with Roll Number {roll}")


if __name__ == "__main__":
    main()
