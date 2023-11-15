import re

# Regular expression pattern for validating email addresses
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# List of sample email addresses to test
sample_emails = [
    'example@email.com',
    'test.user@email.co.uk',
    'my_email123@email-server.net',
    'invalid.email@',
    'noattherate.com',
    'missing@domaincom',
    'spaces in@email.com',
    'double@@email.com',
    'incomplete@domain.',
    'email@-domain.com'
]

# Function to validate email addresses
def validate_email(email):
    if re.match(email_pattern, email):
        return f"{email} is a valid email address."
    else:
        return f"{email} is NOT a valid email address."

# Testing the sample email addresses
for email in sample_emails:
    print(validate_email(email))
