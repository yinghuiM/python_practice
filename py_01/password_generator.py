import random
import string


def random_password(digits_length, include_uppercase, include_symbol):
    """
    Generate a random password
    Args:
        digits_length: The length of the password
        include_uppercase: Boolean, whether to include uppercase letters
        include_symbol: Boolean, whether to include symbols
    Returns:
        password: string, the generated password
    """
    symbol = [
        'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=']
    password = ''
    normal_password = string.ascii_lowercase + string.digits
    uppercase_password = string.ascii_lowercase + \
        string.ascii_uppercase + string.digits
    symbol_password = string.ascii_lowercase + \
        string.ascii_uppercase + string.digits + "".join(symbol)

    if (include_uppercase == True):
        for i in range(digits_length):
            password += random.choice(uppercase_password)
    elif include_symbol:
        for i in range(digits_length):
            password += random.choice(symbol_password)
    else:
        for i in range(digits_length):
            password += random.choice(normal_password)
    return password


print(random_password(10, False, False))
