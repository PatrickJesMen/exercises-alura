# Objective:
# - Create a money divider

# Functions
def divider(value):
    # Math logic
    banknote = [100, 50, 20, 10, 5, 2, 1]

    for note in banknote:
        i = 0
        while value >= note:
            i += 1
            value -= note    
        if i > 0:
            print(f"{i}x {note} Withdrawn")

def main():
    try: 
        money = int(input('Enter your balance to make a withdrawal: $'))

        if money <= 0:
            print("Error: You can't withdrawl nothing.")

        else: 
            divider(money)
    
    except ValueError:
        print("Error: You entered an invalid value.")

if __name__ == '__main__':
    main()