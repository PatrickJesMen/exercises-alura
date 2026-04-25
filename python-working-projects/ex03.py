# Objective:
# - Create a random number generator, and ask the user to guess the number.

# Imports
from random import randint
from os import system
from time import sleep

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
    choosed_numbers = []
    proceed = True
    attempts = 1


    while proceed:
        try:
            print("\033[35m[PROGRAM]\033[0m Enter a number!\n")
            
            if len(choosed_numbers) > 0:
                print(f"Already numbers choosed: {choosed_numbers}")

            CHOICE = int(input("\033[33m[YOU]\033[0m "))

            distance = abs(chosen_number - CHOICE) 

            if CHOICE == chosen_number:
                proceed = False
            else:
                print("\n\033[31mWrong! Try again.\033[0m")

                if distance <= 2:
                    print("TIP: Extremely close! You are almost there.")
                elif distance <= 5:
                    print("TIP: You're getting warmer. Very close now.")
                elif 5 < distance < 20:
                    print("TIP: Not quite. You are within range, but still a bit off.")     
                elif distance >= 20:
                    print("TIP: You are quite far from the target. Keep searching! ")

                sleep(1)

                clear()
                choosed_numbers.append(CHOICE)
                choosed_numbers.sort()
                attempts+=1


        except:
            print("Invalid value. Try again!")
    
    clear()
    print(f"Congratulations! You needed {attempts} attempts.")

def start_program():
    clear()

    # First dialog
    print("\033[35m[PROGRAM]\033[0m Hello! Can you say your name?\n")
    NAME = input("\033[33m[YOU]\033[0m ")
    sleep(1)

    # Second dialog
    proceed = True

    while proceed: 
        print(f"\n\033[35m[PROGRAM]\033[0m {NAME}, what a great name! OK, let's start the game!\n") 
        sleep(0.5)
        print("\033[35m[PROGRAM]\033[0m Please, select one of the following difficulty levels:\n1. EASY\n2. MEDIUM\n3. HARD\n")
        sleep(0.5)
        CHOICE = input("\033[33m[YOU]\033[0m ").upper()
        sleep(1)

        match CHOICE:
            case "1" | "EASY":
                CHOICE = 1
                proceed = False
            case "2" | "MEDIUM":
                CHOICE = 2
                proceed = False
            case "3" | "HARD":
                CHOICE = 3
                proceed = False
            case _:
                print("Invalid value. Try again please!")
                sleep(1)

    # Third dialog
    print("\n\033[35m[PROGRAM]\033[0m OK. Difficulty choosed. Starting program.\n")
    sleep(1)

    # Game started
    game_logic(CHOICE)

# Start program
if __name__ == '__main__':
    start_program()