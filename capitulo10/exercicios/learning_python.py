#!/usr/bin/python3

file = 'learned.txt'

with open(file) as file_object:
    learned = file_object.read()
print(learned.rstrip())

for line in learned.readlines():
    print(line)
