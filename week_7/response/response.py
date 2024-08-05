from validator_collection import validators

s = input("What's you email address? ").strip()

try:
    email_address = validators.email(s)
    print("Valid")
except ValueError:
    print("Invalid")