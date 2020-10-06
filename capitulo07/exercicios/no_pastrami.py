#!/usr/bin/python3

sandwich_orders = [
    'Big Mac',
    'Pastrami',
    'Double Habibs',
    'Pastrami',
    'Mac chicken',
    'Pastrami',
    'Mac fish',
    ]
finished_sandwiches = []

print("AVISO: Acabou o Pastrami!!!\n")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == 'Pastrami':
        print(f"Sinto muito, acabou o {sandwich}!!!")
    else:
        print(f"Eu fiz seu {sandwich}!")
        finished_sandwiches.append(sandwich)

print("\nHoje fiz os seguintes sandwiches:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")
