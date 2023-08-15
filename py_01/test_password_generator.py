import time
from password_generator import random_password


def test_random_password():
    start_time = time.time()
    unique_passwords = set()

    while time.time() - start_time < 600:
        password = random_password(10, True, True)
        if password in unique_passwords:
            print("The password has been generated:", password)
            return False
        unique_passwords.add(password)

    print("Test Successful!")
    return True


test_random_password()
