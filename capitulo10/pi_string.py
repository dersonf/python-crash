#!/usr/bin/python3

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
print(type(pi_string))
pi_string = float(pi_string)
print(type(pi_string))
print(pi_string)

