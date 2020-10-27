#!/usr/bin/python3

import json

number = int(input("Whats your favorite number? "))
filename = 'favorite_number.json'

with open(filename, 'w') as f:
    json.dump(number, f)
