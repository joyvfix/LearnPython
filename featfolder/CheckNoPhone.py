import phonenumbers


def check_phone_number(number):
    try:
        parsed_number = phonenumbers.parse(number, None)
        is_valid = phonenumbers.is_valid_number(parsed_number)
        return is_valid
    except phonenumbers.phonenumberutil.NumberParseException:
        return False


# Example usage: Check if a phone number is valid
phone_number = "+6282226110859"
is_valid_number = check_phone_number(phone_number)
print(f"Is the phone number valid? {is_valid_number}")
