#!/usr/bin/python3

file = 'learning_python.txt'

with open(file) as file_object:
    for line in file_object:
        print(line.replace('Python', 'GO').rstrip())
