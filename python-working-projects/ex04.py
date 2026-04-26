# Objective:
# - Create a calculator

# Imports
from os import system
from time import sleep


# Functions
def calculator(value):
    
    # Separator 
    newCalculation = value.strip().split() 
    
    # Transform
    try:
        number = int(newCalculation[0])
        number_two = int(newCalculation[2])

    except ValueError:
        print("ERROR: You didn't put a valid value. Try again!")

    # Check of operation
    match newCalculation[1]:
        case '+':
            print(number + number_two)

        case '-':
            print(number - number_two)

        case '/':
            if number_two == 0:
                print("ERROR: Division by 0 its prohibited!")
            else: 
                print(number / number_two)

        case '*' | 'x' | '.':
            print(number * number_two)

        case _:
            return ValueError


def main():
    proceed = True

    while proceed:
        system('cls')
        try:
            operation = input("Enter the calculation to be perfomed: ")
            calculator(operation)
            
            if operation:
                proceed = False

        except ValueError:
            print("ERROR: You didn't put a valid value. Try again!")
            sleep(1)
        
if __name__ == '__main__':
    main()