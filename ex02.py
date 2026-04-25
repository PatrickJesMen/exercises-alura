# Objective:
# - Create a random password generator;
# - Must include at least one uppercase and lowercase letter, as well as at least one numeric digit and one special character.

# Imports
from string import ascii_lowercase, ascii_uppercase, digits 
from random import shuffle, choice, choices
from os import system

# Characteres bank
LOW = ascii_lowercase 
UPPER = ascii_uppercase  
NUM = digits 
SIGN = '!@#&*'

# Functions
def generate_key():
    password = [ 
        choice(UPPER),
        choice(NUM),
        choice(SIGN)
    ]

    total_characters = LOW + UPPER + NUM + SIGN
    password.extend(choices(total_characters, k=8))
    shuffle(password)
    return ''.join(password)

def clear():
    system('cls')

def main():
    clear()
    proceed = True
    while proceed:
        print(f"Your password: {generate_key()}")
        q = input("Continue with this password? [Y/N]").upper()

        if q == "Y":
            print("Thank you for your participation.")
            proceed = False

        elif q == "N":
            clear()
            pass

        else:
            clear()
            print("Invalid.")


if __name__ == "__main__":
    main()