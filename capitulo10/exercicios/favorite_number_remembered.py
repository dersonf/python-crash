#!/usr/bin/python3

import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = int(input("Whats your favorite number? "))
    with open(filename, 'w') as f:
        json.dump(number, f)
    print("I'll remember when you ask me again.")
else:
    print(f"I know your favorite number! It's {number}!")
