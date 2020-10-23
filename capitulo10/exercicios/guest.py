#!/usr/bin/python3

file = 'guest.txt'

guest = input("Enter your name: ")
with open(file, 'w') as file_object:
    file_object.write(guest)
