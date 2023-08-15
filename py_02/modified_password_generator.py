import random
import string
import time
import math


def random_password(length, include_uppercase, include_symbol):
    """
    Generate a random password
    Args:
        length: The length of the password
        include_uppercase: Boolean, whether to include uppercase letters
        include_symbol: Boolean, whether to include symbols
    Returns:
        password: string, the generated password
    """

    if length <= 1 or length > 16:
        print("The length of the password must be between 2 and 16")
        raise ValueError

    result = ""
    symbol = [
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=']

    character_sets = [
        string.ascii_lowercase,
        string.digits,
        string.ascii_uppercase if include_uppercase else '',
        "".join(symbol) if include_symbol else ''
    ]

    if include_uppercase and include_symbol:
        weights = [0.4, 0.3, 0.2, 0.1]
    elif include_uppercase:
        weights = [0.5, 0.3, 0.2, 0]
    elif include_symbol:
        weights = [0.5, 0.3, 0, 0.2]
    else:
        weights = [0.6, 0.4]

    for char_set, weight in zip(character_sets, weights):
        result += "".join(random.choices(char_set,
                          k=math.floor(length * weight)))
    return result


if __name__ == "__main__":
    start_time = time.time()
    unique_passwords = set()

    while time.time() - start_time < 5:
        password = random_password(16, True, True)
        if password in unique_passwords:
            print("The password has been generated:", password)
            raise ValueError
        unique_passwords.add(password)
    print("Test Successful!")
