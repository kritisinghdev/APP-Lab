"""Experiment 7: Find email patterns using regular expressions -- CO-3"""

import re

# Pattern explained:
#   [\w.+-]+      -> username (letters, digits, _ . + -)
#   @             -> the @ symbol
#   [\w-]+        -> domain name
#   (\.[\w-]+)+   -> one or more extensions like .com or .co.in
EMAIL_PATTERN = r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+"

text = """
Contact us at support@example.com or sales.team@my-company.co.in.
Personal: john_doe123@gmail.com, invalid@, @nouser.com, hello@site
Send a copy to admin+news@university.edu.
"""

# 1) Find all emails in a text
emails = re.findall(EMAIL_PATTERN, text)
print("Emails found:")
for e in emails:
    print("  ", e)

# 2) Validate a single email (full match)
def is_valid(email):
    return re.fullmatch(EMAIL_PATTERN, email) is not None

for test in ["abc@xyz.com", "abc@xyz", "abc.com"]:
    print(f"{test!r} valid? {is_valid(test)}")

# 3) Extract username and domain using groups
for user, domain in re.findall(r"([\w.+-]+)@([\w-]+(?:\.[\w-]+)+)", text):
    print(f"user = {user:15} domain = {domain}")
