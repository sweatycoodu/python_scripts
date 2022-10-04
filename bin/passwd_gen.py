"""
A simple script to generate random passwords from the shell.
Supports special characters, and can be used to generate passwords of any length.
"""


# Import the required modules for the script to function.

import random
import string


def get_length():
    """Function to declare the length of the password, prompted to the user."""
    length = input("Password length: ")
    # Display an error message if the length is invalid.
    if not length.isdigit():
        print("Invalid length...")
        return get_length()
    return int(length)


def get_special():
    """Function to include special characters in the password, prompted to the user."""
    special = input("Include special characters? (y/n): ")
    # Display an error message if the input is invalid.
    if special.lower() not in ('y', 'n'):
        print("Invalid input...")
        return get_special()
    return special.lower() == 'y'


def generate_password(length, special):
    """Function to generate the password."""
    # Define the characters to be used in the password.
    chars = string.ascii_letters + string.digits
    if special:
        chars += string.punctuation
    # Generate the password.
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def print_password(password):
    """Function to print the generated password to the user."""
    print(f"Generated password: {password}")


def generate_go():
    """Main function to run the script."""
    length = get_length()
    special = get_special()
    password = generate_password(length, special)
    print_password(password)

# Run the script.


generate_go()
