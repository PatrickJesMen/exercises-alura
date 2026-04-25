import os

os.system('cls')

def tip(a, b):
    return a + ( ( a/100 ) * b)

value = float(input("Enter the account amount : $"))
percentage = input("Enter the tip percentage : ")

clean_percentage = int(percentage.replace('%', ''))

r = tip(value, clean_percentage)

print(
    f'\nCOST: ${value}'
)
print(
    f'BILL: {clean_percentage}% (${(value/100)*clean_percentage:.2f})'
)
print(
    f'TOTAL COST: ${r}'
)