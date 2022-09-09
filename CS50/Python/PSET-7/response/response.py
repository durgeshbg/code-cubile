import validator_collection

email = input("What's your email address? ")

try: 
    validator_collection.email(email)
    print("Valid")
except:
    print("Invalid")