# Objective:
# - Create a random number generator, and ask the user to guess the number.

# Imports
from random import randint
from os import system
from time import sleep

# Constants of Colors and Texts
PROGRAM_PREFIX = "\033[35m[PROGRAM]\033[0m"
USER_PREFIX = "\033[33m[YOU]\033[0m"
COLOR_RED = "\033[31m"
COLOR_RESET = "\033[0m"

# Functions
def clear():
    system('cls')

def number_generator(level):
    match level:
        case 1: # Easy
            return randint(0, 10)
        case 2: # Medium
            return randint(0, 30)
        case 3: # Hard
            return randint(0,100)
    
def game_logic(level):
    clear()

    chosen_number = number_generator(level)
    guessed_numbers = []
    proceed = True
    attempts = 1


    while proceed:
        try:
            print(f"{PROGRAM_PREFIX} Enter a number!\n")
            
            if len(guessed_numbers) > 0:
                print(f"Numbers already guessed: {guessed_numbers}")

            choice = int(input(f"{USER_PREFIX} "))

            distance = abs(chosen_number - choice) 

            if choice == chosen_number:
                proceed = False
            else:
                print(f"{COLOR_RED}Wrong! Try again.{COLOR_RESET}")

                if distance <= 2:
                    print("TIP: Extremely close! You are almost there.")
                elif distance <= 5:
                    print("TIP: You're getting warmer. Very close now.")
                elif distance < 20:
                    print("TIP: Not quite. You are within range, but still a bit off.")     
                elif distance >= 20:
                    print("TIP: You are quite far from the target. Keep searching! ")

                sleep(1)

                clear()
                guessed_numbers.append(choice)
                guessed_numbers.sort()
                attempts+=1


        except ValueError:
            print("Invalid value. Try again!")
    
    clear()
    print(f"Congratulations! You needed {attempts} attempts.")

def start_program():
    clear()

    # First dialog
    print(f"{PROGRAM_PREFIX} Hello! Can you say your name?\n")
    name = input(f"{USER_PREFIX} ")
    sleep(1)

    # Second dialog
    proceed = True
    print(f"\n{PROGRAM_PREFIX} {name}, what a great name! OK, let's start the game!\n") 

    while proceed: 
        sleep(0.5)
        print(f"{PROGRAM_PREFIX} Please, select one of the following difficulty levels:\n1. EASY\n2. MEDIUM\n3. HARD\n")
        sleep(0.5)
        choice = input(f"{USER_PREFIX} ").upper()
        sleep(1)

        match choice:
            case "1" | "EASY":
                choice = 1
                proceed = False
            case "2" | "MEDIUM":
                choice = 2
                proceed = False
            case "3" | "HARD":
                choice = 3
                proceed = False
            case _:
                print("Invalid value. Try again please!")
                sleep(1)

    # Third dialog
    print(f"\n{PROGRAM_PREFIX} OK. Difficulty chosen. Starting program.\n")
    sleep(1)

    # Game started
    game_logic(choice)

# Start program
if __name__ == '__main__':
    start_program()