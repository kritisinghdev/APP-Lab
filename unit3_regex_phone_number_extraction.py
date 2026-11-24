"""Unit 3 - Regular Expression, Question 1: Phone Number Extraction
Find and extract valid Indian mobile numbers from free-form text.

An Indian mobile number:
  * has 10 digits and starts with 6, 7, 8 or 9
  * may have a prefix: +91, 91 or 0  (with an optional space or hyphen after it)
  * may be written with one space or hyphen in the middle, e.g. 98765 43210
"""

import re

PHONE_PATTERN = re.compile(r"""
    (?<!\d)                  # not preceded by another digit
    (?:(?:\+91|91|0)[\s-]?)? # optional country code / leading zero
    [6-9]\d{4}               # first 5 digits (first digit is 6-9)
    [\s-]?                   # optional space or hyphen
    \d{5}                    # last 5 digits
    (?!\d)                   # not followed by another digit
""", re.VERBOSE)


def extract_phone_numbers(text):
    """Return a list of the phone numbers found, as written in the text."""
    return [m.group() for m in PHONE_PATTERN.finditer(text)]


def clean_number(number):
    """Keep only the last 10 digits, e.g. '+91 98765-43210' -> '9876543210'."""
    return re.sub(r"\D", "", number)[-10:]


text = """
Hello! Call me on 9876543210 or +91 98765 43210.
My office number is 080-23456789 (landline, not a mobile).
Other contacts: 91-8123456789, 07012345678, +91-6543210987.
Invalid ones: 1234567890 (starts with 1), 98765 (too short),
and 98765432101234 (too many digits).
"""

if __name__ == "__main__":
    print("Text:")
    print(text)

    found = extract_phone_numbers(text)
    print("Valid Indian mobile numbers found:")
    for number in found:
        print(f"  {number:20} -> {clean_number(number)}")

    print("\nTotal found:", len(found))

    # Optional: let the user try their own text
    user_text = input("\nEnter your own text (or press Enter to skip): ")
    if user_text:
        print("Numbers found:", extract_phone_numbers(user_text) or "None")
