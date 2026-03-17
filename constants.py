import re

DATABASE_NAME = "Customer.db"
TABLE_NAME = "CUSTOMER_DATA"

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, email))

def arrange_records(records):
    output = []
    if records:
        for record in records:
            record_format = f"{record[0]},{record[1]},{record[2]}"
            output.append(record_format)

    return output
