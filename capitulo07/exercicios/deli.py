#!/usr/bin/python3

sandwich_orders = ['Big Mac', 'Double Habibs', 'Mac chicken', 'Mac fish']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Eu fiz seu {sandwich}!")
    finished_sandwiches.append(sandwich)

print("\nHoje fiz os seguintes sandwiches:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")
