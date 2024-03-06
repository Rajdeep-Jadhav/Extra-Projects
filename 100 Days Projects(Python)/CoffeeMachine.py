# COFFEE MACHINE
print('Welcome to Coffee Machine!')
order = int(input('What would you like have?\n'
                  '1 = [ESPRESSO]\n'
                  '2 = [LATTE]\n'
                  '3 = [CAPPUCCINO] : '))

Materials = {
    'Water [ml]': 1000,
    'Milk  [ml]': 1000,
    'Coffee [g]': 250}

# --- COFFEES --- #
espresso = {
    'Water ': 50,
    'Milk  ': 0,
    'Coffee': 18,
    'Price ': 1.50
}
latte = {
    'Water ': 200,
    'Milk  ': 150,
    'Coffee': 24,
    'Price': 2.50
}
cappuccino = {
    'Water ': 250,
    'Milk  ': 100,
    'Coffee': 24,
    'Price': 3.00
}

# ---- COINS ---- #
coins = {
    'Penny   ($)': 0.01,
    'Nickel  ($)': 0.05,
    'Dime    ($)': 0.10,
    'Quarter ($)': 0.25}

if order == 1:
    print(f"\nEspresso Price : ${espresso['Price ']}")
elif order == 2:
    print(f"\nLatte Price : ${latte['Price']}")
elif order == 3:
    print(f"\nCappuccino Price : ${cappuccino['Price']}")
else:
    print('Enter Valid Input')

print('\nHow will you pay ?')
p = int(input('Enter number of Pennies($0.01)  :'))
n = int(input('Enter number of Nickels($0.05)  :'))
d = int(input('Enter number of Dimes($0.10)    :'))
q = int(input('Enter number of Quarters($0.25) :'))

user_paid = ((0.01 * p) + (0.05 * n) + (0.1 * d) + (0.25 * q))

change = 0
if order == 1:
    change = user_paid - espresso['Price ']
elif order == 2:
    change = user_paid - latte['Price']
elif order == 3:
    change = user_paid - cappuccino['Price']

change = change.__round__(2)
if change >= 0:
    print(f'\nYour change ${change}')
else:
    print(f'\nYou need to pay ${(-1) * change} more')
